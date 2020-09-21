# -*- coding:utf8 -*-
import pytest

def test_fixture1(login):
    print('test fixture 1 ----------')
    print(f'{login}')

    assert True


def test_fixture2():
    print('test fixture 2 ----------')
    assert True