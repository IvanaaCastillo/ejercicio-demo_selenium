from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import tempfile

def test_page_title():
    chrome_options = Options()
    temp_dir = tempfile.mkdtemp()  # Carpeta temporal para el perfil de usuario
    chrome_options.add_argument(f"--user-data-dir={temp_dir}")
    
    browser = webdriver.Chrome(options=chrome_options)

    browser.get('https://github.com')
    titleElement = browser.find_element(By.ID, 'hero-section-brand-heading')

    assert titleElement.text == 'Build and ship software on a single, collaborative platform'

    browser.quit()
