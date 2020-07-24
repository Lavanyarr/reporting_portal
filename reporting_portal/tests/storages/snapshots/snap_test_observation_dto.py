# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetValidObservationIds.test_when_valid_observation_ids_are_given response'] = [
    GenericRepr("ObservationDetailsDTO(title='title_1', severity='LOW', status='CLOSED', due_date=datetime.datetime(2020, 7, 24, 20, 52, 11, 284781), messages_count=0)"),
    GenericRepr("ObservationDetailsDTO(title='title_2', severity='WARNING', status='REPORTED', due_date=datetime.datetime(2020, 7, 24, 20, 52, 11, 285594), messages_count=0)")
]
