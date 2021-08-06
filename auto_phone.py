import time
from appium import webdriver
import unittest

class Test(unittest.TestCase):
    #每次方法之前执行
    def setUp(self):
        # app = '/Users/jackrechard/Desktop/appium/app-OasisTest-debug.apk'
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "98895a384b33433756",
            "appPackage": "com.ezxr.unitySDKDemo",
            "appActivity": "com.netease.arinsightsdk.SplashActivity",
            'noReset': True
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(2)
        # isAppInstalled = self.driver.is_app_installed('com.ezxr.unitySDKDemo')
        # print(isAppInstalled)
        # if not isAppInstalled:
        #     self.driver.install_app(app)

    #每次方法之后执行
    def tearDown(self):
        self.driver.quit()

    #点击绿洲大场景，在返回到主页，
    def test_1(self):
        time.sleep(2)
        try:
            el3 = self.driver.find_element_by_id("com.ezxr.unitySDKDemo:id/arOasisLayout")
            el3.click()
            time.sleep(3)
            self.driver.back()
            time.sleep(1)
            self.driver.back()
        except Exception:
            print('没有找到el3')
            pass
        # 校验已经返回到主页面，通过校验应用名
        name = self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[@content-desc="AR-World UnitySDK"]/android.widget.TextView')
        self.assertEqual(name.text, 'AR-World UnitySDK')

    @unittest.skip('miss')
    #打开应用，重复锁屏n次每次2s再唤到前台
    def test_2(self):
        time.sleep(2)
        for i in range(2):
            self.driver.lock()
            time.sleep(2)
            self.driver.unlock()
        name = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.TextView")
        self.assertEqual(name.text, '洞见AR-World UnitySDK')

    #内容开发调试，无本地资源
    def test_3(self):
        el2 = self.driver.find_element_by_id("com.ezxr.unitySDKDemo:id/utArContentDebugRl")
        el2.click()
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.TextView")
        el3.click()
        time.sleep(2)

if __name__ == '__main__':

    unittest.main()

    # mytest = Test()
    # mytest.setUp()
    # mytest.test_2(locknum=2)