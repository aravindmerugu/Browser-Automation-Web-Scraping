from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches",["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled") 

  driver = webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com/login/")
  return driver

def clean_text(text):
  temp = float(text.split(": ")[1])
  return temp

def main():
  driver = get_driver()
  driver.find_element(by="id",value="id_username").send_keys("automated")
  time.sleep(2.0)
  driver.find_element(by="id",value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  time.sleep(2.0)
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  time.sleep(2.0)
  element = driver.find_element(by="xpath", 
  value="/html/body/div[1]/div/h1[2]").text
  return clean_text(element)

print(main())