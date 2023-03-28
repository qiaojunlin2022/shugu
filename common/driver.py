# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/27 16:12
# @Author  : qiao
# @File    : driver.py
from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = None


class Driver():
    # 初始化浏览器+打开页面
    def __init__(self, page_url=None):
        global driver
        if driver is None:
            chrome_options = Options()
            chrome_options.add_experimental_option(
                'excludeSwitches', ['enable-logging'])
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            driver = self.driver
            if page_url is not None:
                self.driver.get(page_url)
        else:
            self.driver = driver

    # 打开页面
    def open(self, page_url):
        self.driver.get(page_url)

    # 定位元素
    def find_element(self, locator) -> WebElement:
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        except Exception as msg:
            print("定位元素异常%s" % msg)

    # 定位元素多个
    def find_elements(self, locator) -> List[WebElement]:
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
        except Exception as msg:
            print("定位元素异常%s" % msg)

    # 输入文本信息
    def send_keys(self, locator, value):
        element: WebElement = self.find_element(locator)
        element.send_keys(value)

    # 点击事件
    def click(self, locator):
        element: WebElement = self.find_element(locator)
        element.click()

    # 切换动作
    def switch_to(self, switchType, window_no):
        if switchType == "window":
            windowHandles = self.driver.window_handles
            self.driver.switch_to.window(windowHandles[window_no])
        elif switchType == "frame":
            self.driver.switch_to.frame(window_no)
        elif switchType == "alert":
            self.driver.switch_to.alert
        else:
            print("切换类型不正确！")

    # 退出浏览器
    def quit(self):
        global driver
        driver = None
        self.driver.quit()
