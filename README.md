# To-Fro

We're working on a system that can be used by different communities to help self organise, keep track of need and effectively deploy help.

Find instructions for deployment in the `deployment` directory.

## Development environment

To get running locally and quickly, download docker, clone this repository, then start the applications using this command:

    docker-compose up --build

Configuration is handled via the `.env` file. Environment variables will override what's defined in the `.env` file.

If `DEBUG=True`, then Django's development server will be used. This server includes hot-reload functionality and additional log information. If `DEBUG=False`, a production `gunicorn` server will be used.

During development, you should mount your local copy of the source code into the container. This is volume mount is encapsulated in the `development.yml` file. Do this by changing the command above to:

    docker-compose -f docker-compose.yml -f development.yml up --build

There are a couple of key benefits to mounting the source code as a volume.

1. Local changes to code get copied to the running container, enabling Django to hot-reload the application.
2. Changes to the filesystem in the container get copied to your local filesystem. This becomes useful when [adding apps to Django](https://docs.djangoproject.com/en/3.1/intro/tutorial01/#creating-the-polls-app).

## Useful commands

To execute a python command on the docker container, use a command like this:

    docker exec -it tofro-django python manage.py startapp test

You can see the names of the running containers with `docker ps`.

## Frontend

HTML is generated using [Django views](https://docs.djangoproject.com/en/3.1/topics/http/views/). Most modules of the application will have a `views.py` with the Python code grabbing the data and a `templates` folder containing the template files to be rendered by the views when answering the requests. Some also have a `templatetags` folder defining some [new filters and tags for Django's template language](https://docs.djangoproject.com/en/3.1/howto/custom-template-tags/).

The styles and scripts of the app are build with [ParcelJS](https://parceljs.org/) from the sources in `api/static-src`. The files are compiled to the `api/parcel-built`, which is in Django's `STATICFILES_DIRS` search path. These are then collected, along with images, by Django's `collectstatic` command.

These two steps (Parcel's build and Django's collectstatic) can be run together from the main frontend build script `api/build-scripts/build-frontend-assets.sh`. You will typically be running this inside the tofro-django container like so:

    docker exec tofro-django /code/build_scripts/build-frontend-assets.sh

## Application messages

The application relies on 3rd party packages whose messages needed to be overriden. This is done by taking advantage of [Django's localization system](https://docs.djangoproject.com/en/3.0/topics/i18n/translation/#localization-how-to-create-language-files), with a special language file in the `api/messages_overrides` folder, as described by [this StackOverflow answer](https://stackoverflow.com/a/41945558).

To override a piece of text coming from a 3rd party package:

1. Check that the piece of text is computed via Django's translation utilities. This can be a call to one of the `gettext()` methods (often aliased as `_()`) or using the `{% translate %}` tag.
2. Grab the ID of the message. This will be the string passed to the method or tag.
3. Add an entry to the `messages_overrides/en/LC_MESSAGES/django.po` file, as such:

    msgid "THE_ID_FOUND_IN_THE_3RD_PARTY_PACKAGE"
    msgstr "THE_MESSAGE_YOU_WANT_TO_SHOW"

    Pay attention to the case, as the `msgid` is case sensitive
4. Compile the messages with:

    docker exec -it tofro-django python3 manage.py compilemessages

## Testing

To check that everything works OK, there is a [manual testing plan in the TESTING.md](./TESTING.md) file.

## How notification emails for high priority actions get sent

1. Coordinator completes an `Action`  form choosing its priority as "HIGH"
1. The saved `Action` triggers a signal `post_save_action` in notifications.signals
1. `post_save_action` creates a job running `notifications.create_action_notifications`


   FROM THIS POINT WE ARE RUNNING ON `redis-worker` SERVER
1. `create_action_notifications` in `notifications.notifications` runs
   using the created `Action`. Because we have created a high priority `Action`
   `create_action_notifications` calls `create` in `notifications.notifications.py`
1. `create` in notifications.notifications.py calls
1. `gen_subject_and_message` in `notifications.utils.py` which works out
   the template name and then renders and returns the message content and
   subject using these templates.
1. `create` uses these values to create a new Notification and `save` it
1. new `Notification` triggers signal `post_save_notification` in `notifications.signals.py`
1. `post_save_notification` creates a redis `job` running `send` in `notifications.notifications.py`
1. `send` checks there are recipients, sends the notification by email and updates the `Notification`'s status accordingly
