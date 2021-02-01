from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import requests


def debug(query):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options =options, executable_path = 'geckodriver.exe')
    driver.implicitly_wait(30)
    driver.maximize_window()

    # Navigate to the application home page
    driver.get("https://www.google.com/")

    # get the search textbox
    search_field = driver.find_element_by_name("q")
    search_field.clear()

    # enter search keyword and submit
    query ="stackover flow "+query
    search_field.send_keys(query)
    search_field.submit()

    lists= driver.find_elements_by_class_name("r")

    URL=""
    for listitem in lists:
        tt = listitem.get_attribute("innerHTML")
        URL=tt.split('"')[1]
        break
    print(URL) 

    driver.quit()

    driver1 = webdriver.Firefox(options =options, executable_path = 'geckodriver.exe')
    driver1.implicitly_wait(30)
    driver1.maximize_window()


    driver1.get(URL)

    el= driver1.find_elements_by_class_name("post-text")
    temp=0
    response = ""
    for i in el:
        if temp == 0:
            response += "Question :\n"
            response += i.text + "\n"
        else:
            response += "Answer : " + temp + "\n"
            response += i.text + "\n"
        temp+=1
        response += "............................................................................................."
    driver1.quit()
    return response
