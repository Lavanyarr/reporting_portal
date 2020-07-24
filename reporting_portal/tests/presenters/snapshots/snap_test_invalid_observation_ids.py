# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestInvalidObservationIds.test_get_observations_with_invalid_observation_ids Invalid_observation_ids'] = b'{"response": "observation_ids are invalid try to give valid observation ids", "https_status_code": 404, "res_status": "INVALID_OBSERVATION_IDS"}'
