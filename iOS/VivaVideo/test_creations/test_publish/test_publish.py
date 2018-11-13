# -*- coding: utf-8 -*-
"""创作页面内分享相关的测试用例."""
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS.Base import base as ba, script_ultils as sc, iOS_elements
from selenium.common.exceptions import TimeoutException,NoSuchElementException


class TestCreationShare(TestCase):
    """创作页面内分享相关的测试类."""

    # 获取屏幕尺寸
    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    @classmethod
    def setUpClass(cls):
        sc.driver.launch_app()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        sc.driver.close_app()

    def test_share_01(self):
        """分享-标题&描述."""
        sc.logger.info('分享-标题&描述.')
        fun_name = 'test_share_title'

        sc.logger.info('点击创作中心主按钮')
        ba.home_enter()

        sc.logger.info('点击第一个草稿封面')
        ba.find_element_click('xpath', 5, iOS_elements.el_home_draft)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('保存/上传')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("保存/上传")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('关闭定位服务')
        try:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_xpath(iOS_elements.el_loc_clo)).click()
            sc.capture_screen(fun_name, self.img_path)
        except TimeoutException:
            sc.logger.info('不是第一次点击保存/上传按钮')

        sc.logger.info('输入标题和描述')
        ba.publish_input()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('导出-标题&描述测试完成')

    def test_share_02(self):
        """分享-封面编辑."""
        sc.logger.info('分享-封面编辑.')
        fun_name = 'test_share_cover'

        sc.logger.info('更换封面')
        ba.publish_cover_add()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('导出-封面编辑测试完成')

    def test_share_03(self):
        """分享-其他设置."""
        sc.logger.info('分享-其他设置.')
        fun_name = 'test_share_other'

        sc.logger.info('点击更多')
        sc.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="更多"]').click()

        sc.logger.info('谁可以看')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('谁可以看')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('仅自己可见')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('仅自己可见')).click()
        sc.capture_screen(fun_name, self.img_path)

        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name("我知道了")).click()
        except TimeoutException:
            sc.logger.info('不是第一次设置，无设置提示')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('是否允许下载')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('是否允许下载')).click()

        sc.logger.info('不允许下载')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('不允许')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回发布页')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.pub_back)).click()

        sc.logger.info('导出-其他设置测试完成')

    def test_share_04(self):
        """分享-发布."""
        sc.logger.info('分享-发布')
        fun_name = 'test_share_publish'

        sc.logger.info('发布')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("发布")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('关闭定位服务')
        try:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_xpath(iOS_elements.el_loc_clo)).click()
            sc.capture_screen(fun_name, self.img_path)
        except TimeoutException:
            sc.logger.info('不是第一次点击发布按钮')

        sc.logger.info('数据网络时，取消上传')
        try:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_xpath('//XCUIElementTypeButton[@name="取消"]')).click()

            sc.logger.error('当前是数据网络，取消上传，请手动执行相关测试')
            return False
        except TimeoutException:
            sc.logger.info('Wi-Fi可用')

        sc.logger.info('发布')
        ba.publish()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('分享-发布测试完成')
