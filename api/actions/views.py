from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from actions.models import Action, ActionStatus, ActionFeedback
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils import timezone
from django.views import generic
from django.urls import reverse
from .forms import ActionFeedbackForm, ActionCancellationForm
from datetime import datetime


LIST_DEFINITIONS = {
    'available': {
        'title': "Here's what you can do to help",
        'heading': "Here's what you can do to help",
        'queryset': lambda volunteer:
            volunteer.available_actions.order_by(
                'requested_datetime', '-action_priority')
    },
    'completed': {
        'title': "Your completed actions",
        'heading': "Your completed actions",
        'queryset': lambda volunteer:
            volunteer.completed_actions.order_by(
                'requested_datetime', '-action_priority')
    },
    'ongoing': {
        'title': "Your ongoing actions",
        'heading': "Your ongoing actions",
        'queryset': lambda volunteer:
            volunteer.ongoing_actions.order_by(
                'requested_datetime', '-action_priority'
            )
    },
    'mine': {
        'title': "Your upcoming actions",
        'heading': "Your upcoming actions",
        'queryset': lambda volunteer:
        # order first by action_status to make the assigned
        # actions appear first
        volunteer.upcoming_actions.order_by(
            '-action_status', 'requested_datetime', '-action_priority')
    }
}


class ActionsListView(generic.ListView):
    template_name = 'actions/index.html'
    context_object_name = 'actions'
    list_type = 'available'
    paginate_by = 20

    def get_queryset(self):
        volunteer = self.request.user.volunteer
        # Avoid N+1 queries when rendering the list of actions
        return LIST_DEFINITIONS[self.list_type]['queryset'](volunteer).select_related('help_type', 'resident', 'resident__ward')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['current_list_type'] = self.list_type
        context['title'] = LIST_DEFINITIONS[self.list_type]['title']
        context['heading'] = LIST_DEFINITIONS[self.list_type]['heading']
        return context


def back_url(action, volunteer):
    if (action.assigned_volunteer != volunteer):
        return reverse('actions:available')

    if (action.action_status == ActionStatus.INTEREST or action.action_status == ActionStatus.ASSIGNED):
        return reverse('actions:index')

    if (action.action_status == ActionStatus.ONGOING):
        return reverse('actions:ongoing')

    if (action.action_status == ActionStatus.COULDNT_COMPLETE or action.action_status == ActionStatus.COMPLETED):
        return reverse('actions:completed')

    return reverse('actions:available')


def pkdetail(request, action_pk):
    action = get_object_or_404(Action, pk=action_pk)
    return redirect(action, permanent=True)


def detail(request, action_uuid):
    volunteer = request.user.volunteer
    action = get_object_or_404(Action, action_uuid=action_uuid)

    if request.method == "POST":
        if request.POST.get('_action') == 'contact':
            action.volunteer_made_contact_on = timezone.now()
            action.save()
        else:
            # Check if the action still needs volunteers to register interest.

            if request.POST.get('_action') == 'withdraw_help':
                if action.action_status == ActionStatus.PENDING \
                        or action.action_status == ActionStatus.INTEREST:

                    action.withdraw_interest_from(volunteer)
                    messages.info(
                        request, 'Noted! Sorry to hear you can no longer help.')

                else:
                    if (action.assigned_volunteer == volunteer):
                        messages.error(request,
                                       'Sorry, looks like your help was already accepted. Please contact a coordinator make arrangements.')
            else:
                if action.action_status == ActionStatus.PENDING \
                        or action.action_status == ActionStatus.INTEREST:

                    action.register_interest_from(volunteer)
                    messages.success(request, 'Thanks for volunteering!')

                else:
                    messages.error(
                        request, 'Thanks, but someone has already volunteered to help')
        return redirect(action)

    context = {
        'action': action,
        'back_url': back_url(action, volunteer),
        'title': f"{str(action.help_type).title()} - {str(action.ward).title()} (Action no. {action.id})",
        'heading': action.description,
        'volunteer': volunteer
    }

    return render(request, 'actions/detail.html', context)


def stop_ongoing(request, action_uuid):
    return action_feedback(request, action_uuid, template_name="actions/stop_ongoing.html", Form=ActionCancellationForm, extra_context={
        'title': 'Your collaboration is stopping',
        'heading': 'Your collaboration is stopping'
    })


def action_feedback(request, action_uuid, template_name='actions/complete.html', Form=ActionFeedbackForm, extra_context={}):
    volunteer = request.user.volunteer
    action = get_object_or_404(Action, action_uuid=action_uuid)

    if action.assigned_volunteer != volunteer or not action.can_give_feedback:
        return redirect(action)

    # Get feedback from the volunteer.
    feedback = ActionFeedback(action=action,
                              volunteer=action.assigned_volunteer,
                              created_date_time=timezone.now())
    form = Form(request.POST or None,
                instance=feedback, action=action)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, 'Nice work! Thanks for helping out!')
        return redirect(action)

    context = {
        'action': action,
        'back_url': action.get_absolute_url(),
        'title': 'How did it go?',
        'heading': 'How did it go?',
        'form': form,
        **extra_context
    }

    return render(request, template_name, context)
