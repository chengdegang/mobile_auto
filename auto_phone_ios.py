import time

from appium import webdriver
import unittest

class TestMethod(unittest.TestCase):
    #每次方法之前执行
    def setUp(self):
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

    #每次方法之后执行
    def tearDown(self):
        self.driver.quit()

    #点击绿洲大场景，在返回到主页，
    def test_1(self):
        time.sleep(2)
        try:
            # flag = True
            el3 = self.driver.find_element_by_id("com.ezxr.unitySDKDemo:id/arOasisLayout")
        except Exception:
            print('没有找到el3')
        el3.click()
        time.sleep(3)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        # 校验已经返回到主页面，通过校验应用名
        name = self.driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="AR-World UnitySDK"]/android.widget.TextView')
        self.assertEqual(name.text,'AR-World UnitySDK')

    def test_2(self):
        1
        # print('用例2执行完成')

if __name__ == '__main__':

    unittest.main()