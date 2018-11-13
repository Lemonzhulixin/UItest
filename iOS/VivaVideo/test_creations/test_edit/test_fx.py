# -*- coding: utf-8 -*-
"""特效的基本操作测试用例."""
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS.Base import base as ba, script_ultils as sc, iOS_elements
from selenium.common.exceptions import TimeoutException


class TestEditFX(TestCase):
    """特效的基本操作测试类."""

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

    def test_edit_fx_01(self):
        """剪辑-特效下载."""
        sc.logger.info('剪辑-特效下载')
        fun_name = 'test_edit_fx_download'

        sc.logger.info('点击创作中心主按钮')
        ba.home_enter()

        sc.logger.info('点击视频剪辑')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_home_edit)).click()

        sc.logger.info('添加视频')
        ba.gallery_clip_add('视频', 2)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击下一步')
        ba.find_element_click('predicate', 10, iOS_elements.el_gallery_next)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“效果”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("素材·效果")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"特效"')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('特效')).click()
        sc.logger.info('剪辑-特效下载测试完成')

    def test_edit_fx_02(self):
        """剪辑-特效使用."""
        sc.logger.info('剪辑-特效使用')
        fun_name = 'test_edit_fx_use'

        el_more = 'xiaoying itembar down more'
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name(el_more))
        except TimeoutException:
            sc.logger.info('当前位置已添加过"特效"')

            sc.logger.info('点击屏幕弹出已添加的特效编辑页面')
            ba.screen_tap('特效', 200, 200)

            sc.logger.info('删除')
            sc.driver.find_element_by_name('删除').click()

            sc.logger.info('添加')
            WebDriverWait(sc.driver, 10, 1).until(
                lambda x: x.find_element_by_name('添加')).click()

        sc.logger.info('下载“特效”')
        fx_list = sc.driver.find_elements_by_xpath(iOS_elements.el_fx_download)
        if fx_list:
            for fx in fx_list:
                fx.click()
                time.sleep(5)
        else:
            pass

        sc.logger.info('使用"特效"')
        sc.driver.find_element_by_xpath(iOS_elements.el_fx_cho).click()

        sc.logger.info('确认添加')
        sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()
        time.sleep(5)

        sc.logger.info('再次添加特效')
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_name('添加')).click()

        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(el_more))

        sc.logger.info('使用"特效"')
        sc.driver.find_element_by_xpath(iOS_elements.el_fx_cho).click()

        sc.logger.info('确认添加')
        sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()
        time.sleep(5)
        sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()

        try:
            WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_xpath('//XCUIElementTypeButton[@name="1"]')).click()
        except TimeoutException:
            sc.logger.info('返回首页后，无广告弹出')
        sc.logger.info('剪辑-特效使用测试完成')

    # def test_edit_fx_03(self):
    #     """剪辑-特效-删除&放弃."""
    #     sc.logger.info('剪辑-特效-删除&放弃')
    #     fun_name = 'test_edit_fx_del'
    #
    #     sc.logger.info('点击草稿封面')
    #     time.sleep(0.5)
    #     ba.open_draft(iOS_elements.el_studio_draft)
    #     sc.capture_screen(fun_name, self.img_path)
    #
    #     sc.logger.info('点击“效果”')
    #     WebDriverWait(sc.driver, 5, 1).until(
    #         lambda x: x.find_element_by_name("素材·效果")).click()
    #     sc.capture_screen(fun_name, self.img_path)
    #
    #     sc.logger.info('点击屏幕弹出已添加的特效编辑页面')
    #     ba.screen_tap('特效', 200, 200)
    #
    #     sc.logger.info('删除')
    #     sc.driver.find_element_by_name('删除').click()
    #     sc.capture_screen(fun_name, self.img_path)
    #
    #     sc.logger.info('添加特效并放弃')
    #     WebDriverWait(sc.driver, 10, 1).until(
    #         lambda x: x.find_element_by_name('添加')).click()
    #     sc.capture_screen(fun_name, self.img_path)
    #
    #     sc.logger.info('点击"下载更多"')
    #     el_more = 'xiaoying itembar down more'
    #     ba.more_download(el_more)
    #
    #     sc.logger.info('使用特效')
    #     ba.material_used(iOS_elements.el_store_download1)
    #
    #     sc.logger.info('确定')
    #     WebDriverWait(sc.driver, 5, 1).until(
    #         lambda x: x.find_element_by_name(iOS_elements.el_confirm_btn)).click()
    #     sc.capture_screen(fun_name, self.img_path)
    #
    #     sc.logger.info('取消添加')
    #     WebDriverWait(sc.driver, 5, 1).until(
    #         lambda x: x.find_element_by_name(iOS_elements.el_cancel_btn)).click()
    #
    #     sc.logger.info('确定放弃')
    #     sc.driver.find_element_by_name('确认').click()
    #
    #     sc.logger.info('点击“存草稿”按钮')
    #     WebDriverWait(sc.driver, 5, 1).until(
    #         lambda el: el.find_element_by_name("存草稿")).click()
    #     sc.logger.info('剪辑-特效-删除&放弃测试完成')
