from selenium import webdriver
from selenium.webdriver.common.by import By

#KEEP BROWSER OPEN
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
driver=webdriver.Chrome()
driver.get("https://cad.chp.ca.gov/")

def reach_page():
    firstBox = driver.find_element(by=By.NAME, value="ddlComCenter")
    submit = driver.find_element(by=By.NAME, value="btnCCGo")
    firstBox.click()
    firstBox.send_keys("Los Angeles")
    submit.click()
    
    
def accident_type():
    return driver.find_elements(by=By.TAG_NAME, value="td")
    
    
events = []

driver.implicitly_wait(0.5)

reach_page()
list = accident_type()

allText = ""
for row in list:
    allText = allText + f"{row.text}"
    
print(allText)