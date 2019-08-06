import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:\\Users\\JASBIR-PC\\Desktop\\chromedriver_win32\\chromedriver.exe')

driver.get('https://in.udacity.com/courses/all')

driver.implicitly_wait(50)

course_link = []
course_name =[]
course_level =[]
try:
	courses = driver.find_elements_by_xpath('//h3[@class="card-heading"]/a')
	levels = driver.find_elements_by_xpath('//span["course-level"]/span[@class="capitalize"]')
	skills = driver.find_elements_by_xpath("//span[@class='truncate-content']")
	print(len(courses))
	print(len(levels))
	print(len(skills))
	print(skills)

	for level in levels:	
		course_level.append(level.get_attribute("innerText"))
		print(course_level[-1])
	for skill in skills:
		print(skill.get_attribute("innerText"))
		print("")
except Exception as e:
	print(e)			
driver.close()
driver.quit()