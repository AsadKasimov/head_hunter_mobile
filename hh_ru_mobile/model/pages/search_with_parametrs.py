from appium.webdriver.common.appiumby import AppiumBy
from selene.support.conditions import have
from selene.support.shared import browser
import allure

def click_button_filters():
    with allure.step(f'Нажать кнопку поиска по фильтрам'):
        browser.element(
            (AppiumBy.ID, "ru.hh.android:id/view_main_search_image_button_filters")).click()

def set_search_word(value):
    with allure.step(f'Ввод профессии в поле: {value}'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text('Должность, ключевые слова')).click()
        browser.element((AppiumBy.ID, 'ru.hh.android:id/toolbar_search_query')).send_keys(value)
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(
            have.text(value)).click()

def search_by_name():
    with allure.step(f'Поиск по названии вакансии'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.CompoundButton")).element_by(
            have.text('В названии вакансии')).click()

def set_search_zone(value):
    with allure.step(f'Добавить регион поиска: {value}'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(
            have.text('Добавить регион')).click()
        browser.element((AppiumBy.ID, 'ru.hh.android:id/fragment_suggest_list_edit_text_search')).send_keys(value)
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(
            have.text(value)).click()
        browser.element((AppiumBy.ID, 'ru.hh.android:id/fragment_suggest_list_button_done')).click()

def set_specialization(value):
    with allure.step(f'Добавить специализацию: {value}'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(
            have.text('Добавить специализацию')).click()
        browser.element((AppiumBy.ID, 'ru.hh.android:id/fragment_suggest_professional_category_edit_text_search')).send_keys(value)
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(
            have.text(value)).click()
        browser.element((AppiumBy.ID, 'ru.hh.android:id/fragment_suggest_professional_category_button_done')).click()

def click_submit():
    with allure.step(f'Нажать на поиск'):
        browser.element((AppiumBy.ID, "ru.hh.android:id/fragment_search_filters_button_apply")).click()
