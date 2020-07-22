# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetObservationsDetailsAPITestCase::test_case status'] = 400

snapshots['TestCase01GetObservationsDetailsAPITestCase::test_case body'] = {
    'observation_id': [
        'This field is required.'
    ]
}

snapshots['TestCase01GetObservationsDetailsAPITestCase::test_case header_params'] = {
    'allow': (
        'Allow',
        'OPTIONS, GET'
    ),
    'content-language': (
        'Content-Language',
        'en'
    ),
    'content-length': (
        'Content-Length',
        '46'
    ),
    'content-type': (
        'Content-Type',
        'application/json'
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
