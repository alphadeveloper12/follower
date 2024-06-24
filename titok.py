from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from googletrans import Translator

def scrape_facebook_followers_count(url):
    options = Options()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Disable GPU acceleration
    options.add_argument("--lang=en-US")
    options.add_argument("--lang=en")
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})

    # Path to chromedriver executable
    driver_path = '/usr/lib/chromium-browser/chromedriver'
    service = Service(driver_path)

    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        time.sleep(5)  # Wait for the page to fully load, adjust as necessary

        # Determine the correct XPath based on the URL
        followers_xpath = None

        # Check for the correct XPath containing "followers" or "follower"
        followers_elem = WebDriverWait(driver, 10).until(

            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/h3/div[2]/strong'))
        )
        followers_count = followers_elem.text.strip()

        # Wait for the following count element to be present
        # following_elem = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "/following/")]/span'))
        # )
        # following_count = following_elem.text.strip()
        return {
            "followers": followers_count,
            # "following": following_count
        }

    except Exception as e:
        print(f"Error: {e}")
        return "0 followers"  # Return 0 followers if any exception occurs

    finally:
        driver.quit()

def main():
    url = "https://www.tiktok.com/@shahzadahmad9096"

    try:
        followers_count = scrape_facebook_followers_count(url)
        print(f"Followers Count: {followers_count}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
