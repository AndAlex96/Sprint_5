from doctest import DocTest

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LocatorsSite

class Test_the_constructor_section:
    def test_go_to_the_rolls_section(self, setup_registration):
        driver = setup_registration

        driver.find_element(By.XPATH, LocatorsSite.BUTTON_SAUSES).click() # нажимаем на раздел соусы

        driver.find_element(By.XPATH, LocatorsSite.BUTTON_ROLLS).click()  # нажимаем на раздел булки
        WebDriverWait(driver, 3)
        parent_div = driver.find_element(By.XPATH, LocatorsSite.PARENTS_BUTTON_ROLLS)

        # проверяем класс в выбранном состоянии
        assert parent_div.get_attribute('class') == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"


    def test_go_to_the_sauces_section(self, setup_registration):
        driver = setup_registration

        driver.find_element(By.XPATH, LocatorsSite.BUTTON_SAUSES).click()  # нажимаем на раздел соусы
        WebDriverWait(driver, 3)
        parent_div = driver.find_element(By.XPATH, LocatorsSite.PARENTS_BUTTON_SAUSES)

        assert parent_div.get_attribute(
            'class') == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"


    def test_go_to_the_toppings_section(self, setup_registration):
        driver = setup_registration

        driver.find_element(By.XPATH, LocatorsSite.BUTTON_TOPPINGS).click()  # нажимаем на раздел соусы
        WebDriverWait(driver, 3)
        parent_div = driver.find_element(By.XPATH, LocatorsSite.PARENTS_BUTTON_TOPPINGS)

        assert parent_div.get_attribute(
            'class') == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"



