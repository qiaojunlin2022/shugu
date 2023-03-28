# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/28 13:44
# @Author  : qiao
# @File    : p_sup_query.py
from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from common.driver import Driver


class SupQuery():
    def __init__(self):
        self.driver = Driver()
        self.odriver: WebDriver = self.driver.driver
        # 这里主要是提取分离元素，方便后期维护
        self.locator_shujufuwu = (
            By.CSS_SELECTOR, ".top-bar > li:nth-child(2) > div:nth-child(1) > span:nth-child(2)")
        self.locator_input_sup = (
            By.CSS_SELECTOR, "div.ivu-col:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)")
        self.locator_query_but = (By.CSS_SELECTOR, "div.ivu-col:nth-child(2) > div:nth-child(1) > button:nth-child(2)")
        self.locator_query_but2 = (By.CSS_SELECTOR,
                                   ".ivu-table-fixed-body > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(8) > td:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(3)")
        self.locator_text_success = (By.LINK_TEXT, "测试供应商")
        self.locator_sup_name_success = (By.CSS_SELECTOR, ".name")

    # 封装基础动作-打开页面
    def open_url(self, url):
        self.driver.open(url)

    # 条件查询动作
    def query_sup(self, name):
        self.driver.click(self.locator_shujufuwu)
        self.driver.send_keys(self.locator_input_sup, name)
        self.driver.click(self.locator_query_but)
        sleep(3)

    # 断言查询1数据是否存在
    def get_success_text(self):
        return self.driver.find_element(self.locator_text_success)

    # 详情查询
    def query_sup_02(self):
        self.driver.click(self.locator_shujufuwu)
        self.driver.click(self.locator_query_but2)
        sleep(3)

    # 断言查询2数据是否存在
    def get_success_sup_name(self):
        return self.driver.find_element(self.locator_sup_name_success)
