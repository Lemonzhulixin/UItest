# -*- coding: utf-8 -*-
"""添加字幕的基本操作测试用例."""
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS.Base import base as ba, script_ultils as sc, iOS_elements
from selenium.common.exceptions import TimeoutException
import random


class TestEditText(TestCase):
    """添加字幕的基本操作测试类."""

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

    def test_edit_text_01(self):
        """剪辑-字幕-进入字幕."""
        sc.logger.info('剪辑-进入字幕')
        fun_name = 'test_edit_text'

        sc.logger.info('点击视频剪辑')
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_home_edit)).click()

        sc.logger.info('添加视频')
        ba.gallery_clip_add('视频', 2)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击下一步')
        ba.find_element_click('predicate', 10, iOS_elements.el_gallery_next)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“素材·效果”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("素材·效果")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“字幕”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("字幕")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('剪辑-进入字幕测试完成')

    def test_edit_text_02(self):
        """剪辑-动态字幕添加."""
        sc.logger.info('剪辑-动态字幕添加')
        fun_name = 'test_edit_text_add'

        sc.logger.info('添加动态字幕')
        for i in range(2):
            ba.loop_add_text()
            time.sleep(1)
            sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('剪辑-动态字幕添加测试完成')

    def test_edit_text_03(self):
        """剪辑-普通字幕添加."""
        sc.logger.info('剪辑-普通字幕添加')
        fun_name = 'test_edit_text_comm'

        sc.logger.info('添加普通字幕')
        for i in range(2):
            ba.loop_add_comm_text()
            time.sleep(1)
            sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('剪辑-普通字幕添加测试完成')

    def test_edit_text_04(self):
        """剪辑-字幕-其他设置."""
        sc.logger.info('剪辑-字幕-其他设置')
        fun_name = 'test_edit_text_set'

        sc.logger.info('切换到字体')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.btn_text_font)).click()

        sc.logger.info('点击"下载"按钮')
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_xpath(iOS_elements.btn_font_download)).click()
        except TimeoutException:
            sc.logger.info('当前页面已无为下载字体')

        sc.logger.info('切换到字体设置页面')
        sc.driver.find_element_by_name(iOS_elements.btn_text_set).click()

        sc.logger.info('随机对齐方式')
        el_align = [iOS_elements.btn_text_c, iOS_elements.btn_text_l, iOS_elements.btn_text_r]
        sc.driver.find_element_by_name(random.choice(el_align)).click()

        sc.logger.info('点击阴影开关')
        sc.driver.find_element_by_xpath("//*/XCUIElementTypeSwitch[1]").click()

        sc.logger.info('点击字幕动画开关')
        sc.driver.find_element_by_xpath("//*/XCUIElementTypeSwitch[2]").click()

        sc.logger.info('确认添加')
        ba.effect_add_confirm()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.logger.info('剪辑-字幕-其他设置测试完成')