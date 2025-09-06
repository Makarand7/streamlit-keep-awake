from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# List your Streamlit app URLs here
urls = [
    "https://bertelsmann-arvato-project-ammqvimjvkrdzksiee7pmh.streamlit.app/",
    "https://recommendationswithibm-kbi4ibaoccgd6wyt5soorr.streamlit.app/"
]

# Setup headless Chrome
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Launch browser
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

for url in urls:
    try:
        driver.get(url)
        print(f"Visited: {url}")
        time.sleep(10)  # Wait for 10 seconds to simulate user viewing
    except Exception as e:
        print(f"Failed to visit {url}: {e}")

driver.quit()

