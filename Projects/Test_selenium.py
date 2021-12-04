from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import selenium.webdriver.support.ui as ui

from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(executable_path="E:\PROYECTOS\SC\Projects\chromedriver.exe", options=options)

driver.get("https://www.vivaair.com/#/co/es")

driver.switch_to.frame(driver.find_element(By.XPATH,"/html/body/noscript/iframe"))

origin=Select(driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-home/div/div/div/app-ibe/div/div/div[2]/div[1]/app-station[1]/div[1]/input[1]"))
origin.select_by_visible_text("Barranquilla")
sleep(2)
destiny=Select(driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-home/div/div/div/app-ibe/div/div/div[2]/div[1]/app-station[2]/div/input"))
destiny.select_by_visible_text("Medellín")
sleep(2)
date_origin =Select(driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-home/div/div/div/app-ibe/div/div/div[2]/lib-date-picker/div/div[1]/div/div[2]/input"))
date_origin.select_by_value('5')
sleep(2)
date_destiny =Select(driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-home/div/div/div/app-ibe/div/div/div[2]/lib-date-picker/div/div[2]/div/div[2]/input"))
date_destiny.select_by_value('2')
button=driver.find_elements(By.XPATH,'/html/body/app-root/div[2]/app-home/div/div/div/app-ibe/div/div/div[2]/button/span')
button.click()
sleep(2)
button_selection=driver.find_elements(By.XPATH,'/html/body/app-root/div/app-booking/div/div[2]/app-flight-results/app-flight[1]/div[1]/div[2]')
button_selection.click()
sleep(2)
alert=driver.switch_to.alert
msg=alert.text("Tu vuelo es %s")% button_selection.getText("my text")
print ("Alert shows following message: "+ msg )

sleep(2)
alert.accept()
button_continue = driver.find_elements(By.XPATH,'/html/body/app-root/div/app-booking/div/div[4]/button')
assert "No results found." not in driver.page_source
driver.close()