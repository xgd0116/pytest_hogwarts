# -*- coding:utf8 -*-
import pytest


@pytest.mark.parametrize('a',[1,2])
@pytest.mark.parametrize('b',[3,4])
def test_demo_01(a, b):
    print(a + b)
