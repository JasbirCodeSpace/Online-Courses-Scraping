import csv		
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path='C:\\Users\\JASBIR-PC\\Desktop\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://www.edx.org/course')
course_name=[]
provided_by=[]
duration=[]
course_links=[]
price=[]
desc=[]
about1=[]
about2=[]
level=[]
subject=[]
image=[]
def open_new_course(link):
	#open tab

	driver.execute_script("window.open('');")
	driver.switch_to.window(driver.window_handles[1])
	driver.implicitly_wait(2)
	driver.get(link)
	try:
		print("# case 4 professional")
		WebDriverWait(driver, 2).until(professional)
	except TimeoutException as e:
		print(e)

def professional(driver):
	try:
		link=driver.find_elements_by_xpath('//a[@class="card-link"]')
		money = driver.find_elements_by_xpath('//div[@class="card-stat"]/div[@class="card-detail"]/span')
		effort = driver.find_elements_by_xpath('//div[@class="card-stat"]/div[@class="card-detail"]/span')
		for i in range(len(link)):
			course_links.append(link[i].get_attribute("href"))
			course_name.append(link[i].text)
			price.append(price[i].text)
			duration.append(effort[i].text)
			print(course_links[-1])
			print(course_name[-1])
			print(price[-1])
		return True		
	except Exception as e:
		print(e)
		return False 	

courses = driver.find_elements_by_xpath('//a[@class="course-link"]')
print(len(courses))

for course in courses:
	ele = course.get_attribute("href")
	course_links.append(ele)
	print(ele)




for course in course_links:
	print("opening link " + course)
	open_new_course(course)

print(course_name)
print(course_links)
print(provided_by)
print(price)
print(duration)
print("Done")



driver.close()
driver.quit()		