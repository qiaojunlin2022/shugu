# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/28 15:20
# @Author  : qiao
# @File    : test_sup_edit.py
from time import sleep
import pytest
from common import pconst
from common.util_json import readJson
from pages.login.p_login import Plogin
from pages.sup.p_sup_edit import SupEdit

conf = readJson("datas/sup/data_login.json")


class TestSupQuert():
    def setup_class(self):
        self.plogin: Plogin = Plogin()
        self.pcompEdit: SupEdit = SupEdit()
        self.plogin.open_url(pconst.const_url)
        self.plogin.input_user_pass(conf['user_name'], conf['password'], conf['code'])
        self.plogin.button_login()
        sleep(3)

    def teardown_class(self):
        # 这里作数据清理动作
        self.pcompEdit.driver.quit()

    # 数据驱动新增组件用例
    @pytest.mark.parametrize('param', readJson(pconst.const_json_sup_add))
    def test_01_comp_edit(self, param):
        self.pcompEdit.clicl_edit(param["name"])
        success_text = self.pcompEdit.get_success_text()
        assert success_text is not None


if __name__ == "__main__":
    pytest.main(["-vs", __file__])
