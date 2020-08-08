# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestMyObservations.test_get_observations_list_response Invalid_sort_field_response'] = b'{"total_observations_count": 1, "observation_details": [{"observation_id": 1, "title": "title_1", "reported_on": "15/5/2020 at 5: 30 pm", "severity": "HIGH", "status": "ALL", "due_date": "17/5/2020 at 5: 30 pm", "messages_count": 1, "show_due_date": true, "assigned_to": {"user_id": 1, "name": "name_1", "profile_pic": "profile_pic_1", "phone_no": "99999999_1"}}, {"observation_id": 2, "title": "title_2", "reported_on": "15/5/2020 at 5: 30 pm", "severity": "LOW", "status": "ACTION_IN_PROGRESS", "due_date": "17/5/2020 at 5: 30 pm", "messages_count": 2, "show_due_date": true, "assigned_to": null}]}'
