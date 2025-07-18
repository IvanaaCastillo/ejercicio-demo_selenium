import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_page_title():
    chrome_options = Options()
    # Puedes agregar opciones si quieres, ejemplo para correr en headless:
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Usa webdriver-manager para descargar y manejar automáticamente el driver
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)

    browser.get("https://github.com")

    title_element = browser.find_element(By.ID, "hero-section-brand-heading")
    assert title_element.text == "Build and ship software on a single, collaborative platform"

    browser.quit()
