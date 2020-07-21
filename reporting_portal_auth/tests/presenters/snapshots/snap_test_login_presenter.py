# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestLoginPresenter.test_invalid_username_raise_exception response'] = {
    'res_status': 'INVALID_USERNAME',
    'response': 'username is invalid, try to give valid username'
}

snapshots['TestLoginPresenter.test_invalid_password_raise_exception response'] = {
    'res_status': 'INVALID_PASSWORD',
    'response': 'password is invalid, try to give valid password'
}

snapshots['TestLoginPresenter.test_get_user_token_response response'] = {
    'access_token': 'XpCbV4bTl6v43HTsexE1SUxoNiO7qG',
    'refresh_token': 'amNMDAKB1hMgMpHzjxr6rzHTz59SJo',
    'role': 'USER'
}
