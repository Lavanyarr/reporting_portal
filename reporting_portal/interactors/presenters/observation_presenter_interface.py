import abc


class ObservationPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_create_observation_response(self):
        pass

    @abc.abstractmethod
    def raise_invalid_category_id_exception(self):
        pass

    @abc.abstractmethod
    def raise_invalid_subcategory_id_for_category_exception(self):
        pass
