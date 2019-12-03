import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_navigation_to_todo_page():
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

    driver.refresh()
    driver.find_element_by_xpath('//a[@href="'+"/todo/"+'"]').click()
    assert "To-Do" in driver.page_source
    driver.quit()

def test_adding_a_todo_item():
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
    todo.send_keys("Testing to-do item")
    todo.send_keys(Keys.RETURN)

    time.sleep(1)

    assert driver.find_element_by_xpath("//li[contains(text(),'Testing to-do item')]")
    
    driver.quit()

def test_adding_a_todo_item_without_a_value():
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
    todo.send_keys(Keys.RETURN)

    time.sleep(1)

    assert todo.get_attribute("validationMessage") == "Please fill out this field."
    
    driver.quit()

def test_deleting_a_todo_item():
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
    todo.send_keys("Item to be deleted")
    todo.send_keys(Keys.RETURN)

    time.sleep(1)
    
    todoItemToDelete = driver.find_element_by_xpath("//li[contains(text(),'Item to be deleted')]")
    items = driver.find_elements_by_tag_name("li")
    count = 0
    for element in items:
        if element == todoItemToDelete:
            indexToDelete = count
        count += 1

    delete_btns = driver.find_elements_by_xpath("//input[@value='Delete']")
    delete_btns[indexToDelete].click()

    time.sleep(1)

    assert "Item to be deleted" not in driver.page_source

    driver.quit()

def testing_archiving_a_todo_item():
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
    
    todoItemToArchive = driver.find_element_by_xpath("//li[contains(text(),'Item to be archived')]") #delete the todo item from the add todo item test case
    items = driver.find_elements_by_tag_name("li")
    count = 0
    for element in items:
        if element == todoItemToArchive:
            indexToArchive = count
        count += 1

    archive_btns = driver.find_elements_by_xpath("//button[contains(text(),' Archive to History ')]")
    archive_btns[indexToArchive].click()

    time.sleep(1)

    assert "Item to be archived" not in driver.page_source

    driver.quit()



