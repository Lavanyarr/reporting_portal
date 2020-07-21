import pytest

from reporting_portal_auth.storages.storage_implementation \
    import StorageImplementation
from reporting_portal_auth.exceptions.exceptions import \
    InvalidPassword
from reporting_portal_auth.tests.factories.storage_dtos \
    import UserFactory


@pytest.mark.django_db
class TestvalidatePassword:

    def test_password_with_invalid_password(self):
        username = 'lavanya1'
        password = "lavanya1"
        user = UserFactory.create(username='lavanya1', password='lavanya')

        storage = StorageImplementation()

        # act
        with pytest.raises(InvalidPassword):
            storage.validate_password(username=username,
                                      password=password)

    def test_password_with_valid_password(self, snapshot):

        username ='lavanya'
        password = "lavanya1"
        user = UserFactory.create(username='lavanya', password='lavanya1')

        storage = StorageImplementation()

        # act
        response = storage.validate_password(username=username,
                                             password=password)

        #assert
        snapshot.assert_match(response,'user_id')