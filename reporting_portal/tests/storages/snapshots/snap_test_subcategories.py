# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetCategories.test_subcategories_when_category_as_no_subcategories subcategory_dto'] = [
]

snapshots['TestGetCategories.test_subcategories_when_category_have_subcategories subcategory_dto'] = [
    GenericRepr("SubCategoryDTO(category_id=1, id=1, name='sub_category_1')"),
    GenericRepr("SubCategoryDTO(category_id=1, id=2, name='sub_category_2')")
]
