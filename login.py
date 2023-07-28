from selenium import webdriver
import time
import os

os.environ["PATH"] += os.pathsep + os.path.dirname(os.path.realpath(__file__))
driver = webdriver.PhantomJS()
driver.get('https://gw.ict.ac.cn/')
driver.set_window_size(1124, 850)
name = driver.find_element_by_id("username")
name.send_keys('账号')
password = driver.find_element_by_id('password')
password.send_keys('密码')
driver.find_element_by_id('login-account').click()
time.sleep(1)
driver.quit()
