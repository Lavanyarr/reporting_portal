from typing import List

from reporting_portal.interactors.storages.observation_storage_interface \
    import ObservationStorageInterface
from reporting_portal.models import Observation
from reporting_portal.interactors.storages.dtos import ObservationDetailsDTO, ObservationDetailsWithCount


class ObservationStorageImplementation(ObservationStorageInterface):

    def get_valid_observation_ids(self, observation_ids: List[int]):
        observation_ids = Observation.objects.filter(id__in=observation_ids) \
            .values_list('id', flat=True)
        return observation_ids

    def get_observation_details(self, valid_observation_ids: List[int]):
        observation_objs = Observation.objects.filter(id__in=valid_observation_ids)
        total_count = observation_objs.count()
        observation_dto = self.convert_observation_obj_to_observation_dto(observation_objs)
        observation_details_dto = ObservationDetailsWithCount(
            total_count=total_count,
            observation_details=observation_dto
        )
        return observation_details_dto

    @staticmethod
    def convert_observation_obj_to_observation_dto(observation_objs):
        observation_dto_list = []

        for observation in observation_objs:
            observation_dto = ObservationDetailsDTO(
                id=observation.id,
                title=observation.title,
                severity=observation.severity,
                status=observation.status,
                due_date=observation.due_date,
                messages_count=0,
                reported_on=observation.reported_on,
                assigned_to=observation.assigned_to,
                is_public=observation.is_public
            )
            observation_dto_list.append(observation_dto)

        return observation_dto_list

    def get_my_observation_in_dec_when_given_sort_field_is_reported_on(
            self, observation_dto: ObservationDetailsDTO):

        offset = observation_dto.offset
        limit = observation_dto.limit
        observation_objs = Observation.objects.filter(
            status=observation_dto.filter_type).order_by('-reported_on')[limit: offset + limit]
        return observation_objs

    def get_my_observation_in_dec_when_given_sort_field_is_due_date(
            self, observation_dto: ObservationDetailsDTO):
        offset = observation_dto.offset
        limit = observation_dto.limit
        observation_objs = Observation.objects.filter(
            status=observation_dto.filter_type).order_by('-due_date')[limit: offset + limit]
        return observation_objs

    def get_my_observation_when_given_sort_field_is_reported_on(
            self, observation_dto: ObservationDetailsDTO):
        offset = observation_dto.offset
        limit = observation_dto.limit
        observation_objs = Observation.objects.filter(
            status=observation_dto.filter_type).order_by('reported_on')[limit: offset + limit]
        return observation_objs

    def get_my_observation_when_given_sort_field_is_due_date(
            self, observation_dto: ObservationDetailsDTO):
        offset = observation_dto.offset
        limit = observation_dto.limit
        observation_objs = Observation.objects.filter(
            status=observation_dto.filter_type).order_by('due_date')[limit: offset + limit]
        return observation_objs
