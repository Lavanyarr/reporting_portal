from django.http import response

from reporting_portal_auth.interactors.presenters.user_dtos_presenter_interface \
    import UserDetailsPresenterInterface

from reporting_portal_auth.exceptions.exception_messages import INVALID_USER_IDS


class PresenterImplementation(UserDetailsPresenterInterface):

    def raise_invalid_user_ids_exception(self):
        import json
        response_object = response.HttpResponse(
            json.dumps({
                "response": INVALID_USER_IDS[0],
                "https_status_code": 404,
                "res_status": INVALID_USER_IDS[1]
            })
        )
        return response_object
