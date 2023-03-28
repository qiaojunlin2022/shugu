# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/28 15:06
# @Author  : qiao
# @File    : p_sup_edit.py
from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from common.driver import Driver


class SupEdit():
    def __init__(self):
        self.driver = Driver()
        self.odriver: WebDriver = self.driver.driver
        # 这里主要是提取分离元素，方便后期维护
        self.locator_shujufuwu = (
            By.CSS_SELECTOR, ".top-bar > li:nth-child(2) > div:nth-child(1) > span:nth-child(2)")
        self.locator_edit_but = (
            By.CSS_SELECTOR,
            ".ivu-table-fixed-body > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(8) > td:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)")
        self.locator_abbreviation_name = (
            By.CSS_SELECTOR,
            "div.ivu-col:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > input:nth-child(2)")
        self.locator_save_but = (By.CSS_SELECTOR, "button.btn:nth-child(2)")
        self.locator_text_success = (By.CSS_SELECTOR,
                                     ".ivu-table-body > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(8) > td:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)")

    # 封装基础动作-打开页面
    def open_url(self, url):
        self.driver.open(url)

    # 编辑供应商简称
    def clicl_edit(self, name):
        sleep(2)
        self.driver.click(self.locator_shujufuwu)
        self.driver.click(self.locator_edit_but)
        sleep(3)
        self.driver.send_keys(self.locator_abbreviation_name, name)
        sleep(3)
        self.driver.click(self.locator_save_but)

    # 获取业务数据-成功文字提示-用来判断是否成功
    def get_success_text(self):
        return self.driver.find_element(self.locator_text_success)
