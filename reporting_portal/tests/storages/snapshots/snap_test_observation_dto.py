# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetValidObservationIds.test_when_valid_observation_ids_are_given response'] = GenericRepr("ObservationDetailsWithCount(total_count=2, observation_details=[ObservationDetailsDTO(id=1, title='title_1', severity='WARNING', status='RESOLVED', due_date=FakeDatetime(2020, 7, 31, 16, 5, 54, 365804), messages_count=0, reported_on=FakeDatetime(2012, 1, 14, 0, 0), assigned_to=1, is_public=True), ObservationDetailsDTO(id=2, title='title_2', severity='WARNING', status='RESOLVED', due_date=FakeDatetime(2020, 7, 31, 16, 5, 54, 365804), messages_count=0, reported_on=FakeDatetime(2012, 1, 14, 0, 0), assigned_to=2, is_public=True)])")
