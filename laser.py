from selenium import webdriver
import os
import time

useragent = "Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/72.0"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--allow-popups-during-page-unload")
chrome_options.add_argument("--disable-background-timer-throttling")
chrome_options.add_argument(f'user-agent={useragent}')
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

driver.get("https://aug-a3.blogspot.com/")
print("Opened the web page.")
driver.find_element_by_link_text("Start").click()
time.sleep(5)
driver.find_element_by_link_text("click here").click()
print("...Happening...")
time.sleep(1700)

driver.quit()

print("up all.")
