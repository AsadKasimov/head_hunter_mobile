import allure
from hh_ru_mobile.model.pages import more_vacancy
from hh_ru_mobile.model.controls.skip_login import skip_login


@allure.parent_suite('Mobile')
@allure.suite('Вакансии')
@allure.title(f"Посмотреть больше вакансий без поиска")
def test_more_vacancy():
    skip_login()
    more_vacancy.scroll_to_button()
    more_vacancy.click_button_more()
