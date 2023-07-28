from selenium import webdriver
import os
import time

os.environ["PATH"] += os.pathsep + os.path.dirname(os.path.realpath(__file__))
driver = webdriver.PhantomJS()
driver.set_window_size(1124, 850)
driver.get('https://gw.ict.ac.cn')
driver.find_element_by_id('logout').click()
driver.find_element_by_class_name('btn-confirm').click()
time.sleep(1)
driver.quit()
