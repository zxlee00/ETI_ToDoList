import os
import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

def test_login_without_entering_username_or_password():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000')
    time.sleep(1)
    button = driver.find_element_by_tag_name('a')
    button.click()
    button = driver.find_element_by_xpath("//button")
    button.click()
    time.sleep(1)
    assert driver.find_element_by_css_selector("input:invalid")
    driver.quit()
    
def test_login_without_entering_username():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000')
    time.sleep(1)
    button = driver.find_element_by_tag_name('a')
    button.click()

    time.sleep(1)
    password = driver.find_element_by_id('id_password')
    password.send_keys("admin123")
    button = driver.find_element_by_xpath("//button")
    button.click()
    assert driver.find_element_by_css_selector("input:invalid")
    driver.quit()

def test_login_without_entering_password():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000')
    time.sleep(1)
    button = driver.find_element_by_tag_name('a')
    button.click()

    time.sleep(1)
    username = 'admin'
    driver.find_element_by_id('id_username').send_keys(username)
    button = driver.find_element_by_xpath("//button")
    button.click()
    time.sleep(2)
    assert driver.find_element_by_css_selector("input:invalid")
    driver.quit()

def test_login_with_incorrect_username():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000')
    time.sleep(1)
    button = driver.find_element_by_tag_name('a')
    button.click()

    time.sleep(1)
    username = 'admin?'
    driver.find_element_by_id('id_username').send_keys(username)
    password = driver.find_element_by_id('id_password')
    password.send_keys("admin123")
    button = driver.find_element_by_xpath("//button")
    button.click()
    time.sleep(2)
    assert "The username or password you have entered is incorrect, please try again." in driver.page_source
    driver.quit()

def test_login_with_incorrect_password():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000')
    time.sleep(1)
    button = driver.find_element_by_tag_name('a')
    button.click()

    time.sleep(1)
    username = 'admin'
    driver.find_element_by_id('id_username').send_keys(username)
    password = driver.find_element_by_id('id_password')
    password.send_keys("admin123?")
    button = driver.find_element_by_xpath("//button")
    button.click()
    time.sleep(2)
    assert "The username or password you have entered is incorrect, please try again." in driver.page_source
    driver.quit()

def test_successful_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000')
    time.sleep(1)
    button = driver.find_element_by_tag_name('a')
    button.click()

    time.sleep(2)
    username = 'admin'
    driver.find_element_by_id('id_username').send_keys(username)
    password = driver.find_element_by_id('id_password')
    password.send_keys("admin123")
    button = driver.find_element_by_xpath("//button")
    button.click()
    time.sleep(2)
    assert "You are logged in as " + username + "." in driver.page_source
    driver.quit()
    
def test_navigation_to_login_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000')
    assert "You are not logged in." in driver.page_source

    time.sleep(2)
    button = driver.find_element_by_tag_name('a')
    button.click()
    time.sleep(2)
    assert "Login" in driver.page_source
    driver.quit()

def test_logout():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000')
    time.sleep(1)
    button = driver.find_element_by_tag_name('a')
    button.click()

    time.sleep(2)
    username = 'admin'
    driver.find_element_by_id('id_username').send_keys(username)
    password = driver.find_element_by_id('id_password')
    password.send_keys("admin123")
    button = driver.find_element_by_xpath("//button")
    button.click()
    
    logout = driver.find_element_by_tag_name('a')
    logout.click()
    time.sleep(2)
    assert "You are not logged in." in driver.page_source
    driver.quit()
