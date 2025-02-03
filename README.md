# Demo Python Django Cookiecutter

Demonstration of:

- [Python](https://www.python.org/) programming language

- [Django](https://www.djangoproject.com/) web framework

- [Cookiecutter](https://github.com/cookiecutter/cookiecutter-django) framework for jumpstarting Django projects

- [AWS](https://aws.amazon.com/) cloud services

This demo briefly touches on these additional areas:

- [WhiteNoise](https://whitenoise.readthedocs.io/) simplified static file serving for Python web apps

- [Celery](https://docs.celeryproject.org/) distributed task queue

- [Flower](https://flower.readthedocs.io/) web application for monitoring and managing Celery clusters

- [Docker](https://www.docker.com/) containerization

- [Sentry](https://sentry.io/) application monitoring software

- [Mailpit](https://mailpit.axllent.org/) email testing for developers

- [Ruff](https://github.com/astral-sh/ruff) fast Python linter and code formatter, written in Rust

Beyond this demo, you may want to know about related areas such as:

- [Django REST Framework (DRF)](https://www.django-rest-framework.org/)

- [Django Ninja](https://django-ninja.dev/) web framework for building APIs with Django and Python 3.6+ type hints.

- [Django Watson](https://github.com/etianen/django-watson) Full-text multi-table search application for Django.

Hosting suggestions:

- [Pythonanywhere](https://www.pythonanywhere.com/) - host, run, and code Python in the cloud

- [Appliku](https://appliku.com/) - modern application deployment platform

- [Hetzner](https://www.hetzner.com/) - truly thrifty cloud hosting with virtual private servers

- [Coolify](https://coolify.io/) - open-source platform as a service (PaaS)

- [Railway](https://railway.com/) - infrastructure platform

- [Kubero](https://github.com/kubero-dev/kubero) designed for small 12- Factor apps

- AWS Multiple locations, failover, cloudfront with waf, elastic beanstalk controlling ec2 in three zones, postgresql mirrored. 300 domains on my Django cms and apps.

- Google CloudRun ($0 for small use cases), Google CloudSQL Postgres instance ($9/month for the smallest instance) and Google Cloud Storage ($2/month for 100GB and optional micro google compute instance if you need stateful services such as redis, celery, etc.), Google Secret Manager

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

### Django

Install:

```sh
python -m pip install --user django
```

Verify:

```sh
python -m django --version
```

### Cookiecutter

Install cookiecutter:

```sh
python -m pip install --user cookiecutter
```

Verify:

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

### Cookiecutter output JSON

Cookiecutter creates a JSON file so you can replay the choices later:

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

### Cookiecutter output directories and files

Project-related:

- `.envs` = Environment variables for local development and production deployment.

- `config` = Configuration files for various services.

- `demo_python_django_cookiecutter` = Python package for this project.

- `docs` = Documentation

- `locale` = Locale specific settings, typically for languages and translations.

- `manage.py` = [Django management](https://docs.djangoproject.com/en/5.1/ref/django-admin/) command-line utility for administrative tasks, akin to an easier django-admin.

- `merge_production_dotenvs_in_dotenv.py` = The intent is that production env files are NOT into source control, because they contain secrets However, they are added to the docker image by docker-compose when you run it.

- `package.json` = [Node.js](https://nodejs.org/) fundamental manifest, storing information about applications, modules, packages, and more.

- `pyproject.toml` = configuration file used by packaging tools, as well as other tools such as linters, type checkers, etc.

- `requirements` = Python package requirements file which lists all the dependencies your project needs, and can be used to install those dependencies using pip.

- `tests` = Project-specific tests.

Git-related:

- `.git` = [git](https://git-scm.com/) version control repository

- `.gitattributes` = [gitattributes](https://git-scm.com/docs/gitattributes) tells git to use attributes to pathnames.

- `.github` = [GitHub](https://github.com/) configuration files, such as for GitHub workflows.

- `.gitignore` = [gitignore](https://git-scm.com/docs/gitignore) tells git which files to ignore.

Docker-related:

- `.devcontainer` = The configuration files for a dev container.

- `.dockerignore` = [Docker](https://docs.docker.com/reference/dockerfile/) file that describes files and directories that you want to exclude when building a Docker image.

- `compose` = [Docker Compose](https://docs.docker.com/compose/) is a tool for defining and running multi-container applications..

- `docker-compose.docs.yml` = [Docker Compose](https://docs.docker.com/compose/) instructions for the documentation.

- `docker-compose.local.yml` = [Docker Compose](https://docs.docker.com/compose/) instructions for local development.

- `docker-compose.production.yml` = [Docker Compose](https://docs.docker.com/compose/) instructions for production deployment.

Adjunct-tool-related:

- `.editorconfig` = [EditorConfig](https://editorconfig.org/) is tool for maintaining consistent coding styles.

- `.pre-commit-config.yaml` = [pre-commit](https://pre-commit.com/) is a framework for managing and maintaining multi-language pre-commit hooks.

- `.readthedocs.yml` = [Read The Docs](https://readthedocs.com) is a tool to help build, host, and share documentation.

- `cspell.json` = [CSpell](https://cspell.org/) is a a spell checker for code.

- `webpack` = [webpack](https://webpack.js.org/) is a tool that bundles JavaScript files and other assets into static bundles for use in browsers.

Generic-repository-related:

- `./README.md` = Top level documentation

- `./CONTRIBUTORS.txt` = List of people who have made significant contributions.

- `./COPYING` = Copying license, such as the GPL-3 license.

- `./LICENSE` = General license, such as the GPL-3 license.

## Settings

Read about [settings](https://cookiecutter-django.readthedocs.io/en/latest/1-getting-started/settings.html).

## Get pre-comment

Run:

```
pip install --upgrade pip
pip install pre-commit
pre-commit install
pre-commit
pre-commit run --all-files
```

Success looks like a bunch of green checks, and maybe some red warnings.

```stdout
djLint linting for Django...Passed
```

## Docker

Follow [Getting Up and Running Locally With Docker](https://cookiecutter-django.readthedocs.io/en/latest/2-local-development/developing-locally-docker.html)

Build the stack:

```sh
docker compose -f docker-compose.local.yml build
```

You should see Docker downloading dependencies and building them.

Success looks like:

```stdout
✔ Service postgres      Built
✔ Service celerybeat    Built
✔ Service django        Built
✔ Service celeryworker  Built
✔ Service flower        Built
✔ Service node          Built
```

Run the stack:

```sh
docker compose -f docker-compose.local.yml up
```

The site should start and be accessible.

- If you selected Webpack or Gulp as your frontend pipeline, then visit [http://localhost:3000](http://localhost:3000).

- Otherwise, visit [http://localhost:8000](http://localhost:8000) otherwise.
