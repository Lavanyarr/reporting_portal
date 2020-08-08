# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetMyObservationsInput.test_get_my_observations_when_invalid_limit_is_given Invalid_limit_response'] = b'{"response": "Given limit is invalid try to give valid limit", "https_status_code": 404, "res_status": "INVALID_LIMIT"}'

snapshots['TestGetMyObservationsInput.test_get_my_observations_when_invalid_offset_is_given Invalid_offset_response'] = b'{"response": "Given offset is invalid try to give valid offset", "https_status_code": 404, "res_status": "INVALID_OFFSET"}'

snapshots['TestGetMyObservationsInput.test_get_my_observations_when_invalid_sort_type_is_given Invalid_sort_type_response'] = b'{"response": "Given sort type is invalid try to give valid sort_type", "https_status_code": 404, "res_status": "INVALID_SORT_TYPE"}'

snapshots['TestGetMyObservationsInput.test_get_my_observations_when_invalid_filter_type_is_given Invalid_filter_type_response'] = b'{"response": "Given filter type is invalid try to give valid filter_type", "https_status_code": 404, "res_status": "INVALID_FILTER_TYPE"}'

snapshots['TestGetMyObservationsInput.test_get_my_observations_when_invalid_sort_field_is_given Invalid_sort_field_response'] = b'{"response": "Given sort_field is invalid try to give valid sort_field", "https_status_code": 404, "res_status": "INVALID_SORT_FIELD"}'
