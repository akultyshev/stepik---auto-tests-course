from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, ".form-group #input_value").text
    y = calc(x)

    answer_text_elt = browser.find_element(By.CSS_SELECTOR, ".form-group #answer")
    answer_text_elt.send_keys(y)

    robot_checkbox_elt = browser.find_element(By.CSS_SELECTOR, ".form-check-custom [for='robotCheckbox']")
    robot_checkbox_elt.click()

    robot_radio_elt = browser.find_element(By.CSS_SELECTOR, ".form-radio-custom [for='robotsRule']")
    robot_radio_elt.click()

    button_elt = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_elt.click()
except Exception as ex:
    print(ex)
finally:
    time.sleep(10)
    browser.quit()
