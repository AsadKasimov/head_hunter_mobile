import time

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser

def skip_login():
    with allure.step('Закрыть окно авторизации'):
        time.sleep(2)
        browser.element(
            (AppiumBy.ID, "ru.hh.android:id/fragment_intentions_onboarding_choose_direction_image_close")).click()
