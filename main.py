from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get("https://cad.chp.ca.gov/")

def reach_page():
    firstBox = driver.find_element(by=By.NAME, value="ddlComCenter")
    submit = driver.find_element(by=By.NAME, value="btnCCGo")
    firstBox.click()
    firstBox.send_keys("Los Angeles")
    submit.click()
    
    
def accident_type():
    return driver.find_elements(by=By.TAG_NAME, value="td")
    
    


driver.implicitly_wait(0.5)
reach_page()

list = accident_type()

print(f"List: {list}")
