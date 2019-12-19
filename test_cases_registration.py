import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_navigation_to_Registration_Page():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('http://localhost:8000/accounts/login/')
    registrationButton = driver.find_element_by_link_text('Register')
    registrationButton.click()
    assert "Sign Up" in driver.page_source
    driver.quit()
    
def test_registration_with_username_not_meeting_requirements():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('http://localhost:8000/accounts/login/')
    registrationButton = driver.find_element_by_link_text('Register')
    registrationButton.click()

    userelem = driver.find_element_by_id("id_username")
    userelem.clear()
    userelem.send_keys("ETI testuser")

    pswdelem = driver.find_element_by_id("id_password1")
    pswdelem.clear()
    pswdelem.send_keys("P@ssw0rdeti")

    confirmpswdelem = driver.find_element_by_id("id_password2")
    confirmpswdelem.clear()
    confirmpswdelem.send_keys("P@ssw0rdeti")

    signUpButton = driver.find_element_by_xpath("//button")
    signUpButton.click()

    time.sleep(2)
    assert "Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters." in driver.page_source
    driver.quit()
    
def test_registration_with_password_not_meeting_requirements():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('http://localhost:8000/accounts/login/')
    registrationButton = driver.find_element_by_link_text('Register')
    registrationButton.click()

    userelem = driver.find_element_by_id("id_username")
    userelem.clear()
    userelem.send_keys("etitestuser1")

    pswdelem = driver.find_element_by_id("id_password1")
    pswdelem.clear()
    pswdelem.send_keys("admin")

    confirmpswdelem = driver.find_element_by_id("id_password2")
    confirmpswdelem.clear()
    confirmpswdelem.send_keys("admin")

    signUpButton = driver.find_element_by_xpath("//button")
    signUpButton.click()

    time.sleep(2)
    assert "This password is too short. It must contain at least 8 characters." in driver.page_source
    assert "This password is too common." in driver.page_source
    
    driver.quit() 

def test_registration_with_empty_username():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('http://localhost:8000/accounts/login/')
    registrationButton = driver.find_element_by_link_text('Register')
    registrationButton.click()

    pswdelem = driver.find_element_by_id("id_password1")
    pswdelem.clear()
    pswdelem.send_keys("P@ssw0rdeti")

    confirmpswdelem = driver.find_element_by_id("id_password2")
    confirmpswdelem.clear()
    confirmpswdelem.send_keys("P@ssw0rdeti")

    signUpButton = driver.find_element_by_xpath("//button")
    signUpButton.click()

    time.sleep(2)
    assert driver.find_element_by_css_selector("input:invalid")
    driver.quit()

def test_registration_with_empty_password():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('http://localhost:8000/accounts/login/')
    registrationButton = driver.find_element_by_link_text('Register')
    registrationButton.click()

    userelem = driver.find_element_by_id("id_username")
    userelem.clear()
    userelem.send_keys("etitestuser1")

    confirmpswdelem = driver.find_element_by_id("id_password2")
    confirmpswdelem.clear()
    confirmpswdelem.send_keys("P@ssw0rdeti")

    signUpButton = driver.find_element_by_xpath("//button")
    signUpButton.click()

    time.sleep(2)
    assert driver.find_element_by_css_selector("input:invalid")
    driver.quit()

def test_registration_with_empty_confirm_password():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('http://localhost:8000/accounts/login/')
    registrationButton = driver.find_element_by_link_text('Register')
    registrationButton.click()

    userelem = driver.find_element_by_id("id_username")
    userelem.clear()
    userelem.send_keys("etitestuser1")

    pswdelem = driver.find_element_by_id("id_password1")
    pswdelem.clear()
    pswdelem.send_keys("P@ssw0rdeti")

    signUpButton = driver.find_element_by_xpath("//button")
    signUpButton.click()

    time.sleep(2)
    assert driver.find_element_by_css_selector("input:invalid")
    driver.quit()

def test_validation_when_passwords_do_not_match():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('http://localhost:8000/accounts/login/')
    registrationButton = driver.find_element_by_link_text('Register')
    registrationButton.click()

    userelem = driver.find_element_by_id("id_username")
    userelem.clear()
    userelem.send_keys("etitestuser1")

    pswdelem = driver.find_element_by_id("id_password1")
    pswdelem.clear()
    pswdelem.send_keys("P@ssw0rdeti1")

    confirmpswdelem = driver.find_element_by_id("id_password2")
    confirmpswdelem.clear()
    confirmpswdelem.send_keys("P@ssw0rdeti2")

    signUpButton = driver.find_element_by_xpath("//button")
    signUpButton.click()

    time.sleep(2)
    assert "The two password fields didn't match." in driver.page_source
    driver.quit()

def test_successful_registration():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('http://localhost:8000/accounts/login/')
    registrationButton = driver.find_element_by_link_text('Register')
    registrationButton.click()

    userelem = driver.find_element_by_id("id_username")
    userelem.clear()
    userelem.send_keys("etitestuser1")

    pswdelem = driver.find_element_by_id("id_password1")
    pswdelem.clear()
    pswdelem.send_keys("P@ssw0rdeti")

    confirmpswdelem = driver.find_element_by_id("id_password2")
    confirmpswdelem.clear()
    confirmpswdelem.send_keys("P@ssw0rdeti")

    signUpButton = driver.find_element_by_xpath("//button")
    signUpButton.click()

    time.sleep(2)
    assert "Login" in driver.page_source
    driver.quit()

def test_registration_with_existing_username():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('http://localhost:8000/accounts/login/')
    registrationButton = driver.find_element_by_link_text('Register')
    registrationButton.click()

    userelem = driver.find_element_by_id("id_username")
    userelem.clear()
    userelem.send_keys("etitestuser1")

    pswdelem = driver.find_element_by_id("id_password1")
    pswdelem.clear()
    pswdelem.send_keys("P@ssw0rdeti")

    confirmpswdelem = driver.find_element_by_id("id_password2")
    confirmpswdelem.clear()
    confirmpswdelem.send_keys("P@ssw0rdeti")

    signUpButton = driver.find_element_by_xpath("//button")
    signUpButton.click()

    time.sleep(2)
    assert "A user with that username already exists." in driver.page_source
    driver.quit()
