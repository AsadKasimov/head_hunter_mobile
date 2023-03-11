from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selene.support.shared import browser
from hh_ru_mobile.utils import scrolling
import allure


def scroll_to_button():
    with allure.step(f'Скролим до кнопки'):
        scrolling.scroll_to(type_selector=MobileBy.ID,
                            from_selector='ru.hh.android:id/cell_section_header_large_narrow_text_view', x=0, y=-2700)


def click_button_more():
    with allure.step(f'Нажать на кнопку "Еще ......... вакансии"'):
        browser.element((AppiumBy.ID, "ru.hh.android:id/view_hh_button_title_text_view")).click()
