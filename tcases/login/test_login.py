# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/27 16:21
# @Author  : qiao
# @File    : test_login.py
from time import sleep
import pytest

from common import pconst
from common.util_json import readJson
from pages.login.p_login import Plogin


class TestLogin():
    def setup_method(self):
        self.plogin: Plogin = Plogin()

    def teardown_method(self):
        self.plogin.driver.quit()

    # 数据驱动登陆测试用例
    @pytest.mark.parametrize('param', readJson(pconst.const_json_login))
    def test_01_login(self, param):
        self.plogin.open_url(pconst.const_url)
        sleep(1)
        self.plogin.input_user_pass(param['user_name'], param['password'], param['code'])
        sleep(1)
        self.plogin.button_login()
        sleep(1)
        cpjx = self.plogin.get_cpjx()
        assert cpjx is not None
        sleep(1)


if __name__ == "__main__":
    pytest.main(["-vs", __file__])
