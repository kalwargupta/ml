#!usr/bin/python3
from selenium import webdriver

#inputs from user  
usr = input('enter the fb login id')
pwd = input ('enter the password')

#opening firefox
driver=webdriver.Firefox()

#opening the url as facebook.com
driver.get('https://www.facebook.com')
print ("facebook page opened")

#feeding the email id 
username_field=driver.find_element_by_id('email')
username_field.send_keys(usr)
print("email id entered")

#feeding the password
password_field=driver.find_element_by_id('pass')
password_field.send_keys(pwd)
print ('password is entered')

#login button clickd
login_button=driver.find_element_by_id('loginbutton')
login_button.click()

#done

