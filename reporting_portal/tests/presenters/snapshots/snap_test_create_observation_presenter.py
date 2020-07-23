# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCreateObservation.test_invalid_category_id_for_observation invalid_category_id'] = {
    'https_status_code': 404,
    'res_status': 'INVALID_CATEGORY_ID',
    'response': 'category_id is invalid try to give valid category_id'
}

snapshots['TestCreateObservation.test_invalid_sub_category_id_for_observation invalid_category_id'] = {
    'https_status_code': 404,
    'res_status': 'INVALID_SUBCATEGORY_ID',
    'response': 'subcategory_id is invalid try to give valid subcategory_id for given category_id'
}

snapshots['TestCreateObservation.test_create_observation_with_valid_details invalid_category_id'] = 'observation_created'
