import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LocatorsSite

# переход в конструктор из личного кабинета по клику на Конструктор
class Test_switching_to_the_constructor:
    def test_transfer_to_constructor_by_clicking_on_contructor_button(self, setup_registration, random_email):
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
        entrance = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, LocatorsSite.BUTTON_PERSONAL_ACCOUNT)))
        entrance.click()  # ждем кликабильности кнопки Личный кабинет и нажимаем на нее

        # авторизуемся
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, LocatorsSite.INPUT_EMAIL)))
        driver.find_element(By.XPATH, LocatorsSite.INPUT_EMAIL).send_keys(r_random_email)
        driver.find_element(By.XPATH, LocatorsSite.INPUT_PASSWORD).send_keys("123456")
        driver.find_element(By.XPATH, LocatorsSite.BUTTON_LOGIN).click()  # кнопка Войти

        entrance = WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, LocatorsSite.BUTTON_PERSONAL_ACCOUNT)))
        entrance.click()  # ждем кликабильности кнопки Личный кабинет и нажимаем на нее

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
        driver.find_element(By.XPATH, LocatorsSite.BUTTON_CONSTRUCTOR).click() # нажали на кномку Конструктор
        constructor_element = driver.find_element(By.XPATH, LocatorsSite.LOGO_COLLECT_BURGER) # находим Соберите бургер
        assert constructor_element is not None # проверяем его наличие на странице

# переход в конструктор из личного кабинета по клику на логотип Stellar Burgers
    def test_transfer_to_constructor_by_clicking_on_logo_stellar_burgers(self, setup_registration, random_email):
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
        entrance = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, LocatorsSite.BUTTON_PERSONAL_ACCOUNT)))
        entrance.click()  # ждем кликабильности кнопки Личный кабинет и нажимаем на нее

        # авторизуемся
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, LocatorsSite.INPUT_EMAIL)))
        driver.find_element(By.XPATH, LocatorsSite.INPUT_EMAIL).send_keys(r_random_email)
        driver.find_element(By.XPATH, LocatorsSite.INPUT_PASSWORD).send_keys("123456")
        driver.find_element(By.XPATH, LocatorsSite.BUTTON_LOGIN).click()  # кнопка Войти

        entrance = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, LocatorsSite.BUTTON_PERSONAL_ACCOUNT)))
        entrance.click()  # ждем кликабильности кнопки Личный кабинет и нажимаем на нее

        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
        driver.find_element(By.XPATH, LocatorsSite.LOGO_BURGER).click()  # нажали на логотип Stellar Burgers
        constructor_element = driver.find_element(By.XPATH, LocatorsSite.LOGO_COLLECT_BURGER)  # находим Соберите бургер
        assert constructor_element is not None  # проверяем его наличие на странице


