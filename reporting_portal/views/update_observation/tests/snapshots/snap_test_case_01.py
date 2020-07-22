# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UpdateObservationAPITestCase::test_case status'] = 200

snapshots['TestCase01UpdateObservationAPITestCase::test_case body'] = b''

snapshots['TestCase01UpdateObservationAPITestCase::test_case header_params'] = {
    'allow': (
        'Allow',
        'OPTIONS, PUT'
    ),
    'content-language': (
        'Content-Language',
        'en'
    ),
    'content-length': (
        'Content-Length',
        '0'
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
