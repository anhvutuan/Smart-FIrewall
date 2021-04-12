import re
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def chrome(headless=True):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--incognito")

    mode = "headless" if headless else "start-fullscreen"
    chrome_options.add_argument(f"--{mode}")

    driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(),
        options=chrome_options
    )
    return driver


def element(driver, locator, by=By.CSS_SELECTOR):
    return WebDriverWait(driver, 60).until(ec.presence_of_element_located((by, locator)))


def elements(driver, locator, by=By.CSS_SELECTOR):
    return driver.find_elements(*(by, locator))


if __name__ == "__main__":
    urls = [
        r"https://vietteltelecom.vn/di-dong/sim-so/tra-truoc",
        r"https://vietteltelecom.vn/di-dong/sim-so/tra-sau"
    ]
    PAGES = 10
    driver = chrome()
    try:
        with open('simsoviettel.txt', 'w') as f:
            for url in urls:
                driver.get(url)
                time.sleep(3)
                for i in range(PAGES):
                    for i in elements(driver, "#sim-thuong .name"):
                        sim = i.text.strip()
                        if sim.isdigit():
                            print(sim)
                            print(sim, file=f)
                    try:
                        element(driver, "//*[@class='navpage']//li[@class='current']/following-sibling::li/a", By.XPATH).click()
                    except:
                        time.sleep(3)
                        element(driver, "//*[@class='navpage']//li[@class='current']/following-sibling::li/a", By.XPATH).click()
                    time.sleep(3)
    finally:
        driver.quit()
