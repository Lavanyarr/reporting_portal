'''

    TODO:
    tests for login interactor
    1. invalid username
    2. invalid password

    valid:
        1. valid username

        requirements: common-> oauth_user_auth_token(oauth2_storage)

        to_be_impelmented:
            1. test_invalid_username  21: 25
            2. test_invalid_password
            3. test_valid_credentails

        on_going:
            1. test_invalid_username

        completed:
         1. test_invalid_username  21: 25
            2. test_invalid_password
            3. test_valid_credentails


'''
from unittest.mock import (
    create_autospec,
    Mock,
    patch
)
import pytest

from reporting_portal_auth.constants.enums import Role
from reporting_portal_auth.interactors.login_interactor import \
    LoginInteractor
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from common.oauth2_storage import OAuth2SQLStorage


class TestLoginInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from reporting_portal_auth.interactors.storages.storage_interface \
            import StorageInterface
        storage = create_autospec(StorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from reporting_portal_auth.interactors.presenters.presenter_interface \
            import PresenterInterface
        presenter = create_autospec(PresenterInterface)
        return presenter

    @pytest.fixture()
    def oauth2_storage_mock(self):
        from common.oauth2_storage import OAuth2SQLStorage
        oauth_storage = create_autospec(OAuth2SQLStorage)
        return oauth_storage

    def test_login_with_invalid_username(
            self, storage_mock, presenter_mock, oauth2_storage_mock):
        from reporting_portal_auth.exceptions.exceptions import InvalidUserName
        # arrange
        username = 'lavanya1'
        password = "lavanya"

        interactor = LoginInteractor(storage=storage_mock,
                                     oauth_storage=oauth2_storage_mock)

        invalid_user_name = Mock()
        storage_mock.validate_user_name.side_effect = InvalidUserName
        presenter_mock.raise_invalid_user_name_exception.return_value = invalid_user_name

        # act
        response = interactor.user_login_wrapper(username=username,
                                                 password=password,
                                                 presenter=presenter_mock)
        # assert
        storage_mock.validate_user_name.assert_called_once_with(username=username)
        presenter_mock.raise_invalid_user_name_exception.assert_called_once_with(username=username)

    def test_login_with_invalid_password(
            self, storage_mock, presenter_mock, oauth2_storage_mock):
        from reporting_portal_auth.exceptions.exceptions import \
            InvalidPassword
        # arrange
        username = 'lavanya1'
        password = "lavanya"

        interactor = LoginInteractor(storage=storage_mock,
                                     oauth_storage=oauth2_storage_mock)

        storage_mock.validate_password.side_effect = InvalidPassword
        presenter_mock.raise_invalid_password_exception.return_value = Mock()

        # act
        response = interactor.user_login_wrapper(username=username,
                                                 password=password,
                                                 presenter=presenter_mock)
        # assert
        storage_mock.validate_password.assert_called_once_with(
                username=username, password=password)
        presenter_mock.raise_invalid_password_exception.assert_called_once_with(
            password=password
        )

    @patch.object(OAuthUserAuthTokensService, 'create_user_auth_tokens')
    def test_login_with_valid_username_and_password(self,
                                                    auth_token,
                                                    storage_mock,
                                                    presenter_mock,
                                                    oauth2_storage_mock):
        # arrange
        user_id = 1
        username = 'lavanya1'
        password = "lavanya1"
        role = 'USER'

        import dataclasses
        import datetime
        from common.oauth2_storage import OAuth2SQLStorage
        from reporting_portal_auth.tests.storages.dtos import (
            UserAuthTokensDTO,
            UserDTO
        )

        user_token_dto = UserAuthTokensDTO(user_id=1,
                                           access_token='XpCbV4bTl6v43HTsexE1SUxoNiO7qG',
                                           refresh_token='amNMDAKB1hMgMpHzjxr6rzHTz59SJo',
                                           expires_in=datetime.datetime(5189, 4, 11, 20, 55, 5, 722643)
                                           )

        user_dto = UserDTO(
            user_token_dto=user_token_dto,
            user_role=role
        )

        user_dto_response = Mock()
        auth_token.return_value = user_token_dto
        storage_mock.validate_password.return_value = user_id
        storage_mock.get_user_role.return_value = role
        presenter_mock.get_user_token_response.return_value = user_dto_response
        interactor = LoginInteractor(storage=storage_mock,
                                     oauth_storage=oauth2_storage_mock)

        # act
        response = interactor.user_login_wrapper(username=username,
                                                 password=password,
                                                 presenter=presenter_mock)

        # assert
        storage_mock.validate_user_name.assert_called_once_with(username=username)
        storage_mock.validate_password.assert_called_once_with(
            username=username, password=password)
        storage_mock.get_user_role.assert_called_once_with(user_id=user_id)

        presenter_mock.get_user_token_response.assert_called_once_with(user_dto=user_dto)

        assert response == user_dto_response
