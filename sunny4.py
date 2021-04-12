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
        r"https://shop.vnpt.vn/sim-so.html",
        r"https://shop.vnpt.vn/sim-so.html?source=toanquoc"
    ]
    maxresult = None
    currentresult = None
    driver = chrome()
    try:
        with open('simsovnpt.txt', 'w') as f:
            for url in urls:
                driver.get(url)
                _, currentresult, maxresult, *_ = re.findall(r"\d+", element(driver, ".summary").text)

                while (int(currentresult) < int(maxresult)):
                    for i in elements(driver, ".btnBuySim span"):
                        sim = i.text
                        if sim.isdigit():
                            print(sim)
                            print(sim, file=f)

                    element(driver, "//li[contains(@class, 'active')]/following-sibling::li/a", By.XPATH).click()
                    time.sleep(3)
                    _, currentresult, maxresult, *_ = re.findall(r"\d+", element(driver, ".summary").text)
    finally:
        driver.quit()
