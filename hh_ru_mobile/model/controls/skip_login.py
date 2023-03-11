from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser

def skip_login():

    browser.element(
        (AppiumBy.ID, "ru.hh.android:id/fragment_intentions_onboarding_choose_direction_image_close")).click()
