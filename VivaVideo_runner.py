#coding=utf-8
import os
import time
import unittest
from iOS.Base import script_ultils as sc, HTMLTestRunner
from iOS.iOSCrashAnalysis import FileOperate
from iOS.Base.script_params import *

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

        suite = unittest.TestSuite([suite1, suite2, suite3, suite4, suite5, suite6])

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
    now_time = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    report_path = sc.path_lists[2]
    filename = report_path + now_time + ".html"
    fp = open(filename, 'wb+')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='VivaVideo UI（iOS） 测试结果',
        description='详细测试报告',
        verbosity = 2
    )
    runner.run(RunTest('full'))
    fp.close()
    print('关闭appium')
    time.sleep(1)
    cmd_kill = 'pkill node'
    os.system(cmd_kill)
    print("xxxxxxxxxxxxxxxxxxxxxxxxx Finish Test xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

    print("============开始导出crashreport==========")
    find_str = 'XiaoYing-'  # 待测app crashreport文件关键字
    file_format1 = [".ips"]  # 导出的crash文件后缀
    file_format2 = [".crash"]  # 解析后的crash文件后缀

    reportPath = PATH("/Users/iOS_Team/.jenkins/workspace/iOS_UI_VivaVideo/UItest/CrashInfo/iOS/")
    beforePath = os.path.join(reportPath + '/Before')
    if not os.path.exists(beforePath):
        os.makedirs(beforePath)

    afterPath = os.path.join(reportPath + '/After')
    if not os.path.exists(afterPath):
        os.makedirs(afterPath)
    print("导出设备中的所有crash文件")
    # for i in range(0, len(l_devices)):
    #     duid = l_devices[i]["devices"]
    #     exportReport = 'idevicecrashreport -u ' + duid + ' ' + beforePath + '/'
    #     print(exportReport)
    #     os.system(exportReport) #导出设备中的crash

    duid = device_list[0][1]
    exportReport = 'idevicecrashreport -u ' + duid + ' ' + beforePath + '/'
    print(exportReport)
    os.system(exportReport)  # 导出设备中的crash

    print("============开始过滤并解析待测app相关crashreport==========")
    # .bash_profile中配置以下环境，记得重启下mac
    # DEVELOPER_DIR="/Applications/XCode.app/Contents/Developer"
    # export DEVELOPER_DIR
    f = FileOperate.FileFilt()
    f.FindFile(find_str, file_format1, beforePath)
    for file in f.fileList:
        inputFile = os.path.abspath(file)  # 绝对路径
        # print(inputFile)
        analysisPath = PATH("/Users/iOS_Team/.jenkins/workspace/iOS_UI_VivaVideo/UItest/iOS/iOSCrashAnalysis/")
        cmd_analysis = 'python3 ' + analysisPath + '/BaseIosCrash.py' + ' -i ' + inputFile
        # print(cmd_analysis)
        os.system(cmd_analysis)

    # 移动解析完成的crashreport和原始ips文件到新的文件夹
    f.MoveFile(find_str, file_format1, beforePath, afterPath)
    f.MoveFile(find_str, file_format2, beforePath, afterPath)
    print("============crashreport解析完成==========")

    # 删除所有解析之前的crash文件，若不想删除，注掉即可
    print("============删除所有解析之前的crash文件==========")
    f.DelFolder(beforePath)