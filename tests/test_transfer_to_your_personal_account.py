import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LocatorsSite

# переход в личный кабинет
class Test_transfer_to_personal_account:
    def test_transfer_to_personal_account_to_click_on_button_persaccount(self, setup_registration, random_email):
        driver = setup_registration
        r_random_email = random_email()
        driver.find_element(By.XPATH, LocatorsSite.BUTTON_PERSONAL_ACCOUNT).click()  # Кнопка Личный кабинет
        driver.find_element(By.XPATH, LocatorsSite.BUTTON_REGISRET).click()  # Кнопка зарегистрироваться

        driver.find_element(By.XPATH, LocatorsSite.INPUT_NAME).send_keys("andrey")
        driver.find_element(By.XPATH, LocatorsSite.INPUT_EMAIL).send_keys(r_random_email)
        driver.find_element(By.XPATH, LocatorsSite.INPUT_PASSWORD).send_keys("123456")
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, LocatorsSite.BUTTON_REGISRET_ACCOUNT)))  # ожидаем кликабильности кнопки регистрации
        driver.find_element(By.XPATH, LocatorsSite.BUTTON_REGISRET_ACCOUNT).click()  # зарегистрировали аккаунт

        driver.get("https://stellarburgers.nomoreparties.site/")  # перешли на главную
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
        entrance = WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, LocatorsSite.BUTTON_PERSONAL_ACCOUNT)))
        entrance.click()  # ждем кликабильности кнопки Личный кабинет и нажимаем на нее

        # авторизуемся
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, LocatorsSite.INPUT_EMAIL)))
        driver.find_element(By.XPATH, LocatorsSite.INPUT_EMAIL).send_keys(r_random_email)
        driver.find_element(By.XPATH, LocatorsSite.INPUT_PASSWORD).send_keys("123456")
        driver.find_element(By.XPATH, LocatorsSite.BUTTON_LOGIN).click()  # кнопка Войти

        # проверяем вход в аккаунт в личном кабинете
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))  # Подождали загрузки главной стр сайта
        driver.find_element(By.XPATH, LocatorsSite.BUTTON_PERSONAL_ACCOUNT).click()  # перешли в личный кабинет
        check_email = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, LocatorsSite.INPUT_LOGIN)))  # ожидаем видимости поля с логином и сохраняем в переменную
        value = check_email.get_attribute('value')  # сохранили значение атрибута

        assert r_random_email.upper() == value.upper()  # проверили, что созданный логин совпадает с введенным при регистрации и учитываем возможность расхождения регистра