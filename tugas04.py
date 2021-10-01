from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://demoqa.com/text-box')
driver.maximize_window()

def test_submit():
    driver.find_element_by_id('userName').send_keys('Listy')
    driver.find_element_by_id('userEmail').send_keys('listy@gmail.com')
    driver.find_element_by_id('currentAddress').send_keys('jakarta')
    driver.find_element_by_id('permanentAddress').send_keys('bandung')
    element = driver.find_element_by_xpath("//button[@id='submit']")
    driver.execute_script("arguments[0].click();", element)

    Name = driver.find_element_by_id('name').text
    Email = driver.find_element_by_id('email').text
    CurrentAddress = driver.find_element_by_id('currentAddress').text
    PermanentAddress = driver.find_element_by_id('permanentAddress').text

    assert Name == 'Name:Listy'
    assert Email == 'Email:listy@gmail.com'
    assert CurrentAddress == 'Current Address :jakarta'
    assert PermanentAddress == 'Permananet Address :bandung'
