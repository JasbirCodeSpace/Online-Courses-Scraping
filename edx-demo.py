from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:\\Users\\JASBIR-PC\\Desktop\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://www.edx.org/course')

course_name=[]
provided_by=[]
duration=[]
course_links=[]
course_images=[]
price=[]
desc=[]
about1=[]
about2=[]
level=[]
subject=[]
display_image=[]
links=[]
def open_new_course(link,img):
	#open tab

	driver.execute_script("window.open('');")
	driver.switch_to.window(driver.window_handles[1])
	driver.implicitly_wait(10)
	driver.get(link)

	try:
		print("#case 2")
		course_name.append(driver.find_element_by_xpath('//span[@class="text-size-heading"]').text)	
		provided_by.append(driver.find_element_by_xpath("//li[@data-field='school']/span[@class='block-list__desc']/a").text)
		price.append(driver.find_element_by_xpath("//li[@data-field='price']/span[@class='block-list__desc']").text)
		duration.append(driver.find_element_by_xpath("//li[@data-field='length']/span[@class='block-list__desc']").text+driver.find_element_by_xpath("//li[@data-field='effort']/span[@class='block-list__desc']").text)
		about1.append(driver.find_element_by_xpath('//p[@class="course-intro-lead-in"]/span').text)
		about2.append(driver.find_element_by_xpath('//*[@id="course-about-area"]/div[1]/div[2]').text)
		level.append(driver.find_element_by_xpath('//li[@data-field="level"]/span[@class="block-list__desc"]').text)
		subject.append(driver.find_element_by_xpath('//li[@data-field="subject"]/span[@class="block-list__desc"]').text)						
		display_image.append(img)
		
		print(course_name[-1])
		print(provided_by[-1])
		print(duration[-1])
		print(price[-1])
		print(about1[-1])
		print(about2[-1])
		print(level[-1])
		print(subject[-1])
		print(display_image[-1])

		print("\n")

	except Exception as e :
		print(e)
	driver.close()
	driver.switch_to.window(driver.window_handles[0])	

courses = driver.find_elements_by_xpath('//a[@class="course-link"]')
images = driver.find_elements_by_xpath('//a[@class="course-link"]/div/img')

for course,image in zip(courses,images):
	course_links.append(course.get_attribute("href"))
	course_images.append(image.get_attribute("src"))

print(len(course_links))
print(len(course_images))
for course,image in zip(course_links,course_images):
	print("opening link " + course)
	open_new_course(course,image)

print(course_name)
print(links)
print(provided_by)
print(price)
print(duration)
print("Done")



driver.close()
driver.quit()			