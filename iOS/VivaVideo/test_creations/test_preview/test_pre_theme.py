# -*- coding: utf-8 -*-
"""预览页面的theme测试用例."""
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from iOS.Base import base as ba, script_ultils as sc, iOS_elements


class TestPreviewTheme(TestCase):
    """预览页面的theme测试类."""

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

    def test_preview_theme(self):
        """预览页-主题·配乐页面."""
        sc.logger.info('预览页-主题·配乐页面')
        fun_name = 'test_preview_theme'

        sc.logger.info('点击创作中心主按钮')
        ba.home_enter()

        sc.logger.info('点击“视频剪辑”按钮')
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_xpath(iOS_elements.el_home_edit)).click()
        except TimeoutException:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_xpath(iOS_elements.home_edit)).click()

        sc.logger.info('添加视频')
        ba.gallery_clip_add('视频', 1)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('切换到图片')
        sc.driver.find_element_by_name("视频").click()
        sc.driver.find_element_by_name("图片").click()

        sc.logger.info('添加图片')
        ba.gallery_clip_add('图片', 2)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击下一步')
        ba.find_element_click('predicate', 10, iOS_elements.el_gallery_next)

        sc.logger.info('点击“主题·配乐”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("主题·配乐")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('暂停播放')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.btn_stop)).click()

        sc.logger.info('使用“主题”')
        try:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_xpath(iOS_elements.el_theme_use)).click()
        except TimeoutException:
            sc.logger.info('当前页面无已下载的主题')
            WebDriverWait(sc.driver, 10, 1).until(
                lambda x: x.find_element_by_xpath(iOS_elements.el_theme_download)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下载更多')
        sc.driver.find_element_by_name('下载更多').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下拉刷新')
        ba.refresh('down', 0.3, 500, 1)
        time.sleep(3)

        sc.logger.info('下载并使用主题')
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name("使用")).click()
        except TimeoutException:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name(iOS_elements.el_store_download1)).click()

            sc.logger.info('使用主题')
            WebDriverWait(sc.driver, 10, 1).until(
                lambda x: x.find_element_by_name("使用")).click()
            sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('暂停播放')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.btn_stop)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()

        sc.logger.info('预览页-主题·配乐测试完成')