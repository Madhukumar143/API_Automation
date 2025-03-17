import time
from datetime import datetime
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_fill_timesheet():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")  # Incognito mode
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://terralogic.paxanimi.ai/login")
    for _ in range(5):
        pyautogui.hotkey('ctrl', '-')
    driver.find_element(By.XPATH,"//input[@id='basic_userEmail']").send_keys("madhukumar.hm@terralogic.com")
    driver.find_element(By.XPATH,"//input[@id='basic_password']").send_keys("Madhu@3442")
    driver.find_element(By.XPATH,"//div[contains(text(),'Sign In')]").click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//p[contains(text(),'Hello')]")))
    today_day = datetime.today().day
    start_time = "9:00 am"
    end_time ="6:00 pm"
    project_name = "GIIS Mobile Apps - GIIS PTE"
    task_name = "Testing GIIS Mobile Apps"
    Description = (
        "1. notification Test cases : ongoing\n"
        "2. message automation  - 2 test cases completed\n"
        "3. calendar module import calendar : Completed (Only UI)\n"
        "4. Message module Comments part : Completed (Only UI)"
    )

    click_on_dayin_home_page = f"//span[normalize-space()='{today_day}']/following-sibling::img"

    driver.find_element(By.XPATH,click_on_dayin_home_page).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'Add Task')]")))
    driver.find_element(By.XPATH,"//div[contains(text(),'Add Task')]").click()
    def scroll_inside_dropdown(target_item,dropdown_view_locator):
        # Locate the target item inside the dropdown
        for i in range(60):
            count = len(driver.find_elements(By.XPATH,f"//div[@title='{target_item}']"))
            def is_clickable():
                try:
                    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, f"//div[@title='{target_item}']")))
                    return True
                except:
                    return False
            if count>0:
                if is_clickable():
                    driver.find_element(By.XPATH, f"//div[@title='{target_item}']").click()
                    break
                else:
                    driver.execute_script("arguments[0].scrollTop += 250", dropdown_view_locator)
            else:
                driver.execute_script("arguments[0].scrollTop += 250", dropdown_view_locator)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='ant-select-selector'])[1]")))
    drop_down = driver.find_element(By.XPATH, "(//div[@class='ant-select-selector'])[1]")
    drop_down.click()
    dropdown_menu = driver.find_element(By.XPATH, "(//div[@class='rc-virtual-list-holder'])[1]")
    scroll_inside_dropdown(start_time,dropdown_menu)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='ant-select-selector'])[2]")))
    drop_down = driver.find_element(By.XPATH, "(//div[@class='ant-select-selector'])[2]")
    drop_down.click()
    dropdown_menu = driver.find_element(By.XPATH, "(//div[@class='rc-virtual-list-holder'])[2]")
    scroll_inside_dropdown(end_time, dropdown_menu)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='ant-select-selector'])[3]")))
    drop_down = driver.find_element(By.XPATH, "(//div[@class='ant-select-selector'])[3]")
    drop_down.click()
    time.sleep(1)
    dropdown_menu = driver.find_element(By.XPATH, "(//div[@class='rc-virtual-list-holder'])[3]")
    scroll_inside_dropdown(project_name, dropdown_menu)
    driver.find_element(By.XPATH,"//input[@placeholder='Enter the task name']").send_keys(task_name)
    driver.find_element(By.XPATH, "//textarea[@placeholder='Enter the description']").send_keys(Description)
    driver.find_element(By.XPATH,"//button[contains(@type,'submit')]").click()
    time.sleep(3)

