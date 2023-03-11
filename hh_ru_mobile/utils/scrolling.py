from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


def scroll_to(type_selector: MobileBy, from_selector: str, x: int, y: int):
    # ура рабортает

    wait = WebDriverWait(browser.driver, 10)
    element = wait.until(
        EC.visibility_of_element_located((type_selector, from_selector)))

    action = TouchAction(browser.driver)
    action.press(element).move_to(x=x, y=y).release().perform()
