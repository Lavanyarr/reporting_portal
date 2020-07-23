# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateUserAPITestCase::test_case status'] = 201

snapshots['TestCase01CreateUserAPITestCase::test_case body'] = {
    'access_token': 'XpCbV4bTl6v43HTsexE1SUxoNiO7qG',
    'refresh_token': 'amNMDAKB1hMgMpHzjxr6rzHTz59SJo',
    'role': 'USER'
}

snapshots['TestCase01CreateUserAPITestCase::test_case header_params'] = {
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
        '117'
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
