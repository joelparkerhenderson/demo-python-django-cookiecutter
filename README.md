# Demo Python Django Cookiecutter

# Demo Python Django Cookiecutter AWS

Demonstration of:

* [Python](https://www.python.org/) programming language

* [Django](https://www.djangoproject.com/) web framework

* [Cookiecutter](https://github.com/cookiecutter/cookiecutter-django) framework for jumpstarting Django projects

* [AWS](https://aws.amazon.com/) cloud services
  
This demo briefly touches on these additional areas:

* [WhiteNoise](https://whitenoise.readthedocs.io/) simplified static file serving for Python web apps

* [Celery](https://docs.celeryproject.org/) distributed task queue
  
* [Flower](https://flower.readthedocs.io/) web application for monitoring and managing Celery clusters

* [Docker](https://www.docker.com/) containerization

* [Sentry](https://sentry.io/) application monitoring software

* [Mailpit](https://mailpit.axllent.org/) email testing for developers

Beyond this demo, you may want to know about related areas such as:

* [Django REST Framework (DRF)](https://www.django-rest-framework.org/)

* [Django Ninja](https://django-ninja.dev/) web framework for building APIs with Django and Python 3.6+ type hints.

* [Django Watson](https://github.com/etianen/django-watson](Full-text multi-table search application for Django)

Hosting suggestions: 

* [Pythonanywhere](https://www.pythonanywhere.com/) - host, run, and code Python in the cloud

* [Appliku](https://appliku.com/) - modern application deployment platform

* [Hetzner](https://www.hetzner.com/) - truly thrifty cloud hosting with virtual private servers

* [Coolify](https://coolify.io/) - open-source platform as a service (PaaS)

* [Railway](https://railway.com/) - infrastructure platform

* [Kubero](https://github.com/kubero-dev/kubero) designed for small 12- Factor apps

* AWS Multiple locations, failover, cloudfront with waf, elastic beanstalk controlling ec2 in three zones, postgresql mirrored. 300 domains on my Django cms and apps. 

* Google CloudRun ($0 for small use cases), Google CloudSQL Postgres instance ($9/month for the smallest instance) and Google Cloud Storage ($2/month for 100GB and optional micro google compute instance if you need stateful services such as redis, celery, etc.), Google Secret Manager

## Prerequisites

Example to get prerequisites with macOS and brew package manager:

```sh
brew install python
brew install postgresql
brew install redis
```

### Python

Verify you have Python 3.13+ and pip 24.3.1+:

```sh
python --version
pip --version
```

### PostgreSQL

Verify you have PostgresSQL 16.6+:

```sh
psql --version
```

Verify it works:

```sh
pg_ctl status
```

### Redis

Verify you have Redis 7.2.6+:

```sh
redis-server --version
```

Verify it works:

```sh
redis-cli ping
```

## Start

### Virtual environment

Create a virtual environment named for this project then activate it:

```sh
python -m venv demo && source demo/bin/activate
```

### Cookiecutter

Install cookiecutter:

```sh
python -m pip install --user cookiecutter
```

Verify you have cookiecutter 2.6.0+:

```sh
cookiecutter --version
```

Generate a new cookiecutter-django project:

```sh
cookiecutter gh:cookiecutter/cookiecutter-django
```

Interaction:

```txt
You've downloaded ~/.cookiecutters/cookiecutter-django before. 
Is it okay to delete and re-download it? [y/n] (y): 
  [1/27] project_name (My Awesome Project): Demo Python Django Cookiecutter    
  [2/27] project_slug (demo_python_django_cookiecutter): 
  [3/27] description (Behold My Awesome Project!): Demonstration of Python and Django and Cookiecutter
  [4/27] author_name (Daniel Roy Greenfeld): Joel Parker Henderson
  [5/27] domain_name (example.com): joelparkerhenderson.com
  [6/27] email (joel-parker-henderson@joelparkerhenderson.com): joel@joelparkerhenderson.com
  [7/27] version (0.1.0): 
  [8/27] Select open_source_license
    1 - MIT
    2 - BSD
    3 - GPLv3
    4 - Apache Software License 2.0
    5 - Not open source
    Choose from [1/2/3/4/5] (1): 3
  [9/27] Select username_type
    1 - username
    2 - email
    Choose from [1/2] (1): 2
  [10/27] timezone (UTC): 
  [11/27] windows (n): 
  [12/27] Select editor
    1 - None
    2 - PyCharm
    3 - VS Code
    Choose from [1/2/3] (1): 3
  [13/27] use_docker (n): y
  [14/27] Select postgresql_version
    1 - 16
    2 - 15
    3 - 14
    4 - 13
    5 - 12
    Choose from [1/2/3/4/5] (1): 1
  [15/27] Select cloud_provider
    1 - AWS
    2 - GCP
    3 - Azure
    4 - None
    Choose from [1/2/3/4] (1): 1
  [16/27] Select mail_service
    1 - Mailgun
    2 - Amazon SES
    3 - Mailjet
    4 - Mandrill
    5 - Postmark
    6 - Sendgrid
    7 - Brevo
    8 - SparkPost
    9 - Other SMTP
    Choose from [1/2/3/4/5/6/7/8/9] (1): 2
  [17/27] use_async (n): y
  [18/27] use_drf (n): y
  [19/27] Select frontend_pipeline
    1 - None
    2 - Django Compressor
    3 - Gulp
    4 - Webpack
    Choose from [1/2/3/4] (1): 4
  [20/27] use_celery (n): y
  [21/27] use_mailpit (n): y
  [22/27] use_sentry (n): y
  [23/27] use_whitenoise (n): y
  [24/27] use_heroku (n): n
  [25/27] Select ci_tool
    1 - None
    2 - Travis
    3 - Gitlab
    4 - Github
    5 - Drone
    Choose from [1/2/3/4/5] (1): 4
  [26/27] keep_local_envs_in_vcs (y): y
  [27/27] debug (n): 
```

Cookiecutter creates a file so you can replay the choices later:

```sh
cat ~/.cookiecutter_replay/cookiecutter-django.json
```

The output JSON starts with this:

```json
{
  "cookiecutter": {
    "project_name": "Demo Python Django Cookiecutter",
    "project_slug": "demo_python_django_cookiecutter",
    "description": "Demonstration of Python and Django and Cookiecutter",
    "author_name": "Joel Parker Henderson",
    "domain_name": "joelparkerhenderson.com",
    "email": "joel@joelparkerhenderson.com",
    "version": "0.1.0",
    "open_source_license": "GPLv3",
    "username_type": "email",
    "timezone": "UTC",
    "windows": "n",
    "editor": "VS Code",
    "use_docker": "y",
    "postgresql_version": "16",
    "cloud_provider": "AWS",
    "mail_service": "Amazon SES",
    "use_async": "y",
    "use_drf": "y",
    "frontend_pipeline": "Webpack",
    "use_celery": "y",
    "use_mailpit": "y",
    "use_sentry": "y",
    "use_whitenoise": "y",
    "use_heroku": "n",
    "ci_tool": "Github",
    "keep_local_envs_in_vcs": "y",
    "debug": "n",
    "_template": "gh:cookiecutter/cookiecutter-django",
    "_output_dir": "/Users/jph/git/joelparkerhenderson/demo",
    "_repo_dir": "/Users/jph/.cookiecutters/cookiecutter-django",
    "_checkout": null
  }
}
```

# Original README.md
Demonstration of Python and Django and Cookiecutter

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: GPLv3

## Settings

Moved to [settings](https://cookiecutter-django.readthedocs.io/en/latest/1-getting-started/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy demo_python_django_cookiecutter

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/2-local-development/developing-locally.html#using-webpack-or-gulp).

### Celery

This app comes with Celery.

To run a celery worker:

```bash
cd demo_python_django_cookiecutter
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important _where_ the celery commands are run. If you are in the same folder with _manage.py_, you should be right.

To run [periodic tasks](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html), you'll need to start the celery beat scheduler service. You can start it as a standalone process:

```bash
cd demo_python_django_cookiecutter
celery -A config.celery_app beat
```

or you can embed the beat service inside a worker with the `-B` option (not recommended for production use):

```bash
cd demo_python_django_cookiecutter
celery -A config.celery_app worker -B -l info
```

### Email Server

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [Mailpit](https://github.com/axllent/mailpit) with a web interface is available as docker container.

Container mailpit will start automatically when you will run all docker containers.
Please check [cookiecutter-django Docker documentation](https://cookiecutter-django.readthedocs.io/en/latest/2-local-development/developing-locally-docker.html) for more details how to start all containers.

With Mailpit running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](https://cookiecutter-django.readthedocs.io/en/latest/3-deployment/deployment-with-docker.html).

### Custom Bootstrap Compilation

The generated CSS is set up with automatic Bootstrap recompilation with variables of your choice.
Bootstrap v5 is installed using npm and customised by tweaking your variables in `static/sass/custom_bootstrap_vars`.

You can find a list of available variables [in the bootstrap source](https://github.com/twbs/bootstrap/blob/v5.1.3/scss/_variables.scss), or get explanations on them in the [Bootstrap docs](https://getbootstrap.com/docs/5.1/customize/sass/).

Bootstrap's javascript as well as its dependencies are concatenated into a single file: `static/js/vendors.js`.
