# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetValidObservationIds.test_when_valid_observation_ids_are_given response'] = [
    GenericRepr("ObservationDetailsDTO(title='title_1', severity='WARNING', status='RESOLVED', due_date=datetime.datetime(2020, 7, 31, 16, 5, 54, 365804), messages_count=0)"),
    GenericRepr("ObservationDetailsDTO(title='title_2', severity='WARNING', status='RESOLVED', due_date=datetime.datetime(2020, 7, 31, 16, 5, 54, 365804), messages_count=0)")
]
