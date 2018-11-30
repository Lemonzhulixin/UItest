# -*- coding: utf-8 -*-
from appium import webdriver
import time
from iOS.Base.start_appium import myserver
from iOS.Base.getPakeage import getPakeage
import os


def env_init_iOS(deviceName, deviceID, port):
    desired_caps = {
        'platformName': 'iOS',
        'platformVersion': '',
        'deviceName': deviceName,
        'bundleId': 'com.quvideo.XiaoYing',
        'app': '',
        'noReset': True,
        'automationName': 'XCUITest',
        'udid': deviceID,
        'xcodeOrgId': 'BMP99N9345',
        'xcodeSigningId': 'iPhone Developer',
        'autoLaunch': True,
        'wdaLocalPort': 8001
    }

    remote_url = 'http://localhost:' + str(port) + '/wd/hub'
    time.sleep(5)
    drivers = webdriver.Remote(remote_url, desired_caps)
    return drivers


# device_list = [('iPhone2140','e80251f0e66967f51add3ad0cdc389933715c3ed')]
device_list = [('iPhone2146','abab40339eaf2274aaf1ef068e11d6f85d84aae1')]

myserver().create_pools(len(device_list))
port_list = myserver().ports

deviceName = device_list[0][0]
deviceID = device_list[0][1]
port = port_list[0]

print('远程复制ipa文件到本地')
cmd_copy = 'sshpass -p ios scp -r xxx@10.0.xx.xx:/Users/iOS_Team/XiaoYing_AutoBuild/XiaoYing/XiaoYingApp/fastlane/output_ipa/ ~/Desktop'
os.system(cmd_copy)

print('ipa文件本地路径')
path = "/Users/zhulixin/Desktop/output_ipa/"
file_format = ['.ipa']
ipa_path = getPakeage().get_ipa(path, file_format)
print(ipa_path)

print('安装ipa文件到设备中')
getPakeage().install(path, file_format, deviceID)

driver = env_init_iOS(deviceName, deviceID, port)
