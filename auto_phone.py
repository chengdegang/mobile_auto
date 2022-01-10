import os
import socket
import time
import selenium
from appium import webdriver
import unittest
import similar
from appium.webdriver.common.mobileby import MobileBy
from BeautifulReport import BeautifulReport as bf
from main import send_file

# """
# 测试开始，判断appium端口已开启，待测设备已连接
# """
# print("{:*{}25}".format('测试开始','^'))
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('127.0.0.1', 4723))
# s.shutdown(2)
# print('%s:%d is ready' % ('127.0.0.1', 4723))
#
# m = os.system('adb devices -l | grep "SM"')
# if len(str(m)) == 1:
#     print('device connected')
# else:
#     print('device not connected')

def setUpModule():
    print(" Module start .....")

def tearDownModule():
    print(" Module end ...")

"""
测试前保证已开启apium server并确保手机已连接（三星s8）
"""
class Test(unittest.TestCase):
    #每次方法之前执行
    def setUp(self):
        # app = '/Users/jackrechard/Desktop/appium/app-OasisTest-debug.apk'
        self.packname = 'com.ezxr.oasis_android_unity'
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "98895a384b33433756",
            # "appPackage": "com.ezxr.unitySDKDemo",#Unity测试ccc
            "appPackage": self.packname,#UnitySDK
            "appActivity": "com.netease.arinsightsdk.SplashActivity",
            'noReset': True
        }
        try:
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        except selenium.common.exceptions.WebDriverException:
            print('app连接失败！请检查连接信息')
        time.sleep(3)
        #检查是否安装应用，若没有安装则安装
        # isAppInstalled = self.driver.is_app_installed('com.ezxr.unitySDKDemo')
        # print(isAppInstalled)
        # if not isAppInstalled:
        #     self.driver.install_app(app)

    #每次方法之后执行
    def tearDown(self):
        self.driver.quit()

    # @unittest.skip('miss')
    def test_1(self):
        '''sdk打开无闪退'''
        time.sleep(2)
        try:
            el1 = self.driver.find_element_by_id(f"{self.packname}:id/arOasisLayout")
            # el1 = self.driver.find_element_by_id("com.ezxr.unitySDKDemo:id/arOasisLayout")
            el1.click()
            time.sleep(3)
            self.driver.back()
            # self.driver.back()
        except Exception:
            print('没有找到el')
            pass
        time.sleep(3.5)
        # 校验已经返回到主页面，通过校验应用名
        name = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.TextView")
        self.assertEqual(name.text, '洞见AR-World UnitySDK')

    # @unittest.skip('miss')
    def test_2(self):
        '''打开应用，重复锁屏n次每次2s再唤到前台'''
        time.sleep(2)
        for i in range(2):
            self.driver.lock()
            time.sleep(2)
            self.driver.unlock()
        name = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.TextView")
        self.assertEqual(name.text, '洞见AR-World UnitySDK')

    # @unittest.skip('miss')
    def test_3(self):
        '''内容开发调试，无本地资源'''
        time.sleep(2)
        el2 = self.driver.find_element_by_id(f"{self.packname}:id/utArContentDebugRl")
        el2.click()
        time.sleep(1)
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.TextView")
        el3.click()
        time.sleep(1)
        #通过截图与预设图片对比判断
        # self.driver.get_screenshot_as_file('images/test_3.png')
        # self.assertTrue(similar.similar('images/test_3.png','images/test_3_expect.png'))
        #抓取toast信息
        # print(self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'Clicked popup')]").text)
        toast = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        self.assertEqual(toast, '路径下未找到相关AR资源')

    # @unittest.skip('miss')
    def test_4(self):
        '''验证删除本地指定资源，并验证能成功下载'''
        el1 = self.driver.find_element_by_id(f"{self.packname}:id/arToolboxRL")
        el1.click()
        time.sleep(1)
        el2 = self.driver.find_element_by_id(f"{self.packname}:id/rl_fun_test")
        el2.click()
        time.sleep(1)
        el3 = self.driver.find_element_by_id(f"{self.packname}:id/pidInputET")
        el3.click()
        time.sleep(2)
        el3.send_keys("576")
        el4 = self.driver.find_element_by_id(f"{self.packname}:id/btnCheckLocalEventExist")
        el4.click()
        name = self.driver.find_element_by_id(f"{self.packname}:id/tvCheckLocalEventExist")
        # self.assertEqual(name.text, '不存在该cid资源')
        self.driver.hide_keyboard()
        #删除该资源
        el6 = self.driver.find_element_by_id(f"{self.packname}:id/btnDeleteLocalEvent")
        el6.click()
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(2)
        el7 = self.driver.find_element_by_id(f"{self.packname}:id/arOasisLayout")
        el7.click()
        time.sleep(5)
        el8 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout/android.widget.ImageView[2]")
        el8.click()
        time.sleep(5)
        self.driver.get_screenshot_as_file('images/test_4.png')

    # @unittest.skip('miss')
    def test_5(self):
        '''略'''
        pass

    # @unittest.skip('miss')
    def test_6(self):
        '''验证拍照录制按钮'''
        el1 = self.driver.find_element_by_id(f"{self.packname}:id/arOasisLayout---")
        el1.click()
        pass

"""以下为测试部分框架功能"""
class Test2(unittest.TestCase):
    # @unittest.skip('miss')
    # @classmethod
    # def setUpClass(self):
    #     print('仅运行1次前')
    def setUp(self):
        print("case start...")

    def tearDown(self):
        print("case end...")

    def test_1(self):
        '''测试'''
        result = 6 + 6
        self.assertEqual(result, 12)
        print('test_1')

    a = 1
    b = 2
    @unittest.skipUnless(a==b,"条件成立时执行")
    def test_2(self):
        '''测试'''
        result = 1 + 1
        self.assertEqual(result, 2)
        print('test_2')

class Test3(unittest.TestCase):
    # @unittest.skip('miss')
    def test_3(self):
        '''测试'''
        result = 6 + 6
        self.assertEqual(result, 12)
        print('test_3')

    @classmethod
    def setUpClass(self):
        print('class start ...')

    @classmethod
    def tearDownClass(self):
        print('class end ...')

if __name__ == '__main__':
    """以下仅为测试用"""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test2))
    suite.addTest(unittest.makeSuite(Test3))
    # suite.addTest(Test2('test_1')) #单独只加测试类中的某个测试方法
    runner = unittest.TextTestRunner()
    runner.run(suite)

    # unittest.main() #单独运行

    """运行用例集并将结果以报告html的形式发送至指定企业微信群组内"""
    # t = time.strftime("%Y年%m月%d日%H:%M:%S", time.localtime())
    # reportname = f'安卓sdk_{t}'
    # #生成报告模式运行
    # suite = unittest.TestSuite()  # 定义一个测试集合
    # suite.addTest(unittest.makeSuite(Test))  # 把写的用例加进来（将TestCalc类）加进来
    # run = bf(suite)  # 实例化BeautifulReport模块
    # run.report(filename=reportname, description='UnitySDK安卓自动化测试')
    # dirpath = os.getcwd()
    # # send_file(file=f'{dirpath}/{reportname}.html', key='55001425-cf1d-4355-ba9e-c5d137bf6741') #qa群
    # send_file(file=f'{dir}/{reportname}.html',key='f4b5ffa6-8412-47ed-9c7d-b0c6b22167e8') #吃饭群

    # mytest = Test()
    # mytest.setUp()
    # # mytest.test_1()
    # mytest.test_1
    # mytest.tearDown()
