'''

test validate user
'''

import pytest

from reporting_portal_auth.storages.storage_implementation \
    import StorageImplementation
from reporting_portal_auth.exceptions.exceptions import \
    InvalidUserName
from reporting_portal_auth.tests.factories.storage_dtos \
    import UserFactory


@pytest.mark.django_db
class TestvalidateUserName:

    def test_username_with_invalid_username(self):
        username = "user2"
        user = UserFactory.create(username='lavanya1', password='lavanya')

        storage = StorageImplementation()

        # act
        with pytest.raises(InvalidUserName):
            storage.validate_user_name(username=username)

    def test_username_with_valid_username(self):
        username = "username_1"
        UserFactory.reset_sequence()
        UserFactory.create(name="lavanya", password='lavanya1')

        storage = StorageImplementation()

        # act
        storage.validate_user_name(username=username)
