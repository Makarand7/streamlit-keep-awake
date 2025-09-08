from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

urls = [
    "https://bertelsmann-arvato-project-ammqvimjvkrdzksiee7pmh.streamlit.app/",
    "https://recommendationswithibm-kbi4ibaoccgd6wyt5soorr.streamlit.app/",
    "https://evolution-design.streamlit.app/"
]

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

for url in urls:
    try:
        driver.get(url)
        time.sleep(5)  # wait for page to load

        # Look for the "Yes, get this app back up!" button and click it
        try:
            button = driver.find_element(By.XPATH, "//button[contains(., 'Yes')]")
            button.click()
            print(f"🔄 Woke up: {url}")
            time.sleep(20)  # wait for app to start
        except:
            print(f"✅ App already awake: {url}")

    except Exception as e:
        print(f"❌ Error visiting {url}: {e}")

driver.quit()

