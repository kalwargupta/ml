#!/usr/bin/python3
from selenium import webdriver 
from time import sleep 

usr=input('Enter Email Id:') 
pwd=input('Enter Password:') 

#opening Firefox
driver = webdriver.Firefox() 

#going to page Facebook
driver.get('https://www.facebook.com/') 
print ("Opened facebook") 
sleep(1) 

#entering email id
username_box = driver.find_element_by_id('email') 
username_box.send_keys(usr) 
print ("Email Id entered") 
sleep(1) 

#entering password
password_box = driver.find_element_by_id('pass') 
password_box.send_keys(pwd) 
print ("Password entered") 

#Logging you in
login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 

#Print done in terminal when user is logged in successfully
print ("Done") 

#press any word in terminal to quit
input('Press anything to quit') 
driver.quit() 
print("Finished") 
