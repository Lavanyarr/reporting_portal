# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCategoriesWithSubCategoriesPresenter.test_categories_when_there_are_no_categories empty_dict'] = {
    'categories': [
    ]
}

snapshots['TestCategoriesWithSubCategoriesPresenter.test_categories_when_there_are_categories_but_no_subcategories categories_with_empty_sub_categories_dto'] = {
    'categories': [
        {
            'id': 1,
            'name': 'category_1',
            'subcategories': [
            ]
        }
    ]
}

snapshots['TestCategoriesWithSubCategoriesPresenter.test_categories_when_there_are_categories categories_with_sub_categories_dto'] = {
    'categories': [
        {
            'id': 1,
            'name': 'category_1',
            'subcategories': [
                {
                    'id': 1,
                    'name': 'category_1'
                },
                {
                    'id': 2,
                    'name': 'category_2'
                }
            ]
        }
    ]
}
