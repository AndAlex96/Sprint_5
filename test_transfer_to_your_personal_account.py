import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# переход в личный кабинет
def test_transfer_to_personal_account(setup_registration, random_email):
    driver = setup_registration
    r_random_email = random_email()
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("andrey")
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(r_random_email)
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys("123456")
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/form/button")))  # ожидаем кликабильности кнопки регистрации
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()  # зарегистрировали аккаунт

    driver.get("https://stellarburgers.nomoreparties.site/")  # перешли на главную
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
    entrance = WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div/div/header/nav/a/p')))
    entrance.click()  # ждем кликабильности кнопки Личный кабинет и нажимаем на нее

    # авторизуемся
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input')))
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input').send_keys(r_random_email)
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/input').send_keys("123456")
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/button').click()  # кнопка Войти

    # проверяем переход в личный кабинет
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div/div/header/nav/a/p')))  # Подождали загрузки кнопки ЛК на главной
    driver.find_element(By.XPATH, '/html/body/div/div/header/nav/a/p').click()  # перешли в личный кабинет
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"