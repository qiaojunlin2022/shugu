# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/28 9:59
# @Author  : qiao
# @File    : p_sup_zdel.py
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from common.driver import Driver, driver


class SupDel():
    def __init__(self):
        self.driver = Driver()
        self.odriver: WebDriver = self.driver.driver
        # 这里主要是提取分离元素，方便后期维护
        self.locator_shujufuwu = (
            By.CSS_SELECTOR, ".top-bar > li:nth-child(2) > div:nth-child(1) > span:nth-child(2)")
        self.locator_del_but = (By.CSS_SELECTOR,
                                ".ivu-table-fixed-body > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(8) > td:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(5)")
        self.locator_del_but2 = (By.CSS_SELECTOR,
                                 "div.v-transfer-dom:nth-child(13) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > button:nth-child(2) > span:nth-child(1)")
        self.locator_yes_but = (By.CSS_SELECTOR,
                                "div.v-transfer-dom:nth-child(22) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > button:nth-child(2)")
        self.locator_text_success = (
            By.LINK_TEXT, "测试供应商")

    # 封装基础动作-打开页面
    def open_url(self, url):
        self.driver.open(url)

    # 封装基础动作-删除数据
    def click_del(self):
        self.driver.click(self.locator_shujufuwu)
        sleep(3)
        self.driver.click(self.locator_del_but)
        sleep(1)
        self.driver.click(self.locator_yes_but)
        sleep(1)
        # alert = driver.switch_to.alert
        # text = alert.text
        # print("对话框展示:", text)
        # alert.accept()

    # 断言删除数据是否存在
    def get_success_text(self):
        return self.driver.find_element(self.locator_text_success)
