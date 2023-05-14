from selenium import webdriver

def get_drivers ():
#setting up the opitions for easy scraping 
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_argument("disable-blink-features = AutomationControlled")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  driver = webdriver.Chrome(options=options)
  driver.get("https://www.york.ac.uk/teaching/cws/wws/webpage1.html")
  return driver

def main():
  driver = get_drivers()
  element = driver.find_element(by= "xpath", value = "/html/body/hmtl/table/tbody/tr/td/div[2]/p[2]" )
  return element.text

print(main())