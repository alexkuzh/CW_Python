from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome()
driver.get('http://www.123formbuilder.com/form-5012215/online-order-form')
driver.maximize_window()
# driver.find_element_by_xpath('//input[@placeholder="First"]').send_keys('Sv')
# driver.find_element_by_xpath('//input[@placeholder="Last"]').send_keys('Kol')
# driver.find_element_by_xpath('//div//div//div[2]//div[1]//div[1]//input[1]').send_keys('svet.kol.ukk@gmail.com')
# driver.find_element_by_xpath('//input[contains(@placeholder,"### ### ####")]').send_keys('7775552233')
# driver.find_element_by_xpath('//label[@id="radio-0000000e1"]//label').click()
# driver.find_element_by_xpath('//body/form[@id="form"]/div/div/div/div/div[1]/div[1]/input[1]').send_keys('3')
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
driver.find_element_by_xpath('//body/form[@id="form"]/div/div/div/div/div/div/div[2]').click() #Вызываем календарь
sleep(1)
# driver.find_element_by_xpath('//div[contains(@class,"today")]').click()
driver.find_element_by_css_selector('css=div:nth-of-type(6) >> text=12').click()

sleep(5)