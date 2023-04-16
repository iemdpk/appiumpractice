# Android environment
import unittest
from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy 

desired_caps = dict(
    platformName='Android',
    deviceName='261f61db',
    appPackage='org.telegram.messenger',
    appActivity='org.telegram.ui.LaunchActivity'
)



driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(4)
print("This is Done")

# driver.find_elements(By.xpath("//android.widget.TextView 2[@content-desc=‘Start Messaging’]")).click();

# element = driver.find_element(by=MobileBy.XPATH, value="//android.widget.TextView 2[@text='Start Messaging']")
element = driver.find_element(by=MobileBy.XPATH, value="//android.widget.TextView[@text='Start Messaging']")
element.click()
# element = driver.find_element(MobileBy.NAME, "Start Messaging").click()
