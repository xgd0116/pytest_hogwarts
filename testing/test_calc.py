# -*- coding:utf8 -*-
import sys
sys.path.append('..')
import pytest
from pythoncode import calc


class TestCalc(object):

    def setup_class(self):
        self.ca = calc.Calculator()
        print('setup class>>>>>>>>>>>>>>>>>>>>')

    @pytest.mark.add
    def test_add(self):
        assert 2 == self.ca.add(1, 1)

    @pytest.mark.div
    def test_div(self):
        assert 2 == self.ca.div(2, 1)