import time 
import pandas as pd 
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import datetime
import psycopg2

#Creating a  selenium driver instance
options = webdriver.ChromeOptions() 
options.headless = True 

options.page_load_strategy = 'none' 

chrome_path = ChromeDriverManager().install() 
chrome_service = Service(chrome_path) 

driver = Chrome(options=options, service=chrome_service) 
driver.implicitly_wait(5)

    
#Extracting the data from the website
driver.get('https://www.smartgriddashboard.com/#all/demand') 
time.sleep(10)
try:
    data = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='stat-box col-3']")))
except:
    print("Error")
demand = {}
for i in data:
    label = i.find_element(By.TAG_NAME, "label").text
    label = label.replace("\n"," ")
    
    value = i.find_elements(By.TAG_NAME, "p")
    check = len(value)
    if check<2:
        value = value[0].text
        
    else:
        value = value[1].text
    demand[label] = value




driver.get('https://www.smartgriddashboard.com/#all/generation') 
time.sleep(10)
try:
    data = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='stat-box col-4']")))
except:
    print("Error")
    
generation = {}

for i in data:
    label = i.find_element(By.TAG_NAME, "label").text
    label = label.replace("\n"," ")
    value = i.find_element(By.TAG_NAME, "p").text
    generation[label] = value
    
demand.update(generation)


driver.get('https://www.smartgriddashboard.com/#all/interconnection') 
time.sleep(10)
try:
    data = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='stat-box interconnection col-3']")))
except:
    print("Error")
connection = {}

for i in data:
    label = i.find_element(By.TAG_NAME, "label").text
    label = label.replace("\n"," ")
    value = i.find_element(By.TAG_NAME, "p").text
    connection[label] = value
    

demand.update(connection)


driver = Chrome(options=options, service=chrome_service) 
driver.implicitly_wait(5)
driver.get('https://www.smartgriddashboard.com/#all/co2') 
time.sleep(10)
try:
    data = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='stat-box col-3']")))
except:
    print("Error")
co2 = {}
count=0

co2_label_code= data[2].find_element(By.TAG_NAME, "label").text
co2_label_text = co2_label_code.replace("\n"," ")
value_code = data[2].find_elements(By.TAG_NAME, "p")
co2_value = value_code[1].text
co2[co2_label_text] = co2_value

demand.update(co2)

now_time = datetime.datetime.now()

current_time ={'time':now_time}
demand.update(current_time)
final_list = list(demand.values())


# Inserting the data into the database 
try:
    connection = psycopg2.connect(user="de8_bhpa29",
                                  password="LOdcz31-",
                                  host="data-sandbox.c1tykfvfhpit.eu-west-2.rds.amazonaws.com",
                                  port="5432",
                                  database="pagila")
    cursor = connection.cursor()

    sql_query = """ INSERT INTO student.bp_electricity (System_Demand_Latest_in_MW, Forecast_Peak_Today_in_MW, Max_System_Demand_All_Time_in_MW, Latest_System_Generation_in_MW, Thermal_Generation_Coal_Gas_Other_percentage, Renewable_Generation_in_percentage, Net_Import, Latest_Net_Interconnection, Latest_Ewic, Latest_Moyle, Latest_CO2_Emissions, Time_stamp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql_query, (final_list[0],final_list[1],final_list[2],final_list[3],final_list[4],final_list[5],final_list[6],final_list[7],final_list[8],final_list[9],final_list[10],final_list[11]))

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into the table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into the table", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Connection is closed")

