# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.select import Select
# import time, random


# #initiate webdriver
# driver= webdriver.Chrome('C:\selenium_tutorial\chromedriver.exe')

# #open url and maximise window
# driver.get('https://form.jotform.com/sgupcloud02/traininglog')
# driver.maximize_window()

# name= driver.find_element_by_xpath('//*[@id="input_7"]')
# name.click()
# name.send_keys('ZJ')

# email= driver.find_element_by_xpath('//*[@id="input_9"]')
# email.click()
# email.send_keys('ZJ@ZJ.com')

# # guest_step2=driver.find_element_by_xpath('//a[text()="TOTAL HOURS FOR THE MONTH "]')
# # guest_step2.location_once_scrolled_into_view
# # time.sleep(2)

# phones = driver.find_element_by_xpath('//*[@id="input_12_0_0"]')
# #phones.click()
# dropdown = Select(phones)
# dropdown.select_by_index(1)
# time.sleep(1)

# phones1 =driver.find_element_by_xpath('//*[@id="input_12_1_0"]')
# dropdown1 = Select(phones1)
# dropdown1.select_by_index(1)
# time.sleep(1)

# phones1 =driver.find_element_by_xpath(//*[@id="input_12_0_1"]