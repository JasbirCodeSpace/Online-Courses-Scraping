from selenium import webdriver

udemy = open("udemy.txt","w")
driver = webdriver.Chrome(executable_path='C:\\Users\\JASBIR-PC\\Desktop\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(10)
driver.get("https://www.udemy.com/")

#driver.find_elements_by_xpath("//button[@class='carousel-arrow next']").click()
links = driver.find_elements_by_xpath("//a[@class='merchandising-course-card--mask--2-b-d']")
for link in links:
	print(link.get_attribute('href'))

driver.close()
driver.quit()

#comment
