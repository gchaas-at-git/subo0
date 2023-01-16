from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException

#making the driver headless
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")


# options.add_argument("--disk-cache-size=0")


from time import sleep
import time
import re
import pandas
import random

#load browser driver
# s = Service("C:/Users/gchaa/Dropbox/000_Projekte_Paper_Ideen/200_In_Bearbeitung/SuBo/bot")
# driver = webdriver.Chrome("chromedriver")

#s = Service("C:\Program Files (x86)\chromedriver.exe")



# # head to github login page
# driver.get("https://github.com/login")
# # find username/email field and send the username itself to the input field
# driver.find_element("id", "login_field").send_keys("username")
# # find password input field and insert password as well
# driver.find_element("id", "password").send_keys("password")
# # click login button
# driver.find_element("name", "commit").click()


#driver = webdriver.Chrome(service=s).get("https://umfragen.iab.de/goto/subo1.de")


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

def find_me_elements():

    driver.implicitly_wait(0.2)
    # driver.delete_all_cookies()
    # sleep(2)
    
    #search for tables on page
    table = driver.find_elements(By.TAG_NAME, ("table"))
    rows = driver.find_elements(By.TAG_NAME, ("tr"))

    # table = []
    # rows = []
    # Initialize the column count to 0
    col_count = 0

    # Iterate through the rows
    for row in rows:
        # Find all <td> elements in the current row
        cols = row.find_elements(By.TAG_NAME, ("td"))
        # Update the column count if the current row has more columns
        col_count = max(col_count, len(cols))

    #find stuff to identify questions
    radios = driver.find_elements(By.CSS_SELECTOR, ('*[type="radio"]'))
    checkboxes = driver.find_elements(By.CSS_SELECTOR, ('*[type="checkbox"]'))
    dropdown = driver.find_elements(By.TAG_NAME, ("select"))
    textfield = driver.find_elements(By.CSS_SELECTOR, ('*[type="text"]'))
    textarea = driver.find_elements(By.TAG_NAME, ("textarea"))
    
    #radios = []
    # checkboxes = []
    # dropdown = []
    # textfield = []
    # textarea = []
    

    print(f'#tables: {len(table)}', 
          f'#cols: {col_count}',
          f'#radios: {len(radios)}',
          f'#checkboxes: {len(checkboxes)}',
          f'#dropdown: {len(dropdown)}',
          f'#textfield: {len(textfield)}',
          f'#textareas: {len(textarea)}')

    return {
    #return object length
    'table_len': len(table),
    'rows_len': len(rows),
    'cols_len': col_count,
    'radios_len': len(radios),
    'checkboxes_len': len(checkboxes),
    'dropdown_len': len(dropdown),
    'textfield_len': len(textfield),
    'textarea_len': len(textarea),
    #return the obejcts
    'table': table,
    'radios': radios,
    'checkboxes': checkboxes,
    'dropdown': dropdown,
    'textfield': textfield,
    'textarea': textarea,
    }
    

