from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

CommunicationCenter = "Los Angeles"

def reach_page(driver):
    driver.get("https://cad.chp.ca.gov/")  
    wait = WebDriverWait(driver, timeout=2)
        
    firstBox = driver.find_element(by=By.NAME, value="ddlComCenter")
    
    wait.until(lambda _ : firstBox.is_displayed())  

    submit = driver.find_element(by=By.NAME, value="btnCCGo")

    wait.until(lambda _ : submit.is_displayed())  
    
    firstBox.click()
    firstBox.send_keys(CommunicationCenter)
    
    submit.click()
    
    #6 elements per row

def accident_type(driver, collection):
    table = driver.find_elements(by=By.CLASS_NAME, value="gvRow")
    blueRows = driver.find_elements(by=By.CLASS_NAME, value="gvAltRow")
    table.extend(blueRows)
    
    for child in table:
        columns = child.find_elements(by=By.TAG_NAME, value="td")
        
        for c in columns:
            collection.append(c.text)
            
def getData(time, type, location, area, rows):
    length = int(len(rows) / 7)
    map = {}
    
    # for i in range(0, length):
    #     cell = rows[i]
    #     for j in range(0, 120):
    #         if i == 2 + (7 * j):
    #             time.append(cell)
    #         if i == 3 + (7 * j):
    #             type.append(cell)
    #         if i == 4 + (7 * j):
    #             location.append(cell)
    #         if i == 6 + (7 * j):
    #             area.append(cell)      
                
    for i in range(0, length):
        cell = rows[i]        
        multiplier = 7 * i
        
        timeIndex = multiplier + 2
        typeIndex = multiplier + 3
        locationIndex = multiplier + 4
        areaIndex = multiplier + 6
        
        time.append(rows[timeIndex])
        type.append(rows[typeIndex])
        location.append(rows[locationIndex])
        area.append(rows[areaIndex])
        

    
    """
    class Solution {
        public int[] twoSum(int[] nums, int target) {
            HashMap<Integer, Integer> map = new HashMap<>();
        
            for (int i = 0; i < nums.length; i++) {
                int key = target - nums[i];
                if (map.containsKey(key)) {
                    return new int[] {map.get(key), i};
                } else {
                    map.put(nums[i], i);
                }
            }
        
            return new int[] {};
        }
    }
    """
    
def querySequence(driver, rows, time, type, location, area):
    reach_page(driver)
    accident_type(driver, rows)
    getData(time, type, location, area, rows)

def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome()

    rows = []
    time = []
    type = []
    location = []
    area = []


    querySequence(driver, rows, time, type, location, area)
            
    NL = "\n"
    print(f"{time}{NL}")
    print(f"{type}{NL}")
    print(f"{location}{NL}")
    print(f"{area}{NL}")
    
    
    
if __name__ == "__main__":
    main()