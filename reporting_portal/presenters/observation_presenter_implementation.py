from django.http import response
from reporting_portal.interactors.presenters.observation_presenter_interface \
    import ObservationPresenterInterface

from reporting_portal.exceptions.exception_messages import (
    INVALID_CATEGORY_ID,
    INVALID_SUBCATEGORY_ID
)


class ObservationPresenterImplementation(ObservationPresenterInterface):
    def get_create_observation_response(self):
        import json
        response_object = response.HttpResponse(
            json.dumps("observation_created"),
            status=201
        )
        return response_object

    def raise_invalid_category_id_exception(self):
        import json
        response_object = response.HttpResponse(
            json.dumps({
                "response": INVALID_CATEGORY_ID[0],
                "https_status_code": 404,
                "res_status": INVALID_CATEGORY_ID[1]
            }), status=404
        )
        return response_object

    def raise_invalid_subcategory_id_for_category_exception(self):
        import json
        response_object = response.HttpResponse(
            json.dumps({
                "response": INVALID_SUBCATEGORY_ID[0],
                "https_status_code": 404,
                "res_status": INVALID_SUBCATEGORY_ID[1]
            }), status=404
        )
        return response_object
