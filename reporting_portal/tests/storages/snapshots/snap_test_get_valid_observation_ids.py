# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetValidObservationIds.test_when_invalid_observation_ids_are_given response'] = GenericRepr("<QuerySet [2]>")

snapshots['TestGetValidObservationIds.test_when_valid_observation_ids_are_given valid_observation_ids'] = GenericRepr("<QuerySet [1, 2]>")
