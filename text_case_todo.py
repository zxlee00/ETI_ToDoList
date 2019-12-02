import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

def test_toDoNavigate():
    driver.get('http://localhost:8000/accounts/login/')
    userelem = driver.find_element_by_name("username")
    userelem.clear()
    userelem.send_keys("admin")
    userelem.send_keys(Keys.RETURN)
    pswdelem = driver.find_element_by_name("password")
    pswdelem.clear()
    pswdelem.send_keys("administrator")
    pswdelem.send_keys(Keys.RETURN)

    driver.refresh()
    driver.find_element_by_xpath('//a[@href="'+"/ToDo/"+'"]').click()
    assert "ToDo" in driver.page_source
    driver.quit()

def test_submitEmpty():
    driver.get('http://localhost:8000/accounts/login/')
    userelem = driver.find_element_by_name("username")
    userelem.clear()
    userelem.send_keys("admin")
    userelem.send_keys(Keys.RETURN)
    pswdelem = driver.find_element_by_name("password")
    pswdelem.clear()
    pswdelem.send_keys("administrator")
    pswdelem.send_keys(Keys.RETURN)

    driver.refresh()
    driver.find_element_by_xpath('//a[@href="'+"/ToDo/"+'"]').click()

    time.sleep(1)
    todo = driver.find_element_by_xpath('//*[@id="todotext"]')
    todo.send_keys("")
    todo.send_keys(Keys.RETURN)

    error = driver.find_element_by_xpath("//*[contains(text(), 'To submit, please fill in the textfield!')]"
    assert error.is_displayed() for True
    driver.quit()

def test_textSubmit():
    driver.get('http://localhost:8000/accounts/login/')
    userelem = driver.find_element_by_name("username")
    userelem.clear()
    userelem.send_keys("admin")
    userelem.send_keys(Keys.RETURN)
    pswdelem = driver.find_element_by_name("password")
    pswdelem.clear()
    pswdelem.send_keys("administrator")
    pswdelem.send_keys(Keys.RETURN)

    driver.refresh()
    driver.find_element_by_xpath('//a[@href="'+"/ToDo/"+'"]').click()

    time.sleep(1)
    todo = driver.find_element_by_xpath('//*[@id="todotext"]')
    todo.send_keys("Please go to ETI")
    todo.send_keys(Keys.RETURN)

    error = driver.find_element_by_xpath("//*[contains(text(), 'To submit, please fill in the textfield!')]"
    assert! error.is_displayed() for False
    driver.quit()

def test_toDoArchive():
    driver.get('http://localhost:8000/accounts/login/')
    userelem = driver.find_element_by_name("username")
    userelem.clear()
    userelem.send_keys("admin")
    userelem.send_keys(Keys.RETURN)
    pswdelem = driver.find_element_by_name("password")
    pswdelem.clear()
    pswdelem.send_keys("administrator")
    pswdelem.send_keys(Keys.RETURN)

    driver.refresh()
    driver.find_element_by_name("archive").click()
    driver.quit()

def test_toDoDelete():
    driver.get('http://localhost:8000/accounts/login/')
    userelem = driver.find_element_by_name("username")
    userelem.clear()
    userelem.send_keys("admin")
    userelem.send_keys(Keys.RETURN)
    pswdelem = driver.find_element_by_name("password")
    pswdelem.clear()
    pswdelem.send_keys("administrator")
    pswdelem.send_keys(Keys.RETURN)

    driver.refresh()
    driver.find_element_by_name("delete").click()
    driver.quit()
    
