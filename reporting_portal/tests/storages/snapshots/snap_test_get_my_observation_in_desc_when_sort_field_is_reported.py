# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestObservation.test_get_observations_in_desc_when_sort_field_is_reported_by observation_objs'] = GenericRepr("<QuerySet [<Observation: Observation object (4)>, <Observation: Observation object (3)>, <Observation: Observation object (2)>]>")
