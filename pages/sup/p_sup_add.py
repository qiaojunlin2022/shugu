# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/27 16:44
# @Author  : qiao
# @File    : p_sup_add.py
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from common.driver import Driver
from common.util_json import readJson


class SupAdd():
    def __init__(self):
        self.driver = Driver()
        self.odriver: WebDriver = self.driver.driver
        # 这里主要是提取分离元素，方便后期维护
        self.locator_shujufuwu = (
            By.CSS_SELECTOR, ".top-bar > li:nth-child(2) > div:nth-child(1) > span:nth-child(2)")
        self.locator_add_but = (
            By.CSS_SELECTOR, "button.ivu-btn-primary:nth-child(1)")
        self.locator_new_name = (
            By.CSS_SELECTOR,
            "div.ivu-col:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > input:nth-child(2)")
        self.locator_trust_code = (
            By.CSS_SELECTOR,
            "div.ivu-form-item-required:nth-child(4) > div:nth-child(2) > div:nth-child(1) > input:nth-child(2)")
        self.locator_new_contacts = (
            By.CSS_SELECTOR,
            "div.ivu-col:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > input:nth-child(2)")
        self.locator_new_phone = (
            By.XPATH,
            "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/form/div/div[3]/div[2]/div/div[1]/input")
        self.locator_submit = (
            By.CSS_SELECTOR, "button.btn:nth-child(2)")
        self.locator_cpjx = (
            By.CSS_SELECTOR,
            ".ivu-table-body > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(8) > td:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)")
        self.locator_text_success = (
            By.LINK_TEXT, "测试供应商")

    # 封装基础动作-打开页面
    def open_url(self, url):
        self.driver.open(url)

    # 封装基础动作-新增数据
    def click_new(self):
        self.driver.click(self.locator_shujufuwu)
        self.driver.click(self.locator_add_but)

    # 封装基础动作-输入名称、编码、描述
    def input_form_text(self, name, code, contacts, phone):
        self.driver.send_keys(self.locator_new_name, name)
        self.driver.send_keys(self.locator_trust_code, code)
        self.driver.send_keys(self.locator_new_contacts, contacts)
        self.driver.send_keys(self.locator_new_phone, phone)
        sleep(1)

    # 封装基础动作-提交新增组件
    def click_submit(self):
        self.driver.click(self.locator_submit)

    # 获取业务数据-成功文字提示-用来判断是否成功
    def get_success_text(self):
        return self.driver.find_element(self.locator_text_success)
        # ele = self.driver.find_element(self.locator_text_success)
        # if ele is not None:
        #     return ele.text
        # else:
        #     return None
