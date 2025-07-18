from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_page_title():
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get('https://github.com')
    titleElement = browser.find_element(By.ID, 'hero-section-brand-heading')
    assert titleElement.text == 'Build and ship software on a single, collaborative platform'
    browser.quit()
