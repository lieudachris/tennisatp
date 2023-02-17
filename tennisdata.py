import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_argument('disable-infobars')

chrome_path = ChromeDriverManager().install()

options = Options()
options.add_argument("--window-size=1920x1080")
options.add_argument("--verbose")

#driver = webdriver.Chrome(options=options, executable_path = chrome_path)

chrome_service = webdriver.chrome.service.Service(chrome_path)
driver = webdriver.Chrome(service=chrome_service)

driver.get("http://www.ultimatetennisstatistics.com/playerProfile?playerId=4742")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//ul[@id='playerPills']//a[@class='dropdown-toggle'][normalize-space()='Statistics']"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='dropdown-menu']//a[@id='statisticsPill'][normalize-space()='Statistics']"))).click()
statistics_items = WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, "//table[@class='table table-condensed table-hover table-striped']//tbody//tr/td")))
statistics_value = WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, "//table[@class='table table-condensed table-hover table-striped']//tbody//tr//following::th[1]")))
for item, value in zip(statistics_items, statistics_value):
    print('{} {}'.format(item.text, value.text))