from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome(executable_path='C:\\Users\\JASBIR-PC\\Desktop\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()
base = "https://www.youtube.com/results?search_query="
qstring = "machine+learning"
driver.get(base+qstring)



for i in range(1,4):
	try:
	    element = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.ID, "video-title"))
	    )
	except Exception as e:
		print(e)
	pagelen = driver.execute_script("window.scrollBy(0,300);")
	time.sleep(6)
	
videos = driver.find_elements_by_xpath('//a[@class="yt-simple-endpoint style-scope ytd-video-renderer"]')
	
print(videos)

for i in videos:
	print(i.get_attribute("title"))
	print(i.get_attribute("href"))

		

