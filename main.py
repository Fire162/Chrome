from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode, without a GUI
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL of the webpage
url = "http://example.com"  # Replace with the actual URL

# Interval between each visit in seconds
interval = 1  # 1 second

# Number of times to open the web page
iterations = 10  # Adjust as needed

for i in range(iterations):
    driver.get(url)
    time.sleep(interval)

driver.quit()
