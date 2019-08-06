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
	driver.implicitly_wait(10)
	driver.get(link)

	try:
		print("#case1")
		
		course_name.append(driver.find_element_by_xpath('//div[@class="col-md-8 details"]/h1').text)
		provided_by.append(driver.find_element_by_xpath("//span[@class='providers']").text)
		price.append(driver.find_elements_by_xpath('//div[@class="stat-details"]/div')[0].text)
		duration.append(driver.find_elements_by_xpath('//div[@class="stat-details"]/div')[3].text)

		print(course_name[-1])
		print(provided_by[-1])
		print(duration[-1])
		print(price[-1])

		print("\n")

	except Exception as e:
		try:
			print("#case 2")
			try:
				name = driver.find_element_by_xpath('//span[@class="text-size-heading"]').text
				institute = driver.find_element_by_xpath("//li[@data-field='school']/span[@class='block-list__desc']/a").text
				money = driver.find_element_by_xpath("//li[@data-field='price']/span[@class='block-list__desc']").text
				length = driver.find_element_by_xpath("//li[@data-field='length']/span[@class='block-list__desc']").text
				intro = driver.find_element_by_xpath('//p[@class="course-intro-lead-in"]/span').text
				desc1 = driver.find_element_by_xpath('//*[@id="course-about-area"]/div[1]/div[2]/div/p').text
				desc2 = driver.find_element_by_xpath('//*[@id="what-you-will-learn"]').text
				level_temp = driver.find_element_by_xpath('//li[@data-field="level"]/span[@class="block-list__desc"]').text
				subject_temp = driver.find_element_by_xpath('//li[@data-field="subject"]/span[@class="block-list__desc"]').text
			except Exception as e:
				name = driver.find_element_by_xpath('//*[@id="program-title"]').text
				institute = driver.find_element_by_xpath("//li[@data-field='authoring_organization']/span[@class='block-list__desc']/a").text
				money = driver.find_element_by_xpath("//li[@data-field='price']/span[@class='block-list__desc']/span[aria-label='Current Price']").text
				length = driver.find_element_by_xpath("//li[@data-field='length']/span[@class='block-list__desc']").text
				intro = driver.find_element_by_xpath("//p[@class='banner-description']").text
				desc1 = driver.find_element_by_xpath('//div[@class="overview"]/div').text + '\n'+driver.find_element_by_xpath('//div[@id="job-outlook"]').text
				desc2 = driver.find_element_by_xpath('//div[@id="expected-learning"]/ul').text
				level_temp = "Beginner"
				subject_temp = driver.find_element_by_xpath('//li[@data-field="subject"]/span[@class="block-list__desc"]').text
			course_name.append(name)	
			provided_by.append(institute)
			price.append(money)
			duration.append(length)
			desc.append(intro)
			about1.append(desc1)
			about2.append(desc2)
			level.append(level_temp)
			subject.append(subject_temp)						
			try:
				img = driver.find_element_by_xpath('//div[@class="course-detail-video"]/img').get_attribute("src")
			except Exception as e :
				img = driver.find_element_by_xpath('//div[@class="course-detail-video"]/a/img').get_attribute("src")
			
			image.append(img)
			print(course_name[-1])
			print(provided_by[-1])
			print(duration[-1])
			print(price[-1])
			print(desc[-1])
			print(about1[-1])
			print(about2[-1])
			print(level[-1])
			print(subject[-1])
			print(image[-1])
		except Exception as e:
			print(e)
			try:
				print("#case 3")
				course_name.append(driver.find_element_by_xpath('//h1[@id="program-title"]').text)
				provided_by.append(driver.find_element_by_xpath("//li[@data-field='authoring_organization']/span[@class='block-list__desc']/a").text)
				price.append(driver.find_element_by_xpath("//li[@data-field='price']/span[@class='block-list__desc']/span[@aria-label='Current Price']").text)
				duration.append(driver.find_element_by_xpath("//li[@data-field='length']/span[@class='block-list__desc']").text)
				print(course_name[-1])
				print(provided_by[-1])
				print(duration[-1])
				print(price[-1])
			except Exception as e:
				try:
					print("# case 4 professional")
					WebDriverWait(driver, 10).until(professional)
				except TimeoutException as e:
					print(e)
					return True	
	driver.close()
	driver.switch_to.window(driver.window_handles[0])

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