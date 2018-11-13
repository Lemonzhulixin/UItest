# -*- coding: utf-8 -*-
"""各尺寸导出测试用例."""
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS.Base import base as ba, script_ultils as sc, iOS_elements


class TestExport(TestCase):
    """导出相关操作的测试类."""

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

    def test_export_01_add(self):
        """导出-添加镜头."""
        sc.logger.info('导出-添加镜头')
        fun_name = 'test_export_add'

        sc.logger.info('打开一个草稿视频')
        ba.home_first_click('更多草稿')

        sc.logger.info('点击草稿封面')
        ba.open_draft(iOS_elements.el_studio_draft)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“镜头编辑”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("镜头编辑")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('从相册添加')
        ba.clip_add('相册')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('拍摄添加镜头')
        ba.clip_add('拍摄')
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('导出-添加镜头测试完成')

    def test_export_02_del(self):
        """导出-删除镜头."""
        sc.logger.info('导出-删除镜头')
        fun_name = 'test_export_del'

        clip_list = sc.driver.find_elements_by_name('')

        if len(clip_list) >= 2:
            clip_list = clip_list[:2]

        for clip in clip_list:
            clip.click()

            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name('确认')).click()
            time.sleep(0.5)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('保存/上传')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("保存/上传")).click()
        sc.capture_screen(fun_name, self.img_path)

    def test_export_03_720P(self):
        """导出-720P."""
        sc.logger.info('导出-720P')
        fun_name = 'test_export_720P'

        sc.logger.info('点击“保存到相册”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("保存到相册")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“高清 720P”')
        ba.export_video("高清 720P")
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('导出-保存到相册-720P-二次导出测试完成')