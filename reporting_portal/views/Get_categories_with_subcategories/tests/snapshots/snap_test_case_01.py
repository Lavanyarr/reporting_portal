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
                {
                    'id': 1,
                    'name': 'sub_category_1'
                },
                {
                    'id': 2,
                    'name': 'sub_category_2'
                }
            ]
        },
        {
            'id': 2,
            'name': 'category_2',
            'subcategories': [
            ]
        },
        {
            'id': 3,
            'name': 'category_3',
            'subcategories': [
            ]
        },
        {
            'id': 4,
            'name': 'category_4',
            'subcategories': [
            ]
        }
    ]
}

snapshots['TestCase01GetCategoriesWithSubcategoriesAPITestCase::test_case header_params'] = {
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
        '304'
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
