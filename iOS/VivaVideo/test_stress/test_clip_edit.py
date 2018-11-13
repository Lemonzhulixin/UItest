# -*- coding: utf-8 -*-
"""复杂编辑测试用例."""
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from iOS.Base import base as ba, script_ultils as sc, iOS_elements


class TestEditClip(TestCase):
    """镜头编辑相关操作的测试类."""

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

    def test_edit_01_theme(self):
        """镜头编辑-切换主题."""
        sc.logger.info('镜头编辑-切换主题')
        fun_name = 'test_clip_theme'

        sc.logger.info('打开一个草稿视频')
        ba.home_first_click('更多草稿')

        sc.logger.info('点击草稿封面')
        ba.open_draft(iOS_elements.el_studio_draft)
        sc.capture_screen(fun_name, self.img_path)

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
        sc.logger.info('镜头编辑-切换主题测试完成')

    def test_edit_02_music(self):
        """镜头编辑-添加配乐."""
        sc.logger.info('镜头编辑-添加配乐')
        fun_name = 'test_music_add'

        sc.logger.info('点击“添加配乐”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_xpath('(//XCUIElementTypeImage[@name="xiaoying_itembar_music"])[2]')).click()
        sc.capture_screen(fun_name, self.img_path)

        try:
            sc.logger.info('删除配乐')
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_name(iOS_elements.btn_music_del)).click()

            sc.logger.info('点击添加配乐')
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_name('点击添加配乐')).click()
        except TimeoutException:
            sc.logger.info('未添加过配乐，先添加配乐')

        sc.logger.info('添加配乐')
        ba.music_add()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('暂停播放')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.btn_stop)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('确定')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_accessibility_id(iOS_elements.btn_music_confirm)).click()
        sc.logger.info('镜头编辑-添加配乐测试完成')

    def test_edit_03_edit(self):
        """镜头编辑."""
        sc.logger.info('镜头编辑')
        fun_name = 'test_clip_edit'

        start_x = self.width // 2
        start_y = self.height // 8
        start_bottom = self.height - start_y

        sc.logger.info('点击“镜头编辑”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("镜头编辑")).click()
        sc.capture_screen(fun_name, self.img_path)

        video_flag = 0

        sc.logger.info('镜头编辑-滤镜')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("滤镜")).click()
        sc.capture_screen(fun_name, self.img_path)

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

        sc.logger.info('镜头编辑-比例')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("比例和背景")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('切换到"比例tab"')
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name(iOS_elements.btn_bg_pro)).click()
            sc.capture_screen(fun_name, self.img_path)
        except TimeoutException:
            sc.logger.info('已经在"比例tab"')

        sc.logger.info('剪辑-切换1:1比例')
        el_proportion = "vivavideo_edit_icon_proportion_1_1"
        ba.clip_proportion(el_proportion)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('镜头编辑-图片时长')
        try:
            sc.logger.info('点击“图片时长”')
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_name("图片时长")).click()

            sc.logger.info('点击“确认”')
            sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()
        except TimeoutException:
            video_flag = 1
            sc.logger.info('当前镜头是视频，不支持时长')

        sc.logger.info('镜头编辑-修剪')
        if video_flag == 1:
            sc.logger.info('点击“修剪”')
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name("修剪")).click()

            sc.logger.info('点击“剪除”')
            try:
                WebDriverWait(sc.driver, 5, 1).until(
                    lambda x: x.find_element_by_name("剪中间")).click()
            except TimeoutException:
                WebDriverWait(sc.driver, 5, 1).until(
                    lambda x: x.find_element_by_name("剪除")).click()

            sc.logger.info('点击“确认”')
            sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()

        sc.logger.info('镜头编辑-分割')
        if video_flag == 1:
            sc.logger.info('点击“分割”')
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name("分割")).click()

            sc.logger.info('点击“确认”')
            sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()

        sc.logger.info('剪辑-镜头编辑-复制')
        sc.driver.find_element_by_name("复制").click()

        sc.logger.info('工具栏左滑一些')
        el_copy = sc.driver.find_element_by_name("复制")
        coord_x = el_copy.location.get('x')
        coord_y = el_copy.location.get('y')
        sc.swipe_by_ratio(coord_x, coord_y, 'left', 0.5, 500)

        sc.logger.info('镜头编辑-变速')
        if video_flag == 1:
            sc.logger.info('点击"变速"')
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name("变速")).click()

            sc.logger.info('应用于全部镜头')
            sc.driver.find_element_by_name('应用于全部镜头').click()

            sc.logger.info('点击“确认”')
            sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()

        sc.logger.info('镜头编辑-调色')
        sc.logger.info('点击“调色”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("调色")).click()

        sc.logger.info('点击“取消”')
        sc.driver.find_element_by_name(iOS_elements.el_cancel_btn).click()

        sc.logger.info('工具栏左滑一些')
        el_adjuest = sc.driver.find_element_by_name("调色")
        coord_x = el_adjuest.location.get('x')
        coord_y = el_adjuest.location.get('y')
        sc.swipe_by_ratio(coord_x, coord_y, 'left', 0.5, 500)

        sc.logger.info('镜头编辑-镜头倒放')
        if video_flag == 1:
            ba.clip_reverse()

        sc.logger.info('剪辑-镜头编辑-静音')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_name("静音")).click()

        sc.logger.info('工具栏左滑一些')
        el_mute = sc.driver.find_element_by_name("静音")
        coord_x = el_mute.location.get('x')
        coord_y = el_mute.location.get('y')
        sc.swipe_by_ratio(coord_x, coord_y, 'left', 0.5, 500)

        sc.logger.info('镜头编辑-旋转')
        sc.logger.info('点击“旋转”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("旋转")).click()

        sc.logger.info('镜头编辑-转场')
        sc.logger.info('点击“转场”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("转场")).click()

        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name("应用于全部镜头")).click()
        except TimeoutException:
            sc.logger.info('只有一个镜头，无法添加转场')
            return True

        sc.logger.info('下载更多')
        ba.more_download('下载更多')

        sc.logger.info('选择一个"转场"使用')
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_xpath(iOS_elements.btn_transition_cho)).click()
        except TimeoutException:
            sc.logger.info('选择一个"转场"下载')
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name(iOS_elements.btn_transition_download)).click()

            sc.logger.info('使用')
            WebDriverWait(sc.driver, 10, 1).until(
                lambda x: x.find_element_by_xpath(iOS_elements.btn_transition_cho)).click()

        sc.logger.info('点击“确认”')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_confirm_btn)).click()

        try:
            sc.logger.info('点击“确认”')
            sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()
        except NoSuchElementException:
            sc.logger.info('只有一个镜头，无法应用转场')

        sc.logger.info('工具栏左滑一些')
        el_t = sc.driver.find_element_by_name("转场")
        coord_x = el_t.location.get('x')
        coord_y = el_t.location.get('y')
        sc.swipe_by_ratio(coord_x, coord_y, 'left', 0.5, 600)

        sc.logger.info('剪辑-镜头编辑-图片动画')
        if video_flag == 0:
            sc.logger.info('点击“图片动画”')
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name("图片动画")).click()

        sc.logger.info('保存/上传')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("保存/上传")).click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('镜头编辑测试完成')

    def test_edit_04_export(self):
        """镜头编辑-导出."""
        sc.logger.info('镜头编辑-导出')
        fun_name = 'test_clip_export'

        sc.logger.info('点击“保存到相册”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("保存到相册")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“480P 清晰”')
        ba.export_video("清晰 480P")
        sc.logger.info('镜头编辑-导出测试完成')


