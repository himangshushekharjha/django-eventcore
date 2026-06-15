import pytest
from django.apps import apps
from django.urls import reverse


def test_eventcore_app_is_registered():
    """The `eventcore` app config resolves, proving it's wired into INSTALLED_APPS."""
    app_config = apps.get_app_config("eventcore")
    assert app_config.name == "eventcore"


@pytest.mark.django_db
def test_admin_index_redirects_to_login(client):
    """A GET to the admin index redirects anonymous users to the login page."""
    response = client.get(reverse("admin:index"))
    assert response.status_code == 302
    assert response.url.startswith("/admin/login/")
