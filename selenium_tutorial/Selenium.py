from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import time, random


#initiate webdriver
driver= webdriver.Chrome('C:\selenium_tutorial\chromedriver.exe')

#open url and maximise window
driver.get('http://www.tutorialsninja.com/demo/')
driver.maximize_window()

#click on the navigation for phone
phones = driver.find_element_by_xpath('//a[text()="Phones & PDAs"]')
phones.click()

#click on the iphone button
iphone = driver.find_element_by_xpath('//a[text()="iPhone"]')
iphone.click()
time.sleep(2)

# first picture
first_pic=driver.find_element_by_xpath('//ul[@class="thumbnails"]/li[1]')
first_pic.click()
time.sleep(2)

# next picture
next_click=driver.find_element_by_xpath('//button[@title="Next (Right arrow key)"]')
next_click.click()

for i in range(0,4):
    next_click.click()
    time.sleep(1)

#screenshot
driver.save_screenshot('screenshot#' + str(random.randint(0,101)) + '.png')

#close the image button
xbutton_click=driver.find_element_by_xpath('//button[@title="Close (Esc)"]')
xbutton_click.click()
time.sleep(2)

#quantity
quantity=driver.find_element_by_id('input-quantity')
quantity.click()
time.sleep(1)

#clear the quantity default value and add 2
quantity.clear()
time.sleep(1)
quantity.send_keys('2')
time.sleep(1)

#click on add to cart button
addtobutton= driver.find_element_by_id('button-cart')
addtobutton.click()

# naviagate to laptop menu and scroll down to laptop
laptop=driver.find_element_by_xpath('//a[text()="Laptops & Notebooks"]')
action=ActionChains(driver) # need to research on this
action.move_to_element(laptop).perform()
time.sleep(2)
laptop2=driver.find_element_by_xpath('//a[text()="Show All Laptops & Notebooks"]')
laptop2.click()
time.sleep(2)

# click on the HP laptop into the page
hp_laptop=driver.find_element_by_xpath('//a[text()="HP LP3065"]')
hp_laptop.click()

# scroll down to find add to cart page
addtobutton2=driver.find_element_by_xpath('//button[@id="button-cart"]')
addtobutton2.location_once_scrolled_into_view
time.sleep(2)

#click on the calendar button
calendar=driver.find_element_by_xpath('//i[@class="fa fa-calendar"]')
calendar.click()
time.sleep(1)

#date picker
nextclickcalendar= driver.find_element_by_xpath('//th[@class="next"]')
month_year=driver.find_element_by_xpath('//th[@class="picker-switch"]')

#let it click until it reaches that date
while month_year.text != 'December 2022':
    nextclickcalendar.click()

#click on day 25
calendar_date=driver.find_element_by_xpath('//td[text()="25"]')
calendar_date.click()
time.sleep(2)

#quantity
quantity2=driver.find_element_by_id('input-quantity')
quantity2.click()
time.sleep(1)

#clear the quantity default value and add 2
quantity2.clear()
time.sleep(1)
quantity2.send_keys('3')
time.sleep(2)

#add to cart for laptops
addtobutton2= driver.find_element_by_id('button-cart')
addtobutton2.click()

#click on cart button
time.sleep(1)
cartbutton=driver.find_element_by_id('cart-total')
cartbutton.click()
time.sleep(1)

checkout=driver.find_element_by_xpath('//p[@class="text-right"]/a[2]')
checkout.click()
time.sleep(3)


#click on delete button for items that was sold out
deletebutton=driver.find_element_by_xpath('//i[@class="fa fa-times-circle"]')
deletebutton.click()
time.sleep(1)

# click on the checkout button right after deleted the product that was sold out
checkout2=driver.find_element_by_xpath('//a[text()="Checkout"]')
checkout2.click()
time.sleep(1)

# click on the guest radio button
guest=driver.find_element_by_xpath('//input[@value="guest"]')
guest.click()

# click on the continue once selected guest
guest_button= driver.find_element_by_id('button-account')
guest_button.click()
time.sleep(1)

# scroll down to see the whole website
guest_step2=driver.find_element_by_xpath('//a[text()="Step 2: Billing Details "]')
guest_step2.location_once_scrolled_into_view
time.sleep(2)

#enter first name
first_field=driver.find_element_by_id('input-payment-firstname')
first_field.click()
first_field.send_keys('First')
time.sleep(1)

#enter last name
last_field=driver.find_element_by_id('input-payment-lastname')
last_field.click()
last_field.send_keys('Last')
time.sleep(1)

#enter email
email_field=driver.find_element_by_id('input-payment-email')
email_field.click()
email_field.send_keys('first_last@email.com')
time.sleep(1)

#enter phone
phone_field=driver.find_element_by_id('input-payment-telephone')
phone_field.click()
phone_field.send_keys('12345678')
time.sleep(1)

#enter address
address_field=driver.find_element_by_id('input-payment-address-1')
address_field.click()
address_field.send_keys('Singaporeee')
time.sleep(1)

#enter city
city_field=driver.find_element_by_id('input-payment-city')
city_field.click()
city_field.send_keys('Singapore')
time.sleep(1)

#enter postal
postal_field=driver.find_element_by_id('input-payment-postcode')
postal_field.click()
postal_field.send_keys('654321')
time.sleep(1)

#country - dropdown
country_field=driver.find_element_by_id('input-payment-country')
dropdown=Select(country_field)
dropdown.select_by_index(188)
time.sleep(1)

#region - dropdown
region_field=driver.find_element_by_id('input-payment-zone')
dropdown=Select(region_field)
dropdown.select_by_index(1)
time.sleep(1)

#click on the continue button
continue_2=driver.find_element_by_id('button-guest')
continue_2.click()
time.sleep(1)


#click on continue on button 4
continue_4=driver.find_element_by_id('button-shipping-method')
continue_4.click()
time.sleep(1)

#click on the agree checkbox
agree_checkbox=driver.find_element_by_xpath('//input[@name="agree"]')
agree_checkbox.click()

#click on continue in button 5
continue_5=driver.find_element_by_id('button-payment-method')
continue_5.click()
time.sleep(1)

# #final price
# final_price=driver.find_element_by_xpath('//table[@class="table table-bordered table-hover"]')
# print("This is the final price of the products " + final_price.text)
# time.sleep(2)

#click on confirm order 
confirm_order=driver.find_element_by_id('button-confirm')
confirm_order.click()
time.sleep(5)

#screenshot the sucess
driver.save_screenshot('Sucess#' + str(random.randint(0,101)) + '.png')

# #sucess text
# sucess_text=driver.find_element_by_xpath('//div[@class="col-sm-12"]/h1')
# print(sucess_text.text)
# time.sleep(1)

#click on the continue button
continue_button=driver.find_element_by_link_text("Continue")
continue_button.click()
time.sleep(2)

# close the browser
driver.close()


