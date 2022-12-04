from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

driver = webdriver.Chrome(ChromeDriverManager().install())

#search = driver.find_element(By.CLASS_NAME, "desktop-searchBar")
#search.send_keys("shoes")
#search.send_keys(Keys.RETURN)++

sneakers_names=[]
sneakers_ratings=[]

for j in range(1,5):
	driver.get('https://www.myntra.com/shoes?p='+str(j))
	driver.maximize_window()
	driver.implicitly_wait(3)
	products=driver.find_elements(By.CLASS_NAME, "product-product")
	brands=driver.find_elements(By.CLASS_NAME, "product-brand")
	ratings=driver.find_elements(By.CLASS_NAME, "product-ratingsContainer")
	for i in range(0,len(ratings)):
		product = products[i].text
		brand = brands[i].text
		rating = ratings[i].text
		if 'Sneaker' in product:
			sneakers_names.append(brand +" "+product)
			sneakers_ratings.append(rating)		

with open('Sneakers.csv', mode ='w') as csv_file:		
	for k in range(len(ratings)):
		writer = csv.writer(csv_file)
		writer.writerow([sneakers_names[k],'Casual Shoes',sneakers_ratings[k]])
		
