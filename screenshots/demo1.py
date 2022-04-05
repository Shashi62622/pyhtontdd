from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(r"C:\Users\DELL\PycharmProjects\nopCommerce\testCases\chromedriver.exe")
driver.maximize_window()
driver.get(" https://www.teachmint.com/institute/login")
sleep(2)
driver.find_element_by_id("phone-number-field").send_keys("0000019991")
sleep(2)
driver.find_element_by_xpath("//div[text()='Get OTP']").click()




