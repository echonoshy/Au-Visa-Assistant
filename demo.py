import pdfkit
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def get_pdf_from_page(url):
    # 设置 Chrome 选项
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 确保浏览器以 Headless 模式运行
    chrome_options.add_argument("--disable-gpu")  # 禁用 GPU 加速（在某些系统上可能是必需的）
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("user-agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'")
    service = Service('/usr/local/bin/chromedriver')

    # 初始化 WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 打开网页
    driver.get(url)
    print("Title: " + driver.title)

    # 获取页面的 HTML 源码
    html_source = driver.page_source

    # 关闭浏览器
    driver.quit()
    
    from weasyprint import HTML

    HTML(string=html_source).write_pdf("output.pdf")

    # 使用 pdfkit 将 HTML 转换为 PDF
    # pdfkit.from_string(html_source, 'output.pdf')

if __name__ == "__main__":
    url = "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/orphan-relative-117"
    get_pdf_from_page(url)
