import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "demo_python_django_cookiecutter.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import demo_python_django_cookiecutter.users.signals  # noqa: F401
