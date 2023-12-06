from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import time


# Set up common Chrome options
chrome_options = Options()
# Uncomment the following lines if you want to run the script in headless mode
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")


# Function to get all visa-related page links
def get_pages_link():
    url = "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing"
    index_url = "https://immi.homeaffairs.gov.au"
    pages_link = []

    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'ha-wysiwyg > div > ul > li  a'))
        )
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')

        for a_tag in soup.select('ha-wysiwyg > div > ul > li  a'):
            href = a_tag.get('href')
            if not href.startswith('http'):
                href = index_url + href
            pages_link.append(href)
        return pages_link
    except Exception as e:
        print(f"Error occurred: {e}")
        return []
    finally:
        driver.quit()

# Function to download PDF from a given visa page
def get_pdf(url, pdf_name):
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get(url)
        print_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ctlTaskbarPrintLabel"))
        )
        print_button.click()
        time.sleep(5)  # Adjust as necessary for page load

        # Can't handle the pdf download page, it's not a web page
        # pdf_url = driver.current_url
        # response = requests.get(pdf_url)
        # if response.status_code == 200:
        #     with open(pdf_name, 'wb') as f:
        #         f.write(response.content)
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    # Example usage: get the first PDF link and download it
    visa_links = get_pages_link()
    if visa_links:
        first_link = visa_links[0]
        get_pdf(first_link, 'visa_document.pdf')
