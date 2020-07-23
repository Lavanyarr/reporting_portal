# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02CreateObservationAPITestCase::test_case status'] = 404

snapshots['TestCase02CreateObservationAPITestCase::test_case body'] = {
    'https_status_code': 404,
    'res_status': 'INVALID_SUBCATEGORY_ID',
    'response': 'subcategory_id is invalid try to give valid subcategory_id for given category_id'
}

snapshots['TestCase02CreateObservationAPITestCase::test_case header_params'] = {
    'allow': (
        'Allow',
        'POST, OPTIONS'
    ),
    'content-language': (
        'Content-Language',
        'en'
    ),
    'content-length': (
        'Content-Length',
        '162'
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
