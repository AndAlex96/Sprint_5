import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_go_to_the_rolls_section():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[3]").click() # раздел начинки в заголовке

    driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[1]").click() # возврат к разделу булки
    rolls = driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[2]/ul[1]")
    assert rolls.is_displayed() # проверка видимости элементов раздела

    driver.quit()


def test_go_to_the_sauces_section():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[2]").click()  # раздел соусы в заголовке
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[2]")))

    sauces = driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[2]/ul[2]")
    assert sauces.is_displayed()  # проверка видимости элементов раздела

    driver.quit()


def test_go_to_the_toppings_section():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[3]").click()  # раздел начинки в заголовке
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[3]")))

    toppings = driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[2]/ul[3]")
    assert toppings.is_displayed() # проверка видимости элементов раздела

    driver.quit()

