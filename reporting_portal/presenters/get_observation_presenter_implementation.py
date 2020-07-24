from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from reporting_portal.constants.exception_messages import INVALID_OBSERVATION_IDS
from reporting_portal.interactors.presenters.get_observation_presenter_interface \
    import GetObservationPresenterInterface


class GetObservationPresenterImplementation(
        GetObservationPresenterInterface, HTTPResponseMixin):

    def prepare_invalid_observation_ids_response(self):
        response = {
            "response": INVALID_OBSERVATION_IDS[0],
            "https_status_code": 404,
            "res_status": INVALID_OBSERVATION_IDS[1]
        }

        return self.prepare_201_created_response(response_dict=response)