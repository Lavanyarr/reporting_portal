# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetCategoriesWithSubcategoriesAPITestCase::test_case status'] = 200

snapshots['TestCase01GetCategoriesWithSubcategoriesAPITestCase::test_case body'] = {
    'categories': [
        {
            'id': 1,
            'name': 'category_1',
            'subcategories': [
            ]
        },
        {
            'id': 2,
            'name': 'category_2',
            'subcategories': [
            ]
        }
    ]
}

snapshots['TestCase01GetCategoriesWithSubcategoriesAPITestCase::test_case header_params'] = {
    'allow': (
        'Allow',
        'GET, OPTIONS'
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
