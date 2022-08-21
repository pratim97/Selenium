from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

url = 'https://www.google.com/search?q=google&rlz=1C1RXQR_enIN944IN944&oq=google&aqs=chrome..69i57.6839j0j7&sourceid=chrome&ie=UTF-8'

driver.get(url)
wait = WebDriverWait(driver,10)
driver.find_element('css selector','a.gb_1').click()
wait.until(EC.visibility_of_element_located(('id','identifierId'))).send_keys('raypratim209')

driver.save_screenshot(".//ss_1.png")

driver.execute_script("window.scrollTo(0, 360)")