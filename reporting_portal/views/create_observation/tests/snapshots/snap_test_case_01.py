# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateObservationAPITestCase::test_case status'] = 404

snapshots['TestCase01CreateObservationAPITestCase::test_case body'] = {
    'https_status_code': 404,
    'res_status': 'INVALID_CATEGORY_ID',
    'response': 'category_id is invalid try to give valid category_id'
}

snapshots['TestCase01CreateObservationAPITestCase::test_case header_params'] = {
    'allow': (
        'Allow',
        'OPTIONS, POST'
    ),
    'content-language': (
        'Content-Language',
        'en'
    ),
    'content-length': (
        'Content-Length',
        '131'
    ),
    'content-type': (
        'Content-Type',
        'text/html; charset=utf-8'
    ),
    'vary': (
        'Vary',
        'Accept-Language, Origin, Cookie'
    ),
    'x-frame-options': (
        'X-Frame-Options',
        'SAMEORIGIN'
    )
}
