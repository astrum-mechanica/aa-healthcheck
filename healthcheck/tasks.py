"""Tasks."""

# Third Party
import requests
from celery import shared_task

# Alliance Auth
from allianceauth.services.hooks import get_extension_logger

from .app_settings import HEALTHCHECK_URL

logger = get_extension_logger(__name__)


@shared_task(bind=True)
def heartbeat(self):
    try:
        requests.get(f"{HEALTHCHECK_URL}/start", timeout=10)
        # ping /start first — if the worker is stuck and never
        # gets here, healthchecks.io flags it as overdue
        requests.get(HEALTHCHECK_URL, timeout=10)
    except requests.RequestException as e:
        logger.warning(f"Healthchecks.io ping failed: {e}")
