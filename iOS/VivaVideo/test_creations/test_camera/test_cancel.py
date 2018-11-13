# -*- coding: utf-8 -*-
"""camera取消操作相关的测试用例."""
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS.Base import base as ba, script_ultils as sc, iOS_elements
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.touch_action import TouchAction


class TestCameraCancel(TestCase):
    """camera取消操作相关的测试类."""

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

    def test_cancel_01_shot(self):
        """拍摄-拍摄页放弃."""
        sc.logger.info('拍摄-拍摄页放弃')
        fun_name = 'test_cancel_shot'

        sc.logger.info('点击创作中心主按钮')
        ba.home_enter()

        sc.logger.info('点击“美颜趣拍”')
        WebDriverWait(sc.driver, 5).until(
            lambda x: x.find_element_by_name('美颜趣拍')).click()

        sc.logger.info('切换拍摄模式:自拍美颜->高清相机')
        el_normal = "高清相机"
        ba.find_element_click('name', 5, el_normal)
        sc.capture_screen(fun_name, self.img_path)

        # 点拍
        sc.logger.info('开始录制')
        el_capture = WebDriverWait(sc.driver, 10).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_cp_normal))
        el_capture.click()
        sc.capture_screen(fun_name, self.img_path)
        time.sleep(5)

        sc.logger.info('录制5s后点击录制按钮停止录制')
        el_capture.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击左上角取消按钮')
        ba.find_element_click('name', 5, iOS_elements.el_cam_close)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“丢弃”按钮')
        ba.find_element_click('name', 5, iOS_elements.el_discard)
        sc.logger.info('拍摄-拍摄页放弃测试完成')

    def test_cancel_02_save(self):
        """拍摄-拍摄页保存."""
        sc.logger.info('拍摄-拍摄页保存')
        fun_name = 'test_cancel_save'

        sc.logger.info('点击“美颜趣拍”')
        WebDriverWait(sc.driver, 5).until(
            lambda x: x.find_element_by_name('美颜趣拍')).click()

        sc.logger.info('切换拍摄模式:自拍美颜->高清相机')
        el_normal = "高清相机"
        ba.find_element_click('name', 5, el_normal)
        sc.capture_screen(fun_name, self.img_path)

        # 点拍
        sc.logger.info('录制两段5s的视频')
        el_capture = WebDriverWait(sc.driver, 10).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_cp_normal))
        for i in range(2):
            el_capture.click()
            sc.capture_screen(fun_name, self.img_path)
            time.sleep(5)
            el_capture.click()
            time.sleep(1)

        sc.logger.info('撤销第二段视频')
        for i in range(2):
            sc.driver.find_element_by_name("撤销").click()
            sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击左上角取消按钮')
        ba.find_element_click('name', 5, iOS_elements.el_cam_close)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“保存”按钮')
        ba.find_element_click('name', 5, iOS_elements.el_save)
        sc.logger.info('拍摄-拍摄页保存测试完成')
