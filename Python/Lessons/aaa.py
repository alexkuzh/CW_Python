from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from Svetlana_Burenkova import xpathHelpers as xpH

desired_cap = {
    'browserName': 'chrome',
    # 'browser_version': '81.0',
    # 'os': 'Windows',
    # 'os_version': '10',
    # 'resolution': '1900x768',
    # 'name': 'Bstack-[Python] Sample Test'
}

capabilities = {
    "browserName": "chrome",
    "version": "81.0",
    "enableVNC": True,
    "enableVideo": True
}

# url = 'https://aleksandrkuzhele1:sxi8y58EkWTvHGNboy33@hub-cloud.browserstack.com/wd/hub'
# url = 'http://localhost:4444/wd/hub'
# driver: WebDriver = webdriver.Remote(url,
#                       desired_capabilities=desired_cap)

driver: WebDriver = webdriver.Remote(
    command_executor="http://174.138.52.132:4444/wd/hub",
    desired_capabilities=capabilities)

# driver: WebDriver = webdriver.Remote(
#     command_executor=url,
#     desired_capabilities=desired_cap)
# driver = webdriver.Chrome()
driver.get('https://www.google.com/')

# Check that an element is present on the DOM of a page and visible.
try:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "q")))
    print("First Chrome Page is ready!")
except TimeoutException:
    print("Loading took too much time!")
    # driver.get_screenshot_as_file("google_page_loading_error.png")
    # driver.save_screenshot('google_page_loading_error.png')

    # Checking page title for "Google" then print it
assert "Google", driver.title
print("Page has", driver.title + " as Page title")

# workflow over "elem" variable to better code length
# driver.find_element_by_name("q").clear()
# driver.find_element_by_name("q").send_keys("jknfjen")
# driver.find_element_by_name("q").send_keys(Keys.RETURN)

elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("wikipedia")
elem.send_keys(Keys.RETURN)
driver.implicitly_wait(5)

assert "No results found." not in driver.page_source

# Driver waits until element Wikipedia will be clickable
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Wikipedia')))
elem = driver.find_element(By.PARTIAL_LINK_TEXT, "Wikipedia")
elem.click()
assert "Wikipedia", driver.title
print("Page has", driver.title + " as Page title")

assert "No results found." not in driver.page_source

wait = WebDriverWait(driver, 2)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "central-featured")))
wait.until(EC.visibility_of_element_located((By.ID, "searchInput")))
# elem = driver.find_element(By.ID, "searchInput")
# elem = driver.find_element_by_id("searchInput")
elem = driver.find_element_by_xpath("//input[@id='searchInput']")
elem.send_keys("gold")
elem.send_keys(Keys.RETURN)
wait.until(EC.visibility_of_element_located((By.ID, "firstHeading")))
assert "Gold - Wikipedia", driver.title
print("Page has", driver.title + " as Page title")

driver.find_element_by_xpath("//img[@alt='Gold nugget (Australia) 4 (16848647509).jpg']").click()
driver.find_element_by_xpath("//img[@class='mw-mmv-final-image jpg']").click()
delay = 13  # seconds
try:
    WebDriverWait(driver, delay).until(
        EC.presence_of_element_located((
            By.XPATH, "//*[@src='https://upload.wikimedia.org/wikipedia/commons/d/d7/Gold-crystals.jpg']")))
    print("GoogleBrowser Page is ready!")
    driver.get_screenshot_as_file('ScreenshotGold_page.png')
except TimeoutException:
    print("Loading took too much time!")
    driver.get_screenshot_as_file('gold_page_loading_error.png')
driver.implicitly_wait(10)

#assert "Gold_nugget_(Australia)_4_(16848647509).jpg (3531×2278)" in driver.title
print("Page has", driver.title + " as Page title")
print("Test for Chrome is Done! Gold forever!")

driver.quit()