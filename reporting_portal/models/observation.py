

from django.db import models
from reporting_portal.models import (
    Category,
    SubCategory
)
from reporting_portal.constants.enums import SEVERITY

severity = SEVERITY.get_list_of_tuples()


class Observation(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    severity = models.CharField(max_length=20, choices=severity)
