from selenium import webdriver
from selenium.webdriver.common.service import Service

se = Service(executable='D:\selenium\chromedriver')
driver = webdriver.Chrome(service=se)

url='http://demostore.supersqa.com'
driver.get(url)

#i am learning selenium and git, next lets do the testing concepts revision