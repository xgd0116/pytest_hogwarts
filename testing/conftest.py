# -*- coding:utf8 -*-
import pytest


# @pytest.fixture(autouse=True, params=['aaa','bbb','ccc'])
@pytest.fixture()
def login():
    print('logging....>>>>>>>>>')
    return "LOGIN"