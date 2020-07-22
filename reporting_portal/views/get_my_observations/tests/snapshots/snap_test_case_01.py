# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetMyObservationsAPITestCase::test_case status'] = 400

snapshots['TestCase01GetMyObservationsAPITestCase::test_case body'] = {
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

snapshots['TestCase01GetMyObservationsAPITestCase::test_case header_params'] = {
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
        '124'
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
