from reporting_portal.interactors.storages.storage_interface \
    import StorageInterface
from reporting_portal.interactors.presenters.observation_presenter_interface \
    import ObservationPresenterInterface
from reporting_portal.interactors.storages.dtos import ObservationDTO
from reporting_portal.exceptions.exceptions import (
    InvalidCategoryId,
    InvalidSubCategoryId
)


class CreateObservationInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_observation_wrapper(self, observation_dto: ObservationDTO,
                                   presenter: ObservationPresenterInterface):

        try:
            self.create_observation(observation_dto)
            response = presenter.get_create_observation_response()
        except InvalidCategoryId:
            response = presenter.raise_invalid_category_id_exception()
        except InvalidSubCategoryId:
            response = presenter.raise_invalid_subcategory_id_for_category_exception()
        return response

    def create_observation(self, observation_dto: ObservationDTO):

        if observation_dto.category_id:
            self.storage.validate_category_id(observation_dto.category_id)
        if observation_dto.subcategory_id:
            self.storage.validate_subcategory_id(observation_dto.category_id,
                                             observation_dto.subcategory_id)
        self.storage.create_observation(observation_dto)
