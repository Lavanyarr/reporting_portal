from django.http import (
    response,
    HttpResponse
)

from reporting_portal_auth.exceptions.exception_messages import (
    INVALID_USERNAME,
    INVALID_PASSWORD
)
from reporting_portal_auth.interactors.presenters.presenter_interface \
    import PresenterInterface
from reporting_portal_auth.tests.storages.dtos import UserDTO


class PresenterImplementation(PresenterInterface):

    def raise_invalid_user_name_exception(self, username):

        import json
        response_object = response.HttpResponse(
            json.dumps({
                "response": INVALID_USERNAME[0],
                "https_status_code": 404,
                "res_status":INVALID_USERNAME[1]
            }),
            status=404
        )
        return response_object

    def raise_invalid_password_exception(self, password):
        import json
        response_object = response.HttpResponse(
            json.dumps({
                "response": INVALID_PASSWORD[0],
                "https_status_code": 404,
                "res_status": INVALID_PASSWORD[1]
            }),
            status=404
        )
        return response_object



    def get_user_token_response(
            self, user_dto: UserDTO) -> response.HttpResponse:
        import json
        response_data = {
            "Access_token": user_dto.user_token_dto.access_token,
            "Refresh_token": user_dto.user_token_dto.refresh_token,
            "role": user_dto.user_role
        }
        data = json.dumps(response_data)
        response = HttpResponse(data, status=200)
        return response

