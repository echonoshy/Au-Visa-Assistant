# Prerequisite: please manually download ChromeDriver and ensure it matches the version of Chrome.


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

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 确保浏览器以 Headless 模式运行
    chrome_options.add_argument("--disable-gpu")  # 禁用 GPU 加速（在某些系统上可能是必需的）
    chrome_options.add_argument("user-agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'")

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




def get_pdf_from_page(url):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service

    # 设置 Chrome 选项
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 确保浏览器以 Headless 模式运行
    # chrome_options.add_argument("--disable-gpu")  # 禁用 GPU 加速（在某些系统上可能是必需的）
    chrome_options.add_argument("user-agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'")
    chrome_options.add_argument("--print-to-pdf=a.pdf")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')


    service = Service('/usr/local/bin/chromedriver')

    # 初始化 WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 打开网页
    driver.get('https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/orphan-relative-117')
    print("Title: " + driver.title)
    # 网页将自动保存为 PDF
    driver.quit()



if __name__ == "__main__":
    # Example usage: get the first PDF link and download it
    # visa_links = get_pages_link()
    # if visa_links:
    #     first_link = visa_links[0]
    #     get_pdf(first_link, 'visa_document.pdf')

    url = "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/orphan-relative-117"
    get_pdf_from_page(url)


# https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/orphan-relative-117

