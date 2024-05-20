from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

##############
# Parametros 

adress = 'R. João José dos Reis - Jardim Saint Moritz'



chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.google.com/maps')

driver.find_element(By.XPATH,'//*[@id="searchboxinput"]').send_keys(adress)

driver.find_element(By.XPATH,'//*[@id="searchbox-searchbutton"]/span').click()
driver.find_element(By.XPATH,'//*[@id="assistive-chips"]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]/button/div').click()

texto_inicial = driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[3]/div').text

driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[9]/button/div/div[2]/div[1]').text
