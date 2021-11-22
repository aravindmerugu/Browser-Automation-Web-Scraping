from selenium import webdriver
import time
from datetime import datetime as dt
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
  driver.get("https://automated.pythonanywhere.com")
  return driver

def clean_text(text):
  temp = float(text.split(": ")[1])
  return write_file(temp)

def write_file(text):
  filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
  with open(filename, 'w') as file:
    file.write(str(text))  

def main():
  driver = get_driver()
  while True:
    time.sleep(2.0)
    element = driver.find_element(by="xpath", 
    value="/html/body/div[1]/div/h1[2]").text
    clean_text(element)

print(main())