import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def extract_plant_data(url, name):
    """
    -Initialises driver
    -Navigate to url
    -Save all img elements inside column to DF
    """
    plant_info = []

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(15)

    col_divs = driver.find_elements(By.XPATH, "//div[@class='col' and @style='width:279px']")


    for col_div in col_divs:
        img_elements = col_div.find_elements(By.TAG_NAME, 'img')

        for img_element in img_elements:
            img_src = img_element.get_attribute('src')
            plant_info.append(img_src)


    driver.quit()

    df = pd.DataFrame(plant_info)
    df.to_csv(f'data/{name}.csv')

    print(f'You have collected {len(plant_info)} images of {name}')
