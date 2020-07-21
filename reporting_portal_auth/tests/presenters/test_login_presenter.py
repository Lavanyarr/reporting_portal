import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from reporting_portal_auth.tests.factories.storage_dtos \
    import UserFactory
from reporting_portal_auth.presenters.presenter_implementation \
        import PresenterImplementation
import json
@pytest.mark.django_db
class TestLoginPresenter:

    def test_invalid_username_raise_exception(self, snapshot):

        #arrange
        username = 'lavanya'
        user = UserFactory.create(username='lavanya1', password='lavanya')
        presenter = PresenterImplementation()

        #act
        response = presenter.raise_invalid_user_name_exception(username)

        #assert
        data = json.loads(response.content)

        snapshot.assert_match(data, 'response')

    def test_invalid_password_raise_exception(self, snapshot):
        # arrange
        username = 'lavanya'
        password = "lavanya1"
        user = UserFactory.create(username='lavanya1', password='lavanya')
        presenter = PresenterImplementation()

        # act
        response = presenter.raise_invalid_password_exception(password)

        # assert
        data = json.loads(response.content)

        snapshot.assert_match(data, 'response')

    def test_get_user_token_response(self, snapshot):

        #arrange
        import datetime
        from reporting_portal_auth.constants.enums import Role
        from reporting_portal_auth.tests.storages.dtos import (
            UserAuthTokensDTO,
            UserDTO
        )
        role = Role.get_list_of_tuples()
        user_token_dto = UserAuthTokensDTO(user_id=1,
                                           access_token='XpCbV4bTl6v43HTsexE1SUxoNiO7qG',
                                           refresh_token='amNMDAKB1hMgMpHzjxr6rzHTz59SJo',
                                           expires_in=datetime.datetime(5189, 4, 11, 20, 55, 5, 722643)
                                           )

        user_dto = UserDTO(
            user_token_dto=user_token_dto,
            user_role=role
        )
        presenter = PresenterImplementation()

        #act
        response = presenter.get_user_token_response(user_dto)

        #assert

        data = json.loads(response.content)
        snapshot.assert_match(data, 'response')