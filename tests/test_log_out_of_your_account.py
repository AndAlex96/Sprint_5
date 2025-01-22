import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LocatorsSite


# выход из профиля
class Test_log_out_of_your_account:
    def test_transfer_to_personal_account(self, setup_registration, random_email):
        driver = setup_registration
        r_random_email = random_email()
        driver.find_element(By.XPATH, LocatorsSite.BUTTON_PERSONAL_ACCOUNT).click()  # Кнопка Личный кабинет
        driver.find_element(By.XPATH, LocatorsSite.BUTTON_REGISRET).click()  # Кнопка зарегистрироваться

        driver.find_element(By.XPATH, LocatorsSite.INPUT_NAME).send_keys("andrey")
        driver.find_element(By.XPATH, LocatorsSite.INPUT_EMAIL).send_keys(r_random_email)
        driver.find_element(By.XPATH, LocatorsSite.INPUT_PASSWORD).send_keys("123456")
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, LocatorsSite.BUTTON_REGISRET_ACCOUNT)))  # ожидаем кликабильности кнопки регистрации
        driver.find_element(By.XPATH, LocatorsSite.BUTTON_REGISRET_ACCOUNT).click()  # зарегистрировали аккаунт

        driver.get("https://stellarburgers.nomoreparties.site/")  # перешли на главную
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
        entrance = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, LocatorsSite.BUTTON_LOGIN_TO_ACCOUNT)))
        entrance.click()  # ждем кликабильности кнопки Войти в аккаунт и нажимаем на нее

        # авторизуемся
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, LocatorsSite.INPUT_EMAIL)))
        driver.find_element(By.XPATH, LocatorsSite.INPUT_EMAIL).send_keys(r_random_email)
        driver.find_element(By.XPATH, LocatorsSite.INPUT_PASSWORD).send_keys("123456")
        driver.find_element(By.XPATH, LocatorsSite.BUTTON_LOGIN).click()  # кнопка Войти

    # проверяем переход в личный кабинет
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))  # Подождали загрузки главной стр сайта
        driver.find_element(By.XPATH, LocatorsSite.BUTTON_PERSONAL_ACCOUNT).click()  # перешли в личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
        driver.find_element(By.XPATH, LocatorsSite.OUT_BUTTON).click() # кнопка Выход
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, LocatorsSite.BUTTON_PERSONAL_ACCOUNT)))
        driver.find_element(By.XPATH, LocatorsSite.BUTTON_PERSONAL_ACCOUNT).click() # проверяем переход в ЛК

        assert driver.current_url != 'https://stellarburgers.nomoreparties.site/account/profile' # проверяем, что после выхода в ЛК нет авторизированного профиля