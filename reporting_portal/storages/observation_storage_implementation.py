from typing import List

from reporting_portal.interactors.storages.observation_storage_interface \
    import ObservationStorageInterface
from reporting_portal.models import Observation
from reporting_portal.interactors.storages.dtos import ObservationDetailsDTO


class ObservationStorageImplementation(ObservationStorageInterface):

    def get_valid_observation_ids(self, observation_ids: List[int]):
        observation_ids = Observation.objects.filter(id__in=observation_ids) \
            .values_list('id', flat=True)
        return observation_ids

    def get_observation_details(self, valid_observation_ids: List[int]):
        observation_objs = Observation.objects.filter(id__in=valid_observation_ids)
        observation_dto = self.convert_observation_obj_to_observation_dto(observation_objs)
        return observation_dto

    @staticmethod
    def convert_observation_obj_to_observation_dto(observation_objs):
        observation_dto_list = []

        for observation in observation_objs:
            observation_dto = ObservationDetailsDTO(
                title=observation.title,
                severity=observation.severity,
                status=observation.status,
                due_date=observation.due_date,
                messages_count=0
            )
            observation_dto_list.append(observation_dto)

        return observation_dto_list
