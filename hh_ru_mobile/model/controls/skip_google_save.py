import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.conditions import be
from selene.support.shared import browser


def skip_google_save():
    with allure.step(f'Закрыть окно сохранения логина/пароля'):
        if browser.element((AppiumBy.ID, "android:iнd/autofill_save_no")).matching(be.visible):
            browser.element('#fragment_onboarding_skip_button').tap()
