from django.apps import AppConfig


class ReportingPortalAuthAppConfig(AppConfig):
    name = "reporting_portal_auth"

    def ready(self):
        from reporting_portal_auth import signals # pylint: disable=unused-variable
