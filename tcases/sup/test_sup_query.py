# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/28 13:51
# @Author  : qiao
# @File    : test_sup_query.py
from time import sleep
import pytest
from common import pconst
from common.util_json import readJson
from pages.login.p_login import Plogin
from pages.sup.p_sup_query import SupQuery

conf = readJson("datas/sup/data_login.json")


class TestSupQuery():
    def setup_class(self):
        self.plogin: Plogin = Plogin()
        self.pcompQuery: SupQuery = SupQuery()
        self.plogin.open_url(pconst.const_url)
        self.plogin.input_user_pass(conf['user_name'], conf['password'], conf['code'])
        self.plogin.button_login()
        sleep(3)

    def teardown_class(self):
        # 这里作数据清理动作
        self.pcompQuery.driver.quit()

    # 供应商管理条件查询
    @pytest.mark.parametrize('param', readJson(pconst.const_json_sup_add))
    def test_01_comp_query(self, param):
        self.pcompQuery.query_sup(param["name"])
        success_text = self.pcompQuery.get_success_text()
        assert success_text is not None

    # 供应商详情查询
    def test_02_comp_query(self):
        self.pcompQuery.query_sup_02()
        success_name = self.pcompQuery.get_success_sup_name()
        assert success_name is not None


if __name__ == "__main__":
    pytest.main(["-vs", "./tcases/test_sup_add.py", '--clean-alluredir', '--alluredir=reports/allurefile'])
