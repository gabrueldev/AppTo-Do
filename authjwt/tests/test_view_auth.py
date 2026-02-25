
import pytest
from rest_framework.exceptions import ValidationError
from ..views import cadaster_view, login_view, delete_view, edit_view
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.test import APIClient
from django.urls import reverse

@pytest.mark.django_db
def test_cadaster_view():
    
    client = APIClient()

    data = {
        'username': 'gabruel',
        'email'   : 'gsr@gmail.com',
        'password': 'gabriel'
    }

    url = reverse("cadaster")
    response = client.post(url, data)

    assert response.status_code == 201

@pytest.mark.django_db
def test_login_view():
    client = APIClient()

    user = User.objects.create_user(
        username = 'gabruel',
        email    = 'gsr@gmail.com',
        password = 'gabriel'
    )

    url = reverse('login')

    response = client.post(url, {
        "username": "gabruel",
        "password": "gabriel"
    })

    assert response.status_code == 200
    assert "refresh" in response.data
    assert "access" in response.data

@pytest.mark.django_db
def test_dono_update_view():
    client = APIClient()

    user = User.objects.create_user(
        username = 'gabruel',
        email    = 'gsr@gmail.com',
        password = 'gabriel'
    )

    client.force_authenticate(user=user)
    
    url = reverse("edit", args=[user.username])
    response = client.patch(url, {"email": "gsr@gmail.com"})

    assert response.status_code == 200
    user.refresh_from_db()
    assert user.email == "gsr@gmail.com"

@pytest.mark.django_db
def test_fail_update_view():
    client = APIClient()

    user1 = User.objects.create_user(username="gabruel", password="123")
    user2 = User.objects.create_user(username="steffani", password="123")

    client.force_authenticate(user=user2)

    url = reverse("edit", args=[user1.username])

    response = client.patch(url, {
        "email": "gsr@gmail.com"
    })

    assert response.status_code == 403

@pytest.mark.django_db
def test_unauthenticated_edit_view():
    client = APIClient()

    user = User.objects.create_user(username="gabruel", password="123")

    url = reverse("edit", args=[user.username])

    response = client.patch(url, {
        "email": "gsr@gmail.com"
    })

    assert response.status_code == 401

@pytest.mark.django_db
def test_dono_delete_view():
    client = APIClient()

    user = User.objects.create_user(username="gabruel", password="123")

    client.force_authenticate(user=user)

    url = reverse("delete", args=[user.username])

    response = client.delete(url)

    assert response.status_code == 204
    assert User.objects.filter(username="gabruel").count() == 0

@pytest.mark.django_db
def test_fail_delete_view():
    client = APIClient()

    user1 = User.objects.create_user(username="gabruel", password="123")
    user2 = User.objects.create_user(username="steffani", password="123")

    client.force_authenticate(user=user2)

    url = reverse("delete", args=[user1.username])

    response = client.delete(url)

    assert response.status_code == 403