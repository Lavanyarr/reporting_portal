import factory

from reporting_portal_auth.models import User
from reporting_portal_auth.constants.enums import Role

role = Role.get_list_of_tuples()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.sequence(lambda x: "user_{0}".format(x + 1))
    phone_no = factory.sequence(lambda x: x + 1)
    user_role = factory.Iterator(role, getter=lambda c: c[0])
    profile_pic = factory.sequence(lambda x: "pic_{0}".format(x + 1))
    username = factory.sequence(lambda x: "username_{0}".format(x+1))
    password = factory.PostGenerationMethodCall('set_password')
