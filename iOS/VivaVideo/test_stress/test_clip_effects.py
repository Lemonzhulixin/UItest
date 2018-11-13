# -*- coding: utf-8 -*-
"""复杂编辑测试用例."""
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from iOS.Base import base as ba, script_ultils as sc, iOS_elements
import random


class TestEditEffects(TestCase):
    """复杂编辑-添加多个效果测试类."""

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

    def test_effcts_01_music(self):
        """复杂操作-添加配乐."""
        sc.logger.info('复杂操作-添加配乐')
        fun_name = 'test_effcts_music'

        sc.logger.info('打开一个草稿视频')
        ba.home_first_click('更多草稿')

        sc.logger.info('点击草稿封面')
        ba.open_draft(iOS_elements.el_studio_draft)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“素材·效果”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("素材·效果")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"多段配乐"')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('多段配乐')).click()

        sc.logger.info("循环添加3个'配乐'")
        for i in range(3):
            ba.loop_add_music()
            time.sleep(1)
            sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('确认添加')
        sc.logger.info('确定')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_confirm_btn)).click()
        sc.logger.info('复杂操作-添加配乐测试完成')

    def test_effcts_02_text(self):
        """复杂操作-添加字幕."""
        sc.logger.info('复杂操作-添加字幕')
        fun_name = 'test_effcts_text'

        sc.logger.info('点击"字幕"')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('字幕')).click()

        sc.logger.info('添加动态字幕')
        for i in range(3):
            ba.loop_add_text()
            time.sleep(1)
            sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加普通字幕')
        for i in range(3):
            ba.loop_add_comm_text()
            time.sleep(1)
            sc.capture_screen(fun_name, self.img_path)

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
        sc.logger.info('复杂操作-添加字幕测试完成')

    def test_effcts_03_sticker(self):
        """复杂操作-添加贴纸."""
        sc.logger.info('复杂操作-添加贴纸')
        fun_name = 'test_edit_sticker'

        sc.logger.info('点击“贴纸”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("贴纸")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加普通贴纸')
        for i in range(3):
            try:
                sc.logger.info('点击"添加"')
                WebDriverWait(sc.driver, 3, 1).until(
                    lambda x: x.find_element_by_name('添加')).click()
            except TimeoutException:
                sc.logger.info('第一次进入贴纸，无添加按钮')

            sc.logger.info('选择一个普通"贴纸"添加')
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_xpath(iOS_elements.el_sticker_cho)).click()

            sc.logger.info('确认添加')
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name(iOS_elements.el_confirm_btn)).click()
            sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加GIF贴纸')
        for i in range(3):
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_name('添加')).click()

            sc.logger.info('点击GIF')
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name('GIF')).click()
            sc.capture_screen(fun_name, self.img_path)

            sc.logger.info('添加一个GIF"贴纸"')
            ba.material_used('下载')
            sc.capture_screen(fun_name, self.img_path)

            sc.logger.info('确定')
            time.sleep(0.5)
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name(iOS_elements.el_confirm_btn)).click()

        sc.logger.info('退出贴纸添加页面')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_confirm_btn)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('复杂操作-添加贴纸测试完成')

    def test_effcts_04_collage(self):
        """复杂操作-添加画中画."""
        sc.logger.info('复杂操作-添加画中画')
        fun_name = 'test_edit_collage'

        sc.logger.info('点击"画中画"')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('画中画')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加图片画中画')
        ba.collage_add('图片')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('确认添加')
        ba.effect_add_confirm()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"画中画"')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('画中画')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加视频画中画')
        ba.collage_add('视频')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('确认添加')
        ba.effect_add_confirm()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"画中画"')
        time.sleep(0.5)
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('画中画')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加gif画中画')
        ba.collage_add('GIF')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('确认添加')
        ba.effect_add_confirm()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('复杂操作-添加画中画测试完成')

    def test_effcts_05_fx(self):
        """复杂操作-添加特效."""
        sc.logger.info('复杂操作-添加特效')
        fun_name = 'test_edit_fx'

        sc.logger.info('点击"特效"')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('特效')).click()
        sc.capture_screen(fun_name, self.img_path)

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
        sc.logger.info('复杂操作-添加特效测试完成')

    def test_effcts_05_sound(self):
        """复杂操作-添加配音和音效."""
        sc.logger.info('复杂操作-添加配音和音效')
        fun_name = 'test_edit_sound'

        sc.logger.info('左滑并点击"配音和音效"')
        el_loc = WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('画中画'))
        ba.swipe_left(el_loc, 0.3, 300)

        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('配音和音效')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('"录制"一段音频')
        ba.sound_rec_add()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加一段音效')
        ba.sound_audio_add()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('确认添加')
        time.sleep(2)
        WebDriverWait(sc.driver, 15, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_confirm_btn)).click()
        sc.logger.info('复杂操作-添加配音和音效测试完成')

    def test_effcts_06_publish(self):
        """复杂操作-发布."""
        sc.logger.info('复杂操作-发布')
        fun_name = 'test_edit_publish'

        sc.logger.info('保存/上传')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("保存/上传")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('输入标题和描述')
        ba.publish_input()
        sc.capture_screen(fun_name, self.img_path)

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

        sc.logger.info('选择480P导出')
        try:
            sc.driver.find_element_by_name("清晰 480P").click()
        except NoSuchElementException:
            sc.logger.error('网络不可用，取消上传，请手动执行相关测试')
            return False

        sc.logger.info('开始导出并上传')
        try:
            WebDriverWait(sc.driver, 300, 1).until(
                lambda x: x.find_element_by_name('发现'))
        except TimeoutException:
            sc.logger.error('发布超时')

        sc.logger.info('复杂操作-发布测试完成')