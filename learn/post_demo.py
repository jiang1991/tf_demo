#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import jres.tools
import json
import base64
import time


email = 'wangjiang@viatomtech.com'
psd = 'Viatom4E'
auth = base64.b64encode(str.encode('%s:%s' % (email, psd))).decode("ascii")
headers = {'Authorization': 'Basic %s' % auth}

deviceJson = '''{"Region":"CE","Model":"1641","HardwareVer":"AA","SoftwareVer":"4.2.5","BootloaderVer":"0.1.0.0","FileVer":"3","SPCPVer":"1.4","SN":"1802230655","CurTIME":"2018-12-19,10:40:18","CurBAT":"100%","CurBatState":"0","CurOxiThr":"90","CurMotor":"0","CurPedtar":"556","CurMode":"0","CurState":"0","BranchCode":"","FileList":"20180517151431,20180803143622,20180511010607,20180517114751,"}'''


def get_o2_update():
    r = requests.get('https://api.viatomtech.com.cn/update/O2/us_ver_3')
    # print(r.status_code, r.json())
    jres.tools.print_response(r)


# get / basic auth
def get_patient():

    r = requests.get('https://cloud.viatomtech.com/search/patient', headers=headers)
    jres.tools.print_response(r)


# post / form-data
def login():

    form_data = {
        'email': email,
        'password': psd
    }

    r = requests.post('http://cloud.viatomtech.com/user/login', data=form_data)
    jres.tools.print_response(r)


# post / json
def create_device():
    device = {
        'deviceName': 'sleepo2',
        'deviceSn': 1802230655,
        'branchCode': 20010000,
        'btlVersion': '1.0.0',
        'appVersion': '4.2.5',
        'fileVersion': 3,
        'deviceJson': deviceJson
    }

    print(json.dumps(device))

    r = requests.post('https://cloud.viatomtech.com/oxiupload/device/create', headers=headers, data=json.dumps(device))
    jres.tools.print_response(r)


# get / with params - page
def get_device_list_byuser():
    params = {"page": 2}

    r = requests.get('https://cloud.viatomtech.com/oxiupload/resource/byuser', params=params, headers=headers)

    jres.tools.print_response(r)


# post / json
def create_resource():

    dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    detail = {
        # '2018-08-03 14:36:22 +0800'
        'recordDate': dt,
        'recordDuration': 600
    }
    device = {
        "name": "sleepo2",
        "sn": 1802230655
    }
    with open('./oxidata/20180517114751', 'rb') as f:
        oxi_bytes = f.read()
        oxi_data = base64.b64encode(oxi_bytes).decode("ascii")
        # print(oxi_data)
    oxi_str = {
        "resourceType": "sleep",
        "resourceVersion": "3",
        "resourceDetail": detail,
        "device": device,
        "resourceData": oxi_data
    }

    r = requests.post('https://cloud.viatomtech.com/oxiupload/resource/create', headers=headers, data=json.dumps(oxi_str))
    jres.tools.print_response(r)


if __name__ == '__main__':
    # for x in range(100):
    #     print('\nindex: %s ' % x)
    #     create_resource()
    #     time.sleep(1)
    get_device_list_byuser()