def respond():

    start_time = time.time()
    
    print(f"Code takes {time.time() - start_time} sec when calling respond()")
    
    r = find_me_elements()

    print(f"finding elements takes {time.time() - start_time} sec when calling respond()")

    #single response
    #######################################################################################################
    #######################################################################################################
    #######################################################################################################
    if r['table_len'] == 1 and r['cols_len'] == 1 and r['radios_len'] > 0 and r['checkboxes_len'] ==0 and r['dropdown_len'] == 0 and r['textfield_len'] ==0:
        
        #choose a random radio
        num = random.randint(0,r['radios_len']-1)
        r['radios'][num].click()
        
        print(f'response to single response option, choose category: {num}')
        
        
    #multiple response
    #######################################################################################################
    #######################################################################################################
    #######################################################################################################
    elif r['table_len'] == 1 and r['cols_len'] == 1 and r['radios_len'] == 0 and r['checkboxes_len'] >0 and r['dropdown_len'] == 0:
    
        #choose a number of checks that will be made
        num_mult = random.randint(1,r['checkboxes_len']-1)
        
        #make a list of all response options
        cats = list(range(0,r['checkboxes_len']))
        
        #choose the response categories
        nums = random.choices(cats, k=num_mult)
        
        for num in nums:
            r['checkboxes'][num].click()
        
        print(f'response to multiple response option, choose categories: {nums}')
        
        
    ##rating response
    #######################################################################################################
    #######################################################################################################
    #######################################################################################################
    elif r['table_len'] == 1 and r['cols_len'] > 1 and r['radios_len'] > 0 and r['checkboxes_len'] ==0 and r['dropdown_len'] == 0 and r['textfield_len'] ==0:
    
        #choose a random radio from the first line
        num = random.randint(0,r['cols_len']-1)
        
        num_list = [num]
        
        rows = int(r['radios_len']/r['cols_len'])
        
        for i in range(1,rows):
             r['radios'][num].click()
             
             num = r['cols_len']*i+random.randint(0,r['cols_len']-1)
             num_list = num_list + [num - r['cols_len']*i]
        
        r['radios'][num].click()
        
        print(f'respond to a rating question with {rows} rows. responses for each row: {num_list}')
    
    ##single response with textfield
    #######################################################################################################
    #######################################################################################################
    #######################################################################################################
    elif r['table_len'] == 1 and r['cols_len'] == 1 and r['radios_len'] > 0 and r['checkboxes_len'] ==0 and r['dropdown_len'] == 0 and r['textfield_len'] >0:
        
        #the question this code is based on asks for an email address. The code is very specific for that question
        
        #choose 0 or 1. if 0 respond to the radio button. if 1 respond to the textfield. 
        num_x = random.randint(0,1)
        
        if num_x == 0:
            num = random.randint(0,r['radios_len']-1)
            r['radios'][num].click()
        elif num_x == 1:
            #if an email is needed:
            text = driver.find_elements(By.XPATH, ("//*[contains(text(),'E-Mail')]"))
            
            if len(text) > 0:
                for i in range(0,len(r['textfield'])):
                    r['textfield'][i].send_keys("iamabot@subo.de")
            else:
                for i in range(0,len(r['textfield'])):
                    #this should apply to most. 
                    r['textfield'][i].send_keys(random.randint(0, 100))
        
        print("response to single response with textfield.")
        
    ##textarea
    #######################################################################################################
    #######################################################################################################
    #######################################################################################################
    elif r['textarea_len'] == 1:
        
        r['textarea'][0].send_keys("Hi! I am SuBo_0 a survey bot. It was a pleasure to respond to your survey. Well done.") 
    
        print('textarea response')
    
    ##dropdown menu
    #######################################################################################################
    #######################################################################################################
    #######################################################################################################
    elif r['dropdown_len'] >0:
        
        nums = []
        
        for i in range(0, r['dropdown_len']-1):
            r['dropdown'][i].click()
        
            select = Select(r['dropdown'][i])
            options = select.options
            num = random.randint(0,len(options)-1)
            select.select_by_index(num)
        
            nums.append(num)
            
    
        print(f'dropdown response, choose category {nums}')
    
    ##textfield response
    #######################################################################################################
    #######################################################################################################
    #######################################################################################################

    elif r['table_len'] == 0 and r['textfield_len'] >0:
        
        #this should apply to most.
        num =  random.randint(0, 100)
        r['textfield'][0].send_keys(num) 
        
        print(f"textfield response: {num}")
        
    else:
        print("no response")
    
    print(f"going through IFs takes {time.time() - start_time} sec")
    
    sub_butt()
    
    #do we have an error?
    driver.implicitly_wait(0.2)
    error = driver.find_elements(By.CSS_SELECTOR, ('*[class="error"]'))
    
    
    
    #if we have an error, try to correct it. 
    if len(error) !=0:
        
        print("error found")
        # I assume that the last error message contains the valueable information
        error_text = error[-1].text
        
        print(error_text)
        
        #does the error text contain numbers?
        numbers = re.findall(r'\d+', error_text)
        
        if len(numbers) != 0:
            print("getting numbers")         
            min_number = int(numbers[0])
            max_number = int(numbers[1])
            new_num = random.randint(min_number, max_number)
            
            r = find_me_elements()
        
                
            r['textfield'][0].clear()
            r['textfield'][0].send_keys(new_num)
        else: 
            r['textfield'][0].clear()
            r['textfield'][0].send_keys("")
        
        print(f"corrected textfield response: {num}")
            
        sub_butt()
   
    
    print(f"submit button was hit after {time.time() - start_time} sec")
    
    #remove all objects in r
    r = []



#loop for number of responses to the survey
for i in range(0,2):
    
    print(f"Iteration {i}")
    
    #get me a driver
    #driver = webdriver.Chrome(service= Service("chromedriver.exe"), chrome_options=chrome_options)
    driver = webdriver.Chrome(service= Service("chromedriver.exe"))
    #get me a survey
    #driver.get("https://umfragen.iab.de/goto/subo1.de")
    driver.get("https://umfragen.iab.de/goto/HOPPw1")

    #keep responding until the end of the survey
    while True:
        try:
            driver.current_url
            respond()
                
        except WebDriverException:
            print("Webdriver not active or closed, Exiting")
            break


# driver = webdriver.Chrome(service= Service("chromedriver.exe"))
# driver.get("https://umfragen.iab.de/goto/HOPPw1")