import os
import random
import socket
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class myserver(object):

    def isOpen(self,ip, port):  # 判断端口是否被占用
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, int(port)))
            s.shutdown(2)  # shutdown参数表示后续可否读写
            print('%d is used' % port)
            return True
        except Exception:
            print('%d is available' % port)
            return False

    def getport(self):  # 获得端口号
        port = random.randint(4723, 4800)
        # 判断端口是否被占用
        while self.isOpen('127.0.0.1', port):
            port = random.randint(4723, 4800)
        return port

    def run(self,port):
        """启动appium服务
        :return port_list"""
        print('start appium service')
        cmd_appium = 'appium -p ' + str(port) + ' --session-override'
        print(cmd_appium)

        try:
            #启动appium服务
            logpath = ''.join(["./Results/logs/"])
            if not os.path.exists(logpath):
                os.makedirs(logpath)
            appiumlog = open(logpath + 'appiumlog.log', 'w')
            subprocess.Popen(cmd_appium, shell=True, stdout=appiumlog)
        except Exception as msg:
            print('error message:', msg)
            raise

    def kill_appium(self):
        cmd_kill = 'pkill node'
        subprocess.run(cmd_kill, shell=True)
        print('close appium service')

    executor = ThreadPoolExecutor(6)
    ports = list()

    def create_pools(self, device_list_length):
        for i in range(device_list_length):
            port = self.getport()
            self.ports.append(port)
            self.executor.submit(self.run, port)
        return ('running')