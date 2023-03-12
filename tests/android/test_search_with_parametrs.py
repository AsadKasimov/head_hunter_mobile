import allure
from hh_ru_mobile.model.controls.skip_login import skip_login
from hh_ru_mobile.model.pages import search_with_parametrs


@allure.parent_suite('Mobile')
@allure.suite('Поиск с авторизацией')
@allure.title(f"Поиск с параметрами")
def test_search_with_parametrs():
    skip_login()
    search_with_parametrs.click_button_filters()
    search_with_parametrs.set_search_word('Тестировщик')
    search_with_parametrs.search_by_name()
    search_with_parametrs.set_search_zone('Московская область')
    search_with_parametrs.set_specialization('Тестировщик')
    search_with_parametrs.click_submit()
