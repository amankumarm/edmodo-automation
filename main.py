from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import Select
import sys
import time
path=sys.path[0]+'\\binary\\binary.exe'
driver = webdriver.Firefox(executable_path=path)
driver.get("https://new.edmodo.com/calendar/schedule")
time.sleep(5)
username_element=driver.find_element_by_name("username")
username_element.send_keys("amankumarm441@gmail.com")
password_element=driver.find_element_by_name("password")
password_element.send_keys("thisisedmodopassword")
driver.find_element_by_id("qa-test-lightbox-login").click()
time.sleep(5)

planner_box=driver.find_element_by_class_name("planner-box")
childrens=planner_box.find_elements_by_tag_name("div")[2]

print(childrens)
# driver.close()  