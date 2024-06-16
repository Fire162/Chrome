from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")  # Required for running in some VPS environments
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
chrome_options.add_argument("--headless")  # Run in headless mode for VPS
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")

# Path to ChromeDriver executable (ensure it matches your installation)
chrome_driver_path = "/usr/local/bin/chromedriver"

# Create a new Chrome session
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the website (replace with your desired URL)
website_url = 'http://example.com'
driver.get(website_url)

try:
    # Keep the browser open indefinitely
    while True:
        time.sleep(60)  # Sleep for 60 seconds
except KeyboardInterrupt:
    print("Script interrupted by user")
finally:
    # Close the browser
    driver.quit()
  
