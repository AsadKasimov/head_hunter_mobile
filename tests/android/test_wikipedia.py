import time
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selene import have
from selene.support.conditions import be
from selene.support.shared import browser
from hh_ru_mobile.utils import scrolling


def test_login():
    browser.element(
        (AppiumBy.ID, "ru.hh.android:id/fragment_intentions_onboarding_choose_direction_button_new_user")).click()
    browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text("По телефону или почте")).click()
    browser.element((AppiumBy.ID, "ru.hh.android:id/view_line_input_edit_text")).send_keys('animeklan45@gmail.com')
    browser.element(
        (AppiumBy.ID, "ru.hh.android:id/fragment_authorization_by_code_text_view_to_login_by_password")).click()
    browser.all((AppiumBy.CLASS_NAME, "android.widget.EditText")).element_by(have.text('Пароль')).send_keys('abdullohloh')
    browser.element((AppiumBy.ID, "ru.hh.android:id/view_title_button_button")).click()
    time.sleep(2)
    # это на скип окна сохранение данных т.е. пароль, логин
    if browser.element((AppiumBy.ID, "android:id/autofill_save_no")).matching(be.visible):
        browser.element('#fragment_onboarding_skip_button').tap()


def test_search_without_login():
    browser.element(
        (AppiumBy.ID, "ru.hh.android:id/fragment_intentions_onboarding_choose_direction_image_close")).click()
    browser.element((AppiumBy.ID, "ru.hh.android:id/view_main_search_container")).click()
    browser.element((AppiumBy.ID, "ru.hh.android:id/toolbar_search_query")).send_keys('Тестировщик')
    browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text('Тестировщик')).click()
    assert browser.element((AppiumBy.ID, 'ru.hh.android:id/view_main_search_text_view_position')).should(
        have.text('Тестировщик'))


def test_more_vacancy():
    browser.element(
        (AppiumBy.ID, "ru.hh.android:id/fragment_intentions_onboarding_choose_direction_image_close")).click()
    scrolling.scroll_to(type_selector=MobileBy.ID, from_selector='ru.hh.android:id/cell_section_header_large_narrow_text_view', x=0, y=-2700)
    browser.element((AppiumBy.ID, "ru.hh.android:id/view_hh_button_title_text_view")).click()


def test_search_browser():
    browser.config.wait(3000000)
