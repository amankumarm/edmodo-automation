from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
# from creds import username,password 
import sys
import time
def get_assignments():
    # path=sys.path[0]+'/binary/geckodriver'
    path='./binary/geckodriver'
    print(path)
    # options = Options()
    options = webdriver.FirefoxOptions()
    options.add_argument("--remote-debugging-port=9224")
	options.add_argument("--headless")
	options.add_argument("--disable-gpu")
	options.add_argument("--no-sandbox")
    # options.add_argument('--headless')
    binary = FirefoxBinary(os.environ.get('FIREFOX_BIN'))
    driver = webdriver.Firefox(executable_path=os.environ.get('GECKODRIVER_PATH'),firefox_binary=binary,options=options)
    driver.get("https://new.edmodo.com/calendar/schedule")
    time.sleep(5)
    username_element=driver.find_element_by_name("username")
    username_element.send_keys("amankumarm441@gmail.com")
    password_element=driver.find_element_by_name("password")
    password_element.send_keys("thisisedmodopassword")
    driver.find_element_by_id("qa-test-lightbox-login").click()
    time.sleep(5)
    outputArray=[]
    elem = driver.find_elements_by_xpath(".//*[@class='schedule-group-title']")
    if len(elem)==0:
        print("Enjoy your life")
        return {'status':404,'message':"no assignments for now"}
    first_assi_heading=driver.find_element_by_class_name("schedule-group-title")
    parent=first_assi_heading.find_element_by_xpath("..")
    outerParent=parent.find_element_by_xpath("..")
    allChildren=outerParent.find_elements_by_xpath("./*")
    allChildren.pop(-1)
    for i in range(0,len(allChildren)):
        outputObject={'assigns':[]}
        opArray=[]
        count=0
        testChild=allChildren[i]
        # date
        print("test",testChild.find_element_by_class_name("schedule-group-title").find_elements_by_css_selector("*")[1].get_attribute("innerHTML"))
        outputObject["Date"]="-".join(testChild.find_element_by_class_name("schedule-group-title").find_elements_by_css_selector("*")[1].get_attribute("innerHTML").split("/")[::-1])
        for j in range(0,len(testChild.find_elements_by_class_name("fc-time"))):
            assignments={}
            assignments["Time"]=testChild.find_elements_by_class_name("fc-time")[j].get_attribute("innerHTML")
            assignments["Title"]=testChild.find_elements_by_class_name("title")[j].get_attribute("innerHTML")
            assignments["Group-name"]=testChild.find_elements_by_class_name("group-name")[j].get_attribute("innerHTML")
            assignments["start"]=outputObject["Date"]
            assignments["title"]=assignments["Group-name"]+assignments["Title"]
            assignments["id"]=count
            del assignments["Group-name"]
            del assignments["Time"]
            del assignments["Title"]
            count=count+1
            outputObject['assigns'].append(assignments)
        outputArray.append(outputObject)
    time.sleep(5)
    driver.close()
    return outputArray

# print(get_assignments())