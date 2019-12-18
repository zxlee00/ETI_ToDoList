import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
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

    time.sleep(2)

    assert "Todo List" in driver.page_source
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
            print(indexToDelete)
        count += 1
        print(count)

    delete_btns = driver.find_elements_by_xpath("//a[contains(text(),'DELETE')]")
    print(delete_btns.count)
    delete_btns[indexToDelete].click()

    time.sleep(1)

    assert "Item to be deleted" not in driver.page_source

    driver.quit()

def test_automatically_archiving_a_todo_item_upon_completion():
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
    todo.send_keys("Complete this item")
    todo.send_keys(Keys.RETURN)

    time.sleep(1)
    
    todoItemToComplete = driver.find_element_by_xpath("//li[contains(text(),'Complete this item')]")
    items = driver.find_elements_by_tag_name("li")
    count = 0
    for element in items:
        if element == todoItemToComplete:
            indexToComplete = count
        count += 1

    complete_btns = driver.find_elements_by_xpath("//a[contains(text(),'COMPLETE')]")
    complete_btns[indexToComplete].click()

    time.sleep(1)

    assert "Complete this item" not in driver.page_source

    driver.quit()

def test_displaying_of_timestamp_of_todo_item():
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
    todoitemDatetime = datetime.now()
    todoitemDatetime = datetime.strftime(todoitemDatetime, "%d-%b-%Y, %H:%M")
    todo = driver.find_element_by_name("content")
    todo.send_keys("Test timestamp to-do item")
    todo.send_keys(Keys.RETURN)

    time.sleep(1)

    todoItemDisplayed = "Test timestamp to-do item (" + todoitemDatetime +")"
    
    assert todoItemDisplayed in driver.page_source
    
    driver.quit()

def test_displaying_todo_items_by_user():
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
    todo.send_keys("Test to-do item by user")
    todo.send_keys(Keys.RETURN)

    time.sleep(1)

    assert "Test to-do item by user" in driver.page_source

    logoutBtn = driver.find_element_by_xpath("//a[contains(text(), 'Log Out')]")
    logoutBtn.click()

    time.sleep(2)

    loginBtn = driver.find_element_by_xpath("//a[contains(text(), 'Log In')]")
    loginBtn.click()

    time.sleep(2)

    userelem = driver.find_element_by_id("id_username")
    userelem.clear()
    userelem.send_keys("zxnlee")
    userelem.send_keys(Keys.RETURN)
    pswdelem = driver.find_element_by_id("id_password")
    pswdelem.clear()
    pswdelem.send_keys("P@ssw0rd")
    pswdelem.send_keys(Keys.RETURN)

    time.sleep(2)

    assert "Test to-do item by user" not in driver.page_source

    driver.quit()
