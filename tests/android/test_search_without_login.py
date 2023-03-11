import allure
from hh_ru_mobile.model.pages import search_without_login
from hh_ru_mobile.model.controls.skip_login import skip_login


@allure.parent_suite('Mobile')
@allure.suite('Поиск')
@allure.title(f"Поиск с параметрами")
def test_search_without_login():
    skip_login()
    search_without_login.click_search_container()
    search_without_login.search_query('Тестировщик')
    search_without_login.assert_search_text_position('Тестировщик')
