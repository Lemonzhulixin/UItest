# -*- coding: utf-8 -*-
from appium import webdriver
import time
from iOS.Base.start_appium import myserver


def env_init_iOS(device_name, udid, port):
    desired_caps = {
        'platformName': 'iOS',
        'platformVersion': '',
        'deviceName': device_name,
        'bundleId': 'com.quvideo.XiaoYing',
        'app': '',
        'noReset': True,
        'automationName': 'XCUITest',
        'udid': udid,
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

dev = device_list[0][0]
udid = device_list[0][1]
port = port_list[0]

driver = env_init_iOS(dev, udid, port)
