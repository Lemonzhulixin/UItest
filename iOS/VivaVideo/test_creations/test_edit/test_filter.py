# -*- coding: utf-8 -*-
"""编辑滤镜的基本操作测试用例."""
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS.Base import base as ba, script_ultils as sc, iOS_elements
from selenium.common.exceptions import NoSuchElementException


class TestEditFilter(TestCase):
    """编辑滤镜的基本操作测试类."""

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

    def test_edit_filter(self):
        """剪辑-滤镜下载/使用."""
        sc.logger.info('剪辑-滤镜下载/使用')
        fun_name = 'test_edit_filter'

        start_x = self.width // 2
        start_y = self.height // 8
        start_bottom = self.height - start_y

        sc.logger.info('打开一个草稿视频')
        ba.home_first_click('更多草稿')

        sc.logger.info('点击草稿封面')
        ba.open_draft(iOS_elements.el_studio_draft)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“镜头编辑”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("镜头编辑")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"滤镜"')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("滤镜")).click()

        sc.logger.info('下载更多')
        try:
            sc.driver.find_element_by_name('下载更多').click()
        except NoSuchElementException:
            sc.logger.info('右滑一些，再选择下载更多')
            el_fliter = sc.driver.find_element_by_name("缓流")
            coord_x = el_fliter.location.get('x')
            coord_y = el_fliter.location.get('y')
            sc.swipe_by_ratio(coord_x, coord_y, 'right', 0.5, 500)

            sc.driver.find_element_by_name('下载更多').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下拉刷新')
        ba.refresh('down', 0.3, 500, 1)

        sc.logger.info('下载并使用滤镜')
        while True:
            try:
                sc.driver.find_element_by_name(iOS_elements.el_store_download2).click()
                break
            except NoSuchElementException:
                sc.logger.info('当前页面已无未下载主题')
                sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 300)

        sc.logger.info('使用滤镜')
        WebDriverWait(sc.driver, 20, 1).until(
            lambda x: x.find_element_by_name("使用")).click()

        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("应用于全部镜头")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“确认”')
        sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()

        sc.logger.info('剪辑-滤镜下载/使用测试完成')