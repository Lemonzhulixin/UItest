import mysql.connector
from sshtunnel import SSHTunnelForwarder
import sys

def upload_sql(sql, value):
    db_host = '127.0.0.1'
    with SSHTunnelForwarder(
            ssh_address_or_host=('10.0.xx.xx', 22),
            ssh_username="shu",
            ssh_password="1108",
            remote_bind_address=(db_host, 3306)
    ) as tunnel:
        port = tunnel.local_bind_port
        my_connect = mysql.connector.connect(
            host='127.0.0.1',
            port=port,
            db='qutest',
            user='root',
            password='12345678',
            charset='utf8'
        )
        my_cursor = my_connect.cursor()
        try:
            my_cursor.execute(sql, value)
            my_connect.commit()
        except mysql.connector.Error as err:
            print("Failed inserting by errorcode {}".format(err))
        my_cursor.close()
        my_connect.close()

def insert_ui_tasks(value):
    """
    （UI自动化测试）
    写入task信息
    :param value:
        data = {
            'start_time': '20181212010000',
            'end_time': '20181212011000',
            'app_name': '小影',
            'app_version': '7.6.0',
            'devices': 2,
            'tag': 'Android-20181212010000'
        }
    :return:
    """
    my_sql = "INSERT INTO ui_tasks (task_id, start_time, end_time, app_name, app_version, devices, tag)" \
             " VALUES (NULL, %(start_time)s, %(end_time)s, %(app_name)s, %(app_version)s, %(devices)s, %(tag)s)"
    upload_sql(my_sql, value)
    return


def insert_ui_results(value):
    """
    （UI自动化测试）
    写入result信息
    :param value:
        data = {
            'device_name': 'Nexus 5',
            'count': 10,
            'pass': 8,
            'fail': 1,
            'error': 0,
            'tag': 'Android-20181212010000'
        }
    :return:
    """
    my_sql = "INSERT INTO ui_results (result_id, device_name, count, pass, fail, error, tag, device_log, report)" \
             " VALUES (NULL, %(device_name)s, %(count)s, %(pass)s, %(fail)s, %(error)s, %(tag)s, NULL, NULL)"
    upload_sql(my_sql, value)
    return

def insert_ui_apks_info(value):
    """
    （UI自动化测试）
    写入测试中使用的安装包信息
    :param value:
        data = {
            'app_name': '小影lite',
            'package_name': 'com.quvideo.vivavideo.lite',
            'ver_name': '1.0.2',
            'ver_code': '6100010',
            'file_name': 'XiaoYing_lite_google_V1.0.2_0-googleplay-OthersAbroadRelease.apk',
            'tag': 'Android_20181212010000'
        }
    :return:
    """
    my_sql = "INSERT INTO ui_apks_info (apk_id, app_name, package_name, ver_name, ver_code, file_name, tag) " \
             "VALUES (NULL, %(app_name)s, %(package_name)s, %(ver_name)s, %(ver_code)s, %(file_name)s, %(tag)s)"
    upload_sql(my_sql, value)
    return
