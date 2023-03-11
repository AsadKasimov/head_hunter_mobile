# import time
# from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver import Remote
# from selene.support.shared import browser
# from appium.webdriver.common.touch_action import TouchAction
# from appium.webdriver.common.mobileby import MobileBy
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# app = './ru.hh.android_7.12_11228.apk'
# appName = 'org.wikipedia.alpha'
# udid = 'aafcd061'
# newCommandTimeout = 1234
#
# desired_caps = {
#     'platformName': 'Android',
#     "app": r"C:\Users\kasim\PycharmProjects\experement_scrolling\ru.hh.android_7.12_11228.apk",
#     "appName": "ru.hh.android",
#     "udid": "aafcd061",
#     "newCommandTimeout": 1234
# }
#
# driver = Remote("http://localhost:4723/wd/hub", desired_caps)
# browser.config.driver = driver
# browser.element((AppiumBy.ID, "ru.hh.android:id/fragment_intentions_onboarding_choose_direction_image_close")).click()
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.visibility_of_element_located((MobileBy.ID, 'ru.hh.android:id/cell_section_header_large_narrow_text_view')))
#
# action = TouchAction(driver)
# action.press(element).move_to(x=0, y=-2700).release().perform()

