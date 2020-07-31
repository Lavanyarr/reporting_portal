from django.db import models
from reporting_portal.models import (
    Category,
    SubCategory
)
from reporting_portal.constants.enums import (
    Severity,
    Status
)

SEVERITY = Severity.get_list_of_tuples()
STATUS = Status.get_list_of_tuples()


class Observation(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    severity = models.CharField(max_length=20, choices=SEVERITY)
    status = models.CharField(max_length=20, choices=STATUS, default='REPORTED')
    assigned_to = models.IntegerField(null=True)
    reported_on = models.DateTimeField(null=True, auto_now=True)
    due_date = models.DateTimeField(null=True)
    reported_by = models.IntegerField(null=True)
