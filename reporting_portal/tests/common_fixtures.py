from typing import List

from reporting_portal.interactors.storages.dtos import UserDTO


def prepare_get_user_dtos_mock(mocker, user_ids: List[int]):
    mock = mocker.patch('reporting_portal.adapters.auth_service.AuthService.get_user_dtos')
    user_dtos = [
        UserDTO(
            user_id=user_id,
            name="user_{}".format(_index + 1),
            profile_pic="profile_{}".format(_index + 1),
            phone_no="99999999_{}".format(_index+1)
        ) for _index, user_id in enumerate(user_ids)
    ]

    mock.return_value = user_dtos
    return mock