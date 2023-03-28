# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/27 17:10
# @Author  : qiao
# @File    : test_sup_add.py
from time import sleep
import pytest
from common import pconst
from common.util_json import readJson
from pages.login.p_login import Plogin
from pages.sup.p_sup_add import SupAdd

conf = readJson("datas/sup/data_login.json")


class TestSupAdd():
    def setup_class(self):
        self.plogin: Plogin = Plogin()
        self.pcompAdd: SupAdd = SupAdd()
        self.plogin.open_url(pconst.const_url)
        self.plogin.input_user_pass(conf['user_name'], conf['password'], conf['code'])
        self.plogin.button_login()
        sleep(3)

    def teardown_class(self):
        # 这里作数据清理动作
        self.pcompAdd.driver.quit()

    # 数据驱动新增用例
    @pytest.mark.parametrize('param', readJson(pconst.const_json_sup_add))
    def test_01_comp_add(self, param):
        sleep(1)
        self.pcompAdd.click_new()
        sleep(1)
        self.pcompAdd.input_form_text(param['name'], param['code'], param['contacts'], param['phone'])
        sleep(1)
        self.pcompAdd.click_submit()
        success_text = self.pcompAdd.get_success_text()
        assert success_text is not None


if __name__ == "__main__":
    pytest.main(["-vs", __file__])
