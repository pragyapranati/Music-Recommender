# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest3():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test3(self):
    # Test name: test3
    # Step # | name | target | value
    # 1 | open | http://localhost:8501/ | 
    self.driver.get("http://localhost:8501/")
    # 2 | setWindowSize | 1440x852 | 
    self.driver.set_window_size(1440, 852)
    # 3 | click | css=.element-container:nth-child(1) .st-be .st-be | 
    self.driver.find_element(By.CSS_SELECTOR, ".element-container:nth-child(1) .st-be .st-be").click()
    # 4 | type | css=.element-container:nth-child(1) .st-be .st-be | admin
    self.driver.find_element(By.CSS_SELECTOR, ".element-container:nth-child(1) .st-be .st-be").send_keys("admin")
    # 5 | click | css=.element-container:nth-child(2) .st-be .st-be | 
    self.driver.find_element(By.CSS_SELECTOR, ".element-container:nth-child(2) .st-be .st-be").click()
    # 6 | type | css=.element-container:nth-child(2) .st-be .st-be | 123456
    self.driver.find_element(By.CSS_SELECTOR, ".element-container:nth-child(2) .st-be .st-be").send_keys("123456")
    # 7 | click | css=.st-cq | 
    self.driver.find_element(By.CSS_SELECTOR, ".st-cq").click()
    # 8 | click | css=.st-cq | 
    self.driver.find_element(By.CSS_SELECTOR, ".st-cq").click()
    # 9 | click | css=.st-emotion-cache-uezpnz > .eyeqlp51 | 
    self.driver.find_element(By.CSS_SELECTOR, ".st-emotion-cache-uezpnz > .eyeqlp51").click()
    # 10 | type | css=.element-container:nth-child(3) .st-be .st-be | hindi
    self.driver.find_element(By.CSS_SELECTOR, ".element-container:nth-child(3) .st-be .st-be").send_keys("hindi")
    # 11 | click | css=.element-container:nth-child(4) .st-be .st-be | 
    self.driver.find_element(By.CSS_SELECTOR, ".element-container:nth-child(4) .st-be .st-be").click()
    # 12 | click | css=.element-container:nth-child(4) .st-be .st-be | 
    self.driver.find_element(By.CSS_SELECTOR, ".element-container:nth-child(4) .st-be .st-be").click()
    # 13 | type | css=.element-container:nth-child(4) .st-be .st-be | arijit singh
    self.driver.find_element(By.CSS_SELECTOR, ".element-container:nth-child(4) .st-be .st-be").send_keys("arijit singh")
    # 14 | sendKeys | css=.element-container:nth-child(4) .st-be .st-be | ${KEY_ENTER}
    self.driver.find_element(By.CSS_SELECTOR, ".element-container:nth-child(4) .st-be .st-be").send_keys(Keys.ENTER)
    # 15 | click | css=.st-emotion-cache-10fz3ls > p | 
    self.driver.find_element(By.CSS_SELECTOR, ".st-emotion-cache-10fz3ls > p").click()
    # 16 | click | css=.st-emotion-cache-10zg0a4 path:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".st-emotion-cache-10zg0a4 path:nth-child(2)").click()
    # 17 | click | css=.st-emotion-cache-uezpnz > .eyeqlp51 | 
    self.driver.find_element(By.CSS_SELECTOR, ".st-emotion-cache-uezpnz > .eyeqlp51").click()
    # 18 | close |  | 
    self.driver.close()
  
