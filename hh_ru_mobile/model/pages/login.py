import os
import time
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from selene import have
from selene.support.shared import browser
import allure

load_dotenv()

def click_login():
    with allure.step(f'Нажать на кнопку "У меня есть аккаунт. Войти"'):
        browser.element(
            (AppiumBy.ID, "ru.hh.android:id/fragment_intentions_onboarding_choose_direction_button_new_user")).click()


def click_phonenum_or_email():
    with allure.step(f'Нажать на "По телефону или почте"'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text("По телефону или почте")).click()


def set_email():
    with allure.step(f'Ввод эл-почты'):
        browser.element((AppiumBy.ID, "ru.hh.android:id/view_line_input_edit_text")).send_keys(os.getenv('EMAIL'))


def lofin_by_password():
    with allure.step(f'Нажать "Войти по поролю"'):
        browser.element(
        (AppiumBy.ID, "ru.hh.android:id/fragment_authorization_by_code_text_view_to_login_by_password")).click()


def set_password():
    with allure.step(f'Ввод пароля'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.EditText")).element_by(have.text('Пароль')).send_keys(os.getenv('PASSWORD'))


def click_button():
    with allure.step(f'Нажать "Продолжить"'):
        browser.element((AppiumBy.ID, "ru.hh.android:id/view_title_button_button")).click()
        time.sleep(2)
