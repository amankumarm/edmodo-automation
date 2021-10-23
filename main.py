from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import Select
from creds import username,password 
import sys
import time
def get_assignments():
    path=sys.path[0]+'\\binary\\binary.exe'
    driver = webdriver.Firefox(executable_path=path)
    driver.get("https://new.edmodo.com/calendar/schedule")
    time.sleep(5)
    username_element=driver.find_element_by_name("username")
    username_element.send_keys(username)
    password_element=driver.find_element_by_name("password")
    password_element.send_keys(password)
    driver.find_element_by_id("qa-test-lightbox-login").click()
    time.sleep(5)
    outputArray=[]
    first_assi_heading=driver.find_element_by_class_name("schedule-group-title")
    parent=first_assi_heading.find_element_by_xpath("..")
    outerParent=parent.find_element_by_xpath("..")
    allChildren=outerParent.find_elements_by_xpath("./*")
    allChildren.pop(-1)
    for i in range(0,len(allChildren)):
        outputObject={'assigns':[]}
        testChild=allChildren[i]
        outputObject["Date"]=testChild.find_element_by_class_name("schedule-group-title").find_elements_by_css_selector("*")[1].get_attribute("innerHTML")
        for j in range(0,len(testChild.find_elements_by_class_name("fc-time"))):
            assignments={}
            assignments["Time"]=testChild.find_elements_by_class_name("fc-time")[j].get_attribute("innerHTML")
            assignments["Title"]=testChild.find_elements_by_class_name("title")[j].get_attribute("innerHTML")
            assignments["Group-name"]=testChild.find_elements_by_class_name("group-name")[j].get_attribute("innerHTML")
            outputObject['assigns'].append(assignments)
        outputArray.append(outputObject)
    time.sleep(5)
    driver.close()
    return outputArray

# get_assignments()