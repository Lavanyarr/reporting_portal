# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestObservation.test_get_observations_when_sort_field_is_due_date observation_objs'] = GenericRepr("<QuerySet [<Observation: Observation object (2)>, <Observation: Observation object (3)>, <Observation: Observation object (4)>]>")
