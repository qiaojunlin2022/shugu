# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/28 9:58
# @Author  : qiao
# @File    : test_sup_zdel.py
from time import sleep
import pytest
from common import pconst
from common.util_json import readJson
from pages.login.p_login import Plogin
from pages.sup.p_sup_zdel import SupDel

conf = readJson("datas/sup/data_login.json")


class TestSupDel():
    def setup_class(self):
        self.plogin: Plogin = Plogin()
        self.pcompDel: SupDel = SupDel()
        self.plogin.open_url(pconst.const_url)
        self.plogin.input_user_pass(conf['user_name'], conf['password'], conf['code'])
        self.plogin.button_login()
        sleep(3)

    def teardown_class(self):
        # 这里作数据清理动作
        self.pcompDel.driver.quit()

    def test_01_comp_del(self):
        self.pcompDel.click_del()
        success_text = self.pcompDel.get_success_text()
        assert success_text is None


if __name__ == "__main__":
    pytest.main(["-vs", __file__])