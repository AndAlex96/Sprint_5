import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# проверка регистрации с корректными данными
def test_registration_with_correct_date(setup_registration, random_email):
    driver = setup_registration
    r_random_email = random_email()
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("andrey")
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(r_random_email)
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys("123456")

    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click() # Кнопка регистрации
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(('https://stellarburgers.nomoreparties.site/login'))) # Ожидаем перехода на страницу авторизации

    email_input = WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input")))
    email_input.send_keys(r_random_email)  # вводим email
    password_input = WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input")))
    password_input.send_keys("123456")  # вводим пароль

    go_in_auth = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/form/button"))) # кнопка Войти
    go_in_auth.click()  # вошли под созданным аккаунтом

    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div/div/header/nav/a/p'))) # Подождали загрузки кнопки ЛК на главной
    driver.find_element(By.XPATH, '/html/body/div/div/header/nav/a/p').click()  # перешли в личный кабинет
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/ul/li[2]/div/div/input"))) # ожидаем видимости поля с логином

    check_email = driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/ul/li[2]/div/div/input")  # нашли поле с логином
    value = check_email.get_attribute('value')  # сохранили значение атрибута

    assert r_random_email.upper() == value.upper() # проверили, что созданный логин совпадает с введенным при регистрации и учитываем возможность расхождения регистра



# проверка ошибки регистрации при вводе некорректного пароля
def test_error_for_incorrect_password(setup_registration, random_email):
    driver = setup_registration
    r_random_email = random_email()
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("andrey")
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys("r_random_email")
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys("123")

    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click() # нажимаем на кнопку регистрации

    assert driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/p").text == "Некорректный пароль" # проверяем наличие уведомления о некорректном пароле
