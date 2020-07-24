# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetMyObservationsAPITestCase.test_case status_code'] = '400'

snapshots['TestCase01GetMyObservationsAPITestCase.test_case body'] = {
    'filter_type': [
        'This field is required.'
    ],
    'sort_field': [
        'This field is required.'
    ],
    'sort_type': [
        'This field is required.'
    ]
}
