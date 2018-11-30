#coding=utf-8
import unittest
from iOS.Base import script_ultils as sc
from iOS.iOSCrashAnalysis.CrashExport import *
from iOS.Base.FileOperate import *
import os
import requests
from iOS.Base import mysql_operation
from iOS.Base import HTMLTestRunner
from iOS.Base.resultCollect import ResultCollect
from iOS.Base.getPakeage import getPakeage

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
    start_time = time.strftime('%Y%m%d%H%M%S', time.localtime())

    fp = open(reportFile, 'wb+')
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

    print('解析crash report')
    find_str = 'XiaoYing-'  # 待测app crashreport文件关键字
    file_format1 = [".ips"]  # 导出的crash文件后缀
    file_format2 = [".crash"]  # 解析后的crash文件后缀
    CrashExport(find_str, file_format1, file_format2)
    end_time = time.strftime('%Y%m%d%H%M%S', time.localtime())

    print('测试结果数据解析并DB存储')
    results = ResultCollect().get_report_info(reportFile)
    print(results)

    loacl_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
    iOS_tag = 'iOS_' + loacl_time

    print('获取ipa安装包信息')
    ipainfo = getPakeage().getIpaInfo(ipa_path)

    apkdata = {
            'app_name': ipainfo[0],
            'package_name': ipainfo[1],
            'ver_name': ipainfo[2],
            'ver_code': ipainfo[3],
            'file_name': 'day_inke_release_xiaoying.ipa',
            'tag': iOS_tag
        }

    taskdata = {
        'start_time': start_time,
        'end_time': end_time,
        'app_name': ipainfo[0],
        'app_version': ipainfo[2],
        'devices': 1,
        'tag': iOS_tag
    }

    resultdata = {
        'device_name': deviceName + '_' + deviceID,
        'count': int(results.get('Count')),
        'pass': int(results.get('Pass')),
        'fail': int(results.get('Fail')),
        'error': int(results.get('Error')),
        'tag': iOS_tag
    }

    print('taskdata:', taskdata)
    mysql_operation.insert_ui_tasks(taskdata)

    print('resultdata:', resultdata)
    mysql_operation.insert_ui_results(resultdata)

    print('apkdata:', apkdata)
    mysql_operation.insert_ui_apks_info(apkdata)

    print("压缩测试结果并传")
    f = FileFilt()
    results_file = f.zip_report(loacl_time,'./Results/', './Results_ZIP/')
    url = 'http://10.0.xx.xx:5100/api/v1/report'
    files = {'file': open(results_file, 'rb')}
    response = requests.post(url, files=files)
    json = response.json()

    print("删除本次的测试结果")
    f.DelFolder('./Results/')
    print("xxxxxxxxxxxxxxxxxxxxxxxxx Finish Test xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")