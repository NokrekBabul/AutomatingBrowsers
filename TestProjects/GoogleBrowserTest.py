import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/theda/PycharmProjects/AutomatingBrowsers/drivers/chromedriver.exe")

driver.implicitly_wait(5)
driver.get("https://google.com")
driver.maximize_window()

driver.find_element_by_name("q").send_keys("babul")
driver.find_element_by_name("btnK").click()

print(driver.title)

time.sleep(5)
driver.close()
driver.quit()

print("Test is completed successfully!!!")

"""Please feel free to contact at: codingandtestingdaily@gmail.com
 Thank you!!! 
 
 """
