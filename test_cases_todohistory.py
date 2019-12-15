import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_navigation_to_todohistory_page():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('http://localhost:8000/accounts/login/')
    userelem = driver.find_element_by_id("id_username")
    userelem.clear()
    userelem.send_keys("admin")
    userelem.send_keys(Keys.RETURN)
    pswdelem = driver.find_element_by_id("id_password")
    pswdelem.clear()
    pswdelem.send_keys("admin123")
    pswdelem.send_keys(Keys.RETURN)

    driver.find_element_by_xpath('//a[@href="'+"/todoHistory/"+'"]').click()
    assert "To-Do List History" in driver.page_source
    driver.quit()

def test_successful_archive_into_todo_history_page():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('http://localhost:8000/accounts/login/')
    userelem = driver.find_element_by_id("id_username")
    userelem.clear()
    userelem.send_keys("admin")
    userelem.send_keys(Keys.RETURN)
    pswdelem = driver.find_element_by_id("id_password")
    pswdelem.clear()
    pswdelem.send_keys("admin123")
    pswdelem.send_keys(Keys.RETURN)

    time.sleep(1)
    todo = driver.find_element_by_name("content")
    todo.send_keys("Item to be archived")
    todo.send_keys(Keys.RETURN)

    time.sleep(1)
    
    todoItemToArchive = driver.find_element_by_xpath("//li[contains(text(),'Item to be archived')]")
    items = driver.find_elements_by_tag_name("li")
    count = 0
    for element in items:
        if element == todoItemToArchive:
            indexToArchive = count
        count += 1

    archive_btns = driver.find_elements_by_xpath("//button[contains(text(),' Archive to History ')]")
    archive_btns[indexToArchive].click()

    time.sleep(1)

    driver.find_element_by_xpath('//a[@href="'+"/todoHistory/"+'"]').click()

    assert "Item to be archived" in driver.page_source

    driver.quit()
