from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

# Set Firefox options for headless mode
firefox_options = Options()
firefox_options.headless = True

# Create a new Firefox session
driver = webdriver.Firefox(options=firefox_options)

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
