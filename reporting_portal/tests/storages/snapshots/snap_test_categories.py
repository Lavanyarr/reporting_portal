# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetCategories.test_get_categories_when_there_are_no_categories category_dto'] = [
]

snapshots['TestGetCategories.test_get_categories_when_there_are_categories category_dto'] = [
    GenericRepr("CategoryDTO(id=1, name='category_1')"),
    GenericRepr("CategoryDTO(id=2, name='category_2')"),
    GenericRepr("CategoryDTO(id=3, name='category_3')")
]
