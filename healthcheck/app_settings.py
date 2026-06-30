"""App settings."""

# Django
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

HEALTHCHECK_URL = getattr(settings, "HEALTHCHECK_URL", None)

if not HEALTHCHECK_URL:
    raise ImproperlyConfigured(
        "HEALTHCHECK_URL is not set. Add HEALTHCHECK_URL to your local.py settings."
    )
