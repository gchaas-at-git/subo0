# import the necessary modules
from selenium import webdriver
import streamlit as st


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait

import streamlit.components.v1 as components

from selenium.webdriver.chrome.options import Options
from time import sleep

def sub_butt():
    driver.implicitly_wait(10)
    
    submit_button = driver.find_elements(By.CSS_SELECTOR, ('*[type="submit"]'))
    print(f'number of buttons: {len(submit_button)}')

    if len(submit_button) ==1:
        submit_button[0].click()

    if len(submit_button) ==2:
        submit_button[1].click()
        
    if len(submit_button) == 0:
        driver.close()

    # return {'sub': len(submit_button)}
    sleep(1)



#title 
st.write("""
#### Some title
""")

input_link = "https://umfragen.iab.de/goto/HOPPw1"

chrome_options = Options()
#chrome_options.add_argument('start-maximized')
chrome_options.add_argument('--window-size=1920x1080')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)            

driver.get(input_link)

driver.save_screenshot("screenshot.png")

screen = st.empty()

with screen.container():
    st.image("screenshot.png", caption='Screenshot of example.com', use_column_width=True)

#if st.sidebar.button("press"):

for i in range(0,10): 
     sub_butt()
     driver.save_screenshot("screenshot.png")
     with screen.container():
        st.image("screenshot.png", caption=f'screen {i}', use_column_width=True)
        st.write(i)




