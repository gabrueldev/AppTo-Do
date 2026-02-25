
import pytest
from ..serializers import cadaster_serializer
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_cadaster_serializer():

    data = {
        'username': 'gabruel',
        'email': 'gsr@gmail.com',
        'password': 'banana'
    }

    serializer = cadaster_serializer(data=data)

    assert serializer.is_valid()
    user = serializer.save()

    print(serializer.errors)
    assert user.username == 'gabruel'
    assert user.email == 'gsr@gmail.com'
    assert user.check_password('banana')