import pytest

from reporting_portal_auth.storages.storage_implementation \
    import StorageImplementation
from reporting_portal_auth.exceptions.exceptions import \
    InvalidPassword
from reporting_portal_auth.tests.factories.storage_dtos \
    import UserFactory


@pytest.mark.django_db
class TestGetRole:

    def test_user_role(self, snapshot):
        username = 'lavanya1'
        password = "lavanya"
        UserFactory.reset_sequence()
        user = UserFactory.create(username='lavanya1', password='lavanya', user_role='USER')

        storage = StorageImplementation()
        user_id = storage.validate_password(username=username,
                                      password=password)

        #act
        response = storage.get_user_role(user_id=user_id)

        #assert
        snapshot.assert_match(response, 'role')

