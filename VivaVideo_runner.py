#coding=utf-8
import unittest
from iOS.Base import script_ultils as sc, HTMLTestRunner
from iOS.iOSCrashAnalysis.CrashExport import *
from iOS.iOSCrashAnalysis.FileOperate import *
from iOS.Base.script_params import *
import os
from iOS.Base.resultCollect import ResultCollect

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def RunTest(TestCases):
    suite = unittest.TestSuite()

    if TestCases == 'full':
        # 用例路径
        sc_path1 = os.path.join(os.getcwd(), "iOS/VivaVideo/test_ahead")
        sc_path2 = os.path.join(os.getcwd(), "iOS/VivaVideo/test_creations/test_camera")
        sc_path3 = os.path.join(os.getcwd(), "iOS/VivaVideo/test_creations/test_edit")
        sc_path4 = os.path.join(os.getcwd(), "iOS/VivaVideo/test_creations/test_preview")
        sc_path5 = os.path.join(os.getcwd(), "iOS/VivaVideo/test_creations/test_publish")
        sc_path6 = os.path.join(os.getcwd(), "iOS/VivaVideo/test_stress")

        suite1 = unittest.TestLoader().discover(sc_path1, pattern="*.py", top_level_dir=None)
        suite2 = unittest.TestLoader().discover(sc_path2, pattern="*.py", top_level_dir=None)
        suite3 = unittest.TestLoader().discover(sc_path3, pattern="*.py", top_level_dir=None)
        suite4 = unittest.TestLoader().discover(sc_path4, pattern="*.py", top_level_dir=None)
        suite5 = unittest.TestLoader().discover(sc_path5, pattern="*.py", top_level_dir=None)
        suite6 = unittest.TestLoader().discover(sc_path6, pattern="*.py", top_level_dir=None)

        suite = unittest.TestSuite(suite1)

        # suite = unittest.TestSuite([suite1, suite2, suite3, suite4, suite5, suite6])

    elif TestCases == 'stress':
        # 用例路径
        sc_path1 = os.path.join(os.getcwd(), "iOS/VivaVideo/test_ahead")
        sc_path2 = os.path.join(os.getcwd(), "iOS/VivaVideo/test_stress")

        suite1 = unittest.TestLoader().discover(sc_path1, pattern="*.py", top_level_dir=None)
        suite2 = unittest.TestLoader().discover(sc_path2, pattern="*.py", top_level_dir=None)

        suite = unittest.TestSuite([suite1, suite2])

    return suite

if __name__ == '__main__':
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxx Start Test xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    log_path = sc.path_lists[1]
    report_path = sc.path_lists[2]
    crash_path = sc.path_lists[3]

    reportFile = report_path + "report.html"
    logFile = log_path + 'output.log'

    # fp = open(reportFile, 'wb+')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title='VivaVideo UI（iOS） 测试结果',
    #     description='详细测试报告',
    #     verbosity = 2
    # )
    # runner.run(RunTest('full'))
    # fp.close()
    # print('关闭appium')
    # time.sleep(1)
    # cmd_kill = 'pkill node'
    # os.system(cmd_kill)

    print('解析crash report')
    find_str = 'XiaoYing-'  # 待测app crashreport文件关键字
    file_format1 = [".ips"]  # 导出的crash文件后缀
    file_format2 = [".crash"]  # 解析后的crash文件后缀
    CrashExport(find_str, file_format1, file_format2)

    # print('测试结果数据解析')
    # results = ResultCollect().get_report_info(reportFile)
    # print(results)
    #
    # log = os.path.abspath(logFile)
    # print(log)
    #
    # report = os.path.abspath(reportFile)
    # print(report)
    #
    # deviceName = device_list[0][0]
    # deviceID = device_list[0][1]
    # print(deviceName, deviceID)

    # afterPath = os.path.join(crash_path + 'After')
    # if not os.path.exists(afterPath):
    #     os.makedirs(afterPath)

    # print("输出所有crash文件路径")
    # f = FileOperate.FileFilt()
    # f.FilePath(afterPath)


    # ipsFiles = []
    # f = FileOperate.FileFilt()
    # f.FindFile(find_str, file_format1, afterPath)
    #
    # for file in f.fileList:
    #     ipsFiles.append(os.path.abspath(file))
    # print('ipsFiles', ipsFiles)


    # print("删除旧的crash文件")
    # f.DelFolder(afterPath)

    print("xxxxxxxxxxxxxxxxxxxxxxxxx Finish Test xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")