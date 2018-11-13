# -*- coding: utf-8 -*-
"""Gallery页面的测试用例."""
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS.Base import base as ba, script_ultils as sc, iOS_elements
from selenium.common.exceptions import TimeoutException


class TestGallery(TestCase):
    """Gallery的测试类."""

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

    def test_gallery_01(self):
        """相册-视频相关操作."""
        sc.logger.info('相册-视频相关操作')
        fun_name = 'test_gallery_video'

        sc.logger.info('点击创作中心主按钮')
        ba.home_enter()

        sc.logger.info('点击“视频剪辑”按钮')
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_xpath(iOS_elements.el_home_edit)).click()
        except TimeoutException:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_xpath(iOS_elements.home_edit)).click()

        sc.logger.info('选择一个视频并进行相关操作')
        ba.gallery_clip_op()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('相册-视频相关操作测试完成')

    def test_gallery_02(self):
        """相册-图片相关操作."""
        sc.logger.info('相册-图片相关操作')
        fun_name = 'test_gallery_img'

        sc.logger.info('选择图片')
        WebDriverWait(sc.driver, 3, 1).until(
            lambda el: el.find_element_by_name('视频')).click()

        WebDriverWait(sc.driver, 3, 1).until(
            lambda el: el.find_element_by_name('图片')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('选择一个图片并进行相关操作')
        ba.gallery_clip_op()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击下一步进入预览页')
        ba.find_element_click('predicate', 10, iOS_elements.el_gallery_next)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作页')
        ba.back_to_home()
        sc.logger.info('相册-图片相关操作测试完成')

    def test_gallery_03(self):
        """相册-放弃操作."""
        sc.logger.info('相册-放弃操作')
        fun_name = 'test_gallery_giveup'

        sc.logger.info('点击“视频剪辑”按钮')
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_xpath(iOS_elements.el_home_edit)).click()
        except TimeoutException:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_xpath(iOS_elements.home_edit)).click()

        sc.logger.info('添加"视频"')
        ba.gallery_clip_add('视频', 2)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('左上角返回')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_name(iOS_elements.gallery_back)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('放弃')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_name('丢弃')).click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('相册-放弃操作相关操作测试完成')