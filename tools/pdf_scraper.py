# Scrape all visa-related documents from the immigration department's official website.


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


def get_pages_link():
    # 目标网页
    url = "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing"
    index_url = "https://immi.homeaffairs.gov.au"
    pages_link = []

    try:
        # 设置 Chrome 的 Options 以启用 Headless 模式
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # 确保无界面运行
        # chrome_options.add_argument("--disable-gpu")  # 对于一些版本的Chrome，这个参数是必需的

        # 初始化 WebDriver
        driver = webdriver.Chrome(options=chrome_options)

        # 打开网页
        driver.get(url)

        # 等待页面加载（根据需要调整等待时间）
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'ha-wysiwyg > div > ul > li  a'))
        )

        # 获取页面源码
        html_content = driver.page_source

        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # 遍历并打印链接
        for a_tag in soup.select('ha-wysiwyg > div > ul > li  a'):
            href = a_tag.get('href')
            if not href.startswith(index_url):
                href = index_url + href
            # print(href)
            pages_link.append(href)
        return pages_link

    except Exception as e:
        print(f"发生错误: {e}")
        return []
    finally:
        # 清理，关闭浏览器
        driver.quit()



if __name__ == "__main__":
    pages_link = get_pages_link()
    print(pages_link)
