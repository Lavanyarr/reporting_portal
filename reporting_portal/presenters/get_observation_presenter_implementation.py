from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from reporting_portal.constants.exception_messages import (
    INVALID_OBSERVATION_IDS,
    INVALID_LIMIT, INVALID_OFFSET, INVALID_SORT_TYPE, INVALID_SORT_FIELD, INVALID_FILTER_TYPE
)
from reporting_portal.interactors.presenters.get_observation_presenter_interface \
    import GetObservationPresenterInterface
from reporting_portal.interactors.storages.dtos import UserObservationDTO


class GetObservationPresenterImplementation(
    GetObservationPresenterInterface, HTTPResponseMixin):

    def prepare_invalid_observation_ids_response(self):
        response = {
            "response": INVALID_OBSERVATION_IDS[0],
            "https_status_code": 404,
            "res_status": INVALID_OBSERVATION_IDS[1]
        }

        return self.prepare_404_not_found_response(response_dict=response)

    def prepare_invalid_limit_response(self):
        response = {
            "response": INVALID_LIMIT[0],
            "https_status_code": 404,
            "res_status": INVALID_LIMIT[1]
        }
        return self.prepare_404_not_found_response(response_dict=response)

    def prepare_invalid_offset_response(self):
        response = {
            "response": INVALID_OFFSET[0],
            "https_status_code": 404,
            "res_status": INVALID_OFFSET[1]
        }
        return self.prepare_404_not_found_response(response_dict=response)

    def prepare_invalid_sort_type_response(self):
        response = {
            "response": INVALID_SORT_TYPE[0],
            "https_status_code": 404,
            "res_status": INVALID_SORT_TYPE[1]
        }
        return self.prepare_404_not_found_response(response_dict=response)

    def prepare_invalid_filter_type_response(self):
        response = {
            "response": INVALID_FILTER_TYPE[0],
            "https_status_code": 404,
            "res_status": INVALID_FILTER_TYPE[1]
        }
        return self.prepare_404_not_found_response(response_dict=response)

    def prepare_invalid_sort_field_response(self):
        response = {
            "response": INVALID_SORT_FIELD[0],
            "https_status_code": 404,
            "res_status": INVALID_SORT_FIELD[1]
        }
        return self.prepare_404_not_found_response(response_dict=response)

    def prepare_my_observation_list(self, user_total_observation_dto: UserObservationDTO):

        my_observation_list = {}
        observation_list = self.get_my_observation_list(
            user_total_observation_dto
        )
        total_count = user_total_observation_dto.common_dto.total_count
        my_observation_list['total_observations_count'] = total_count
        my_observation_list['observation_details'] = observation_list

        return self.prepare_200_success_response(my_observation_list)

    def get_my_observation_list(self, user_total_observation_dto: UserObservationDTO):

        my_observation_list = []
        observation_details = user_total_observation_dto.common_dto.observation_details
        user_details = user_total_observation_dto.assigned_to

        for user_observations in observation_details:
            observation_dict = self.get_my_observation(user_observations)
            observation_dict['assigned_to'] = self.get_user_details(user_observations.assigned_to,
                                                                    user_details)
            my_observation_list.append(observation_dict)

        return my_observation_list

    def get_my_observation(self, observation_details):
        my_observation_dict = {}

        my_observation_dict['observation_id'] = observation_details.id
        my_observation_dict['title'] = observation_details.title
        my_observation_dict['reported_on'] = observation_details.reported_on

        my_observation_dict['severity'] = observation_details.severity
        my_observation_dict['status'] = observation_details.status
        my_observation_dict['due_date'] = self.get_due_date_of_observation(observation_details.due_date,
                                                                           observation_details.is_public)
        my_observation_dict['messages_count'] = observation_details.messages_count
        my_observation_dict['show_due_date'] = observation_details.is_public

        return my_observation_dict

    @staticmethod
    def get_user_details(assigned_to, user_details_dto):

        for user in user_details_dto:
            if user.user_id == assigned_to:
                user_dto = user.__dict__
                return user_dto

    def get_due_date_of_observation(self, due_date, is_public):
        if due_date == None:
            due_date = 'Not Set Due Date'
        elif is_public:
            due_date = due_date
        else:
            due_date = 'In Private'
        return due_date
