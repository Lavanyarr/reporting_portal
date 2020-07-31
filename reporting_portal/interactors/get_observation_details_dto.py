from typing import List

from reporting_portal.exceptions.exceptions import InvalidObservationIds
from reporting_portal.interactors.storages.observation_storage_interface \
    import ObservationStorageInterface

from reporting_portal.interactors.presenters.get_observation_presenter_interface \
    import GetObservationPresenterInterface


class GetObservationDTOInteractor:

    def __init__(self, observation_storage: ObservationStorageInterface):
        self.storage = observation_storage

    def get_observation_details_dto_wrapper(self, observation_ids: List[int],
                                            observation_presenter: GetObservationPresenterInterface):
        try:
            response = self.get_observation_details_dto(observation_ids)
        except InvalidObservationIds:
            response = observation_presenter.prepare_invalid_observation_ids_response()
        return response

    def get_observation_details_dto(self, observation_ids: List[int]):

        unique_observation_ids = self.get_unique_observation_ids(observation_ids)
        valid_observation_ids = self.storage.get_valid_observation_ids(unique_observation_ids)

        invalid_observation_ids = [
            observation_id
            for observation_id in observation_ids if observation_id not in valid_observation_ids
        ]

        if invalid_observation_ids:
            raise InvalidObservationIds
        # use valid_observation_ids for dto

        observation_dtos = self.storage.get_observation_details(
            valid_observation_ids=valid_observation_ids)

        return observation_dtos

    @staticmethod
    def get_unique_observation_ids(observation_ids):
        observation_ids_list = []
        for observation_id in observation_ids:
            if observation_id not in observation_ids_list:
                observation_ids_list.append(observation_id)

        return observation_ids_list
