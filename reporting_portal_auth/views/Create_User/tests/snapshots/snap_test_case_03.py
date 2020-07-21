# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02CreateUserAPITestCase::test_case status'] = 200

snapshots['TestCase02CreateUserAPITestCase::test_case body'] = {
    'res_status': 'INVALID_PASSWORD',
    'response': 'password is invalid, try to give valid password'
}

snapshots['TestCase02CreateUserAPITestCase::test_case header_params'] = {
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
        '97'
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
