import os
from ftplib import FTP
from os import path
from optparse import OptionParser
# from FtpDownload import spilt_cmd
import socket
import sys

import requests


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def test():
    # data = ['test_4_expect.jpg']
    # temname = data[0]
    # temname2 = data[0].split('.')
    # print(type(temname))
    # print(temname)
    # print(temname2)
    # print(os.getcwd())
    # newdir = Path(f'{os.getcwd()}/images/backups/')
    # print(newdir)
    # print("{:*{}25}".format('测试开始','^'))
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect(('127.0.0.1', 4723))
    # s.shutdown(2)
    # print('%s:%d is ready' % ('127.0.0.1', 4723))
    #
    # m = os.system('adb devices -l | grep "SM"')
    # if len(str(m)) == 1:
    #     pass
    # else:
    #     print('device not connected')

    command =  'scp /Users/jackrechard/Desktop/tp.png root@10.244.12.21:/home/chengdegang'
    res =  os.system(command)
    print(res)

def upload():
    cmds = ['-u', 'oracle', '-w', 'oracle', '-a', '10.244.12.21', '-p', '21', '-s', 'ProjData', '-l', 'c://tt.txt']
    print(cmds)

def send_file(file,key):
    id_url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key={key}&type=file"  # 上传文件接口地址
    data = {'file': open(file, 'rb')}  # post jason
    response = requests.post(url=id_url, files=data)  # post 请求上传文件
    json_res = response.json()  # 返回转为json
    media_id = json_res['media_id']  # 提取返回ID
    url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}'   # debug
    headers = {'Content-Type': 'application/json'}
    data = {
            "msgtype": "file",
            "file": {
                "media_id": f"{media_id}"
            }
        }
    r = requests.post(url, headers=headers, json=data)
    print(r.content)
    # print(media_id)
    print('send ok')

def send_msg_to_group():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=f4b5ffa6-8412-47ed-9c7d-b0c6b22167e8'   # debug
    headers = {'Content-Type': 'application/json'}
    data = {
            "msgtype": "file",
            "file": {
                "media_id": "3elBBhR8Zxz5bCCM9KAfhRNWw8JK9YqCN4YTwBto1r45nGut1UHF97-fwQKCfskFy"
            }
        }
        # "msgtype": "markdown",
        # "markdown": {
        #     "content": 'hi , this is u need msg   <font color=\"warning\">请点击链接下载</font>\n'
        #                '[统计数据结果](http://10.244.12.21:8080/view/Tools/job/crawl_phone/ws/Model_summary.xlsx)'
        #
        # }

    r = requests.post(url, headers=headers, json=data)
    print(r.content)

def get():
    print(os.getcwd())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # test()
    # upload()
    # send_msg_to_group()
    # send_file(file='/Users/jackrechard/PycharmProjects/mobile_auto/test.html',
    #           key='f4b5ffa6-8412-47ed-9c7d-b0c6b22167e8')
    get()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

