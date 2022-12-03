from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.myntra.com/')
print(driver.title)

search = driver.find_element(By.CLASS_NAME, "desktop-searchBar")
search.send_keys("shoes")
search.send_keys(Keys.RETURN)

search = driver.find_elements(By.XPATH, "//ul[@class='results-base']/li")
sneakers=[]
for a in search:
	#print (a)
	item = a.text.split('\n')
	print(item[4])
#		if 'Sneaker' in item[4]:
#			print(item[4])
#			sneakers.append(item)

#print (sneakers)