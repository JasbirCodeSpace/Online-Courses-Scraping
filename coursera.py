import csv
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#for courses : div.course-card-with-micro-dp
#for Specialization : s12n-card-with-micro-dp

driver = webdriver.Chrome(executable_path='C:\\Users\\JASBIR-PC\\Desktop\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://www.coursera.org/browse/')


def open_new_specialization(link):
	#open tab
	driver.execute_script("window.open('');")
	driver.switch_to.window(driver.window_handles[1])
	driver.get(link)
	try:
		if driver.find_elements_by_xpath('//button[@class="Button_clbp6a-o_O-default_rkuhc4-o_O-md_1jvotax m-t-1 d-block m-x-auto"]/span[@class="Box_120drhm-o_O-centerJustify_1nezfbd-o_O-centerAlign_19zvu2s-o_O-displayflex_poyjc"]')[0].is_displayed():
			driver.find_elements_by_xpath('//button[@class="Button_clbp6a-o_O-default_rkuhc4-o_O-md_1jvotax m-t-1 d-block m-x-auto"]/span[@class="Box_120drhm-o_O-centerJustify_1nezfbd-o_O-centerAlign_19zvu2s-o_O-displayflex_poyjc"]')[0].click()
	except Exception as e:
		print('')
	WebDriverWait(driver, 10).until(find_coursename)
	WebDriverWait(driver, 10).until(find_courserating)
	WebDriverWait(driver, 10).until(find_coursereviews)

	print("\n")
    #coursera.write("\n")
	driver.close()
	driver.switch_to.window(driver.window_handles[0])


	
def find_coursename(driver):
		# ele = driver.find_elements_by_xpath('//h3[@class="H2_1pmnvep-o_O-weightBold_uvlhiv-o_O-bold_1byw3y2 m-b-2"]')[3].text
		course_name = driver.find_elements_by_xpath('//h3[@class="H2_1pmnvep-o_O-weightBold_uvlhiv-o_O-bold_1byw3y2 m-b-2"]')
		try:
			coursera_spec.write("\n")
			for i in range(len(course_name)):
				ele = course_name[i].text
				print(ele)
				coursera_spec.write(ele+"\n")
			return True		
		except Exception as e:
			return False 
def find_courserating(driver):
		# ele = driver.find_elements_by_xpath('//h3[@class="H2_1pmnvep-o_O-weightBold_uvlhiv-o_O-bold_1byw3y2 m-b-2"]')[3].text
		course_rating = driver.find_elements_by_css_selector("span.H4_1k76nzj-o_O-weightBold_uvlhiv-o_O-bold_1byw3y2")
		try:
			coursera_spec.write("\n")
			for i in range(len(course_rating)):
				ele = course_rating[i].text
				print(ele)
				coursera_spec.write(ele+"\n")
			return True		
		except Exception as e:
			return False			

def find_coursereviews(driver):
		# ele = driver.find_elements_by_xpath('//h3[@class="H2_1pmnvep-o_O-weightBold_uvlhiv-o_O-bold_1byw3y2 m-b-2"]')[3].text
		ratings = driver.find_elements_by_xpath('//div[@class="P_gjs17i-o_O-weightNormal_s9jwp5-o_O-fontBody_56f0wi m-r-1s"]/span')
		try:
			coursera_spec.write("\n")
			for i in range(len(ratings)):
				ele = ratings[i].text
				print(ele)
				coursera_spec.write(ele+"\n")
			return True		
		except Exception as e:
			return False



def open_new_course(link):
	#open tab

	driver.execute_script("window.open('');")

	driver.switch_to.window(driver.window_handles[1])
	driver.implicitly_wait(10)
	driver.get(link)

	try:
		if driver.find_elements_by_xpath('//button[@class="Button_clbp6a-o_O-default_rkuhc4-o_O-md_1jvotax m-t-1 d-block m-x-auto"]/span[@class="Box_120drhm-o_O-centerJustify_1nezfbd-o_O-centerAlign_19zvu2s-o_O-displayflex_poyjc"]')[0].is_displayed():
			driver.find_elements_by_xpath('//button[@class="Button_clbp6a-o_O-default_rkuhc4-o_O-md_1jvotax m-t-1 d-block m-x-auto"]/span[@class="Box_120drhm-o_O-centerJustify_1nezfbd-o_O-centerAlign_19zvu2s-o_O-displayflex_poyjc"]')[0].click()

		course_name = driver.find_element_by_xpath('//h1[@class="H2_1pmnvep-o_O-weightNormal_s9jwp5-o_O-fontHeadline_1uu0gyz max-text-width-xl m-b-1s"]').text
		course_rating = driver.find_element_by_css_selector("span.H4_1k76nzj-o_O-weightBold_uvlhiv-o_O-bold_1byw3y2").text
		ratings = driver.find_element_by_xpath('//div[@class="P_gjs17i-o_O-weightNormal_s9jwp5-o_O-fontBody_56f0wi m-r-1s"]/span').text

		print(course_name)
		print(course_rating)
		print(ratings)
		print("\n")
		coursera_solo.write(course_name+"\n")
		coursera_solo.write(course_rating+"\n")
		coursera_solo.write(ratings+"\n")
		coursera_solo.write("\n\n")
	except Exception as e:
		print(e)
	# WebDriverWait(driver, 10).until(
	# 	EC.visibility_of(driver.find_element_by_xpath('//h1[@class="H2_1pmnvep-o_O-weightNormal_s9jwp5-o_O-fontHeadline_1uu0gyz max-text-width-xl m-b-1s"]').text)
	
	# )

	driver.close()
	driver.switch_to.window(driver.window_handles[0])


#ALL SPECIALIZATIONS
special =  driver.find_elements_by_xpath('//div[@data-e2e="s12n-card-with-micro-dp"]/div/a')
print(len(special))
special_links = []
for specializations in special:
	ele = specializations.get_attribute("href")
	special_links.append(ele)
print(special_links)
coursera_spec.write("SPECIALIZATIONS:"+"\n")
for item in special_links:
	coursera_spec.write(item)
	coursera_spec.write("\n")
coursera_spec.write("\n\n")

#ALL COURSES
#courses =  driver.find_elements_by_class_name('collection-product-card')
courses = driver.find_elements_by_xpath('//div[@data-e2e="course-card-with-micro-dp"]/div/a')
course_links = []
print(len(courses))
for course in courses:
	ele = course.get_attribute("href")
	course_links.append(ele)
print(course_links)
coursera_solo.write("ALL COURSES:"+"\n")
for item in course_links:
	coursera_solo.write(item)
	coursera_solo.write("\n")
coursera_solo.write("\n\n")	

print("========== Srapping Courses from Specializations =============")
#Srapping Courses from Specializations
coursera_spec.write("SPECIALIZATIONS:"+"\n")
for specialization in special_links:
	print("opening link " + specialization)
	coursera_spec.write(specialization)
	open_new_specialization(specialization)
coursera_spec.write("\n\n")

 

print("========== Srapping Main Page Courses =============")
#Srapping Main Page Courses
coursera_solo.write("ALL COURSES:"+"\n")
for course in course_links:
	print("opening link " + course)
	coursera_solo.write(course)
	open_new_course(course)

coursera_solo.write("\n\n")
print("Done")



driver.close()
driver.quit()