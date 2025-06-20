# Load libraries
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Setup selenium
options = webdriver.ChromeOptions ()
options.add_experimental_option('detach', True)
path = '/Users/GillesGuest/PythonLearning/chromedriver/cd4'
browser = webdriver.Chrome(options=options)

# Open website
website= 'https://www.geopost.com/en/lead-time-calculator/'
browser.get(website)
time.sleep(3)
browser.maximize_window
time.sleep(3)

# Accept cookies
accept_cookies = browser.find_element (By.ID, "popin_tc_privacy_button")
browser.execute_script("arguments[0].click();", accept_cookies); # On clique dessus
time.sleep(2)

# Get data from Excel
from_to = pd.read_excel ("C:\\Users\\Gilles Marechal\\OneDrive\\PythonLearning\\DPDScrapping\\DPD_scrapping_data.xlsx")
orig_ctry = from_to.Origin_ctry
orig_ctry_nbr = from_to.Origin_nbr
orig_zip = from_to.Origin_zip
dest_ctry = from_to.Destination_ctry
dest_ctry_nbr = from_to.Destination_nbr
dest_zip = from_to.Destination_zip
OxDx = []

# Loop all lines of the excel https://www.w3schools.com/python/python_lists_loop.asp
for i in range(len(orig_ctry)):
        # enter origin destination pair
    #    orig_drowdown= browser.find_element(By.XPATH, '//*[@id=\"panel-17979-1-0-0\"]/div/div/div[2]/div[1]/div/div[3]/div/i')
        orig_drowdown= browser.find_element(By.XPATH, '//*[@id="panel-17979-1-0-0"]/div/div/div[2]/div/div/div[3]/div/i')
        browser.execute_script("arguments[0].click();", orig_drowdown)
        orig_ctry_selection = browser.find_element(By.XPATH, '//*[@id=\"panel-17979-1-0-0\"]/div/div/div[2]/div/div/div[3]/div/div/div[' + str(orig_ctry_nbr [i]) + ']/span')
        browser.execute_script("arguments[0].click();", orig_ctry_selection)
        orig_zip_box = browser.find_element(By.XPATH, '//*[@id="panel-17979-1-0-0"]/div/div/div[2]/div/div/div[4]/div/input')
        orig_zip_box.send_keys(str(orig_zip[i]))

        dest_drowdown= browser.find_element(By.XPATH, '//*[@id=\"panel-17979-1-0-0\"]/div/div/div[2]/div/div/div[6]/div/i')
        browser.execute_script("arguments[0].click();", dest_drowdown)
        dest_ctry_selection = browser.find_element(By.XPATH, '//*[@id=\"panel-17979-1-0-0\"]/div/div/div[2]/div/div/div[6]/div/div/div[' + str(dest_ctry_nbr [i]) + ']/span')
        browser.execute_script("arguments[0].click();", dest_ctry_selection)
        dest_zip_box = browser.find_element(By.XPATH, '//*[@id="panel-17979-1-0-0"]/div/div/div[2]/div/div/div[7]/div/input')
        dest_zip_box.send_keys(str(dest_zip[i]))

        # push the send button
        calculate_button = browser.find_element(By.XPATH, '//*[@id="panel-17979-1-0-0"]/div/div/div[2]/button')
        calculate_button.click()
        time.sleep(2)

        # get output & manage errors
        try:
          service_name = browser.find_element(By.XPATH, '//*[@id="panel-17979-1-0-0"]/div/div/div[3]/div[2]/div/h1').text
        except:
            service_name = "N/A"
        try:
            Transit_time = browser.find_element(By.XPATH, '//*[@id="panel-17979-1-0-0"]/div/div/div[3]/div[2]/div/p[2]').text
        except:
            Transit_time = "N/A"
        try:
            Station_cutoff_time = browser.find_element(By.XPATH, '//*[@id="panel-17979-1-0-0"]/div/div/div[3]/div[2]/div/p[4]/span').text
        except:
            Station_cutoff_time = "N/A"

        # write output line to csv file
        OxD = {
            "orig_ctry": orig_ctry [i],
            "orig_zip": orig_zip [i],
            "dest_ctry": dest_ctry[i],
            "dest_zip":dest_zip[i],
            "service_name": service_name,
            "Transit_time": Transit_time,
            "Station_cutoff_time": Station_cutoff_time
            }
        OxDx.append(OxD)

        # refresh browser to remove previous values then continue loop
        browser.refresh()
        time.sleep(2)

# Export to Excel
df =pd.DataFrame (OxDx)
Export_path = "C:\\Users\\Gilles Marechal\\OneDrive\\PythonLearning\\DPDScrapping\\"
df.to_excel (Export_path + "DPD_scrapping_output.xlsx", index=False)

# Finish by closing browser
browser.quit()
print ("Finished!")