import allure
from hh_ru_mobile.model.pages import login
from hh_ru_mobile.model.controls.skip_google_save import skip_google_save

@allure.parent_suite('Mobile')
@allure.suite('Авторизация')
@allure.title(f"Вход с помощью пароля")
def test_login_():
    login.click_login()
    login.click_phonenum_or_email()
    login.set_email()
    login.lofin_by_password()
    login.set_password()
    login.click_button()
    skip_google_save()
