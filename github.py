#!/usr/bin/python3
from selenium import webdriver 
from time import sleep 

usr=input('Enter Email Id:') 
pwd=input('Enter Password:') 

#opening Firefox
driver = webdriver.Firefox() 

#going to page Facebook
driver.get('https://github.com/login') 
print ("Opened facebook") 
sleep(1) 

#entering email id
username_box = driver.find_element_by_id('login_field') 
username_box.send_keys(usr) 
print ("Email Id entered") 
sleep(1) 

#entering password
password_box = driver.find_element_by_id('password') 
password_box.send_keys(pwd) 
print ("Password entered") 

#Logging you in
login_box = driver.find_element_by_xpath("//input[@type='submit']") 
login_box.click() 

#Print done in terminal when user is logged in successfully
print ("Done") 

#press any word in terminal to quit
input('Press anything to quit') 
driver.quit() 
print("Finished") 

