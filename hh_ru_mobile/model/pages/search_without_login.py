import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.conditions import have
from selene.support.shared import browser


def click_search_container():
    with allure.step(f'Кликнуть на поисковое поле'):
        browser.element((AppiumBy.ID, "ru.hh.android:id/view_main_search_container")).click()

def search_query(value):
    with allure.step(f'Ввод в поле: {value}'):
        browser.element((AppiumBy.ID, "ru.hh.android:id/toolbar_search_query")).send_keys(value)
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text(value)).click()

def assert_search_text_position(value):
    with allure.step(f'Проверка поиска'):
        assert browser.element((AppiumBy.ID, 'ru.hh.android:id/view_main_search_text_view_position')).should(
            have.text(value))
