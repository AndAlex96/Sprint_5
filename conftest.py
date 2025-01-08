from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import random
import string


# Фикстура для перехода к форме регистрации регистрации
@pytest.fixture
def setup_registration():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/header/nav/a")))
    driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a").click() # Кнопка Личный кабинет
    driver.find_element(By.XPATH, ".//div/main/div/div/p[1]/a").click() # Кнопка зарегистрироваться
    yield driver
    driver.quit()

# Фикстура для создания рандомного email
@pytest.fixture
def random_email():
    def generate_email():
        length_before_domain = 15 - len("yandex.ru")
        prefix = ''.join(random.choices(string.ascii_letters + string.digits, k=length_before_domain))
        email = f"{prefix}@yandex.ru"
        return email

    return generate_email

