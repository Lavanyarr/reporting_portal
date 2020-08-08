import datetime

import factory

from reporting_portal.interactors.storages.dtos import (
    CategoryDTO,
    SubCategoryDTO,
    ObservationDTO,
    ObservationDetailsDTO, UserDTO, ObservationDetailsWithCount
)
from reporting_portal.constants.enums import (
    Severity,
    Status
)


class CategoryDTOFactory(factory.Factory):
    class Meta:
        model = CategoryDTO

    id = factory.sequence(lambda x: x + 1)
    name = factory.sequence(lambda x: "category_{0}".format(x + 1))


class SubCategoryDTOFactory(factory.Factory):
    class Meta:
        model = SubCategoryDTO

    category_id = factory.sequence(lambda x: x + 1)
    id = factory.sequence(lambda x: x + 1)
    name = factory.sequence(lambda x: "category_{0}".format(x + 1))


SEVERITY = Severity.get_list_of_tuples()
STATUS = Status.get_list_of_tuples()


class ObservationFactory(factory.Factory):
    class Meta:
        model = ObservationDTO

    title = factory.sequence(lambda x: "title_{0}".format(x + 1))
    category_id = factory.sequence(lambda x: x + 1)
    subcategory_id = factory.sequence(lambda x: x + 1)
    severity = factory.Iterator(SEVERITY, getter=lambda c: c[0])
    description = factory.sequence(lambda x: "description_{0}".format(x + 1))
    attachments = factory.sequence(lambda x: "attachment_{0}".format(x + 1))


class ObservationDetailsFactory(factory.Factory):
    class Meta:
        model = ObservationDetailsDTO

    id = factory.sequence(lambda x: x + 1)
    title = factory.sequence(lambda x: "title_{0}".format(x + 1))
    severity = factory.Iterator(SEVERITY, getter=lambda c: c[0])
    status = factory.Iterator(STATUS, getter=lambda c: c[0])
    due_date = "17/5/2020 at 5: 30 pm"
    messages_count = factory.sequence(lambda x: x + 1)
    #reported_on = datetime.datetime.now()
    reported_on = "15/5/2020 at 5: 30 pm"
    assigned_to = factory.sequence(lambda x: x + 1)
    is_public = True


class UserDtoFactory(factory.Factory):
    class Meta:
        model = UserDTO

    user_id = factory.sequence(lambda x: x + 1)
    name = factory.sequence(lambda x: "name_{0}".format(x + 1))
    profile_pic = factory.sequence(lambda x: "profile_pic_{0}".format(x + 1))
    phone_no = factory.sequence(lambda x: "99999999_{0}".format(x + 1))

class ObservationDetailsWithCountFactory(factory.Factory):

    class Meta:
        model = ObservationDetailsWithCount

    total_count = factory.sequence(lambda x: x+1)
    observation_details = ObservationDetailsFactory.create_batch(2)

