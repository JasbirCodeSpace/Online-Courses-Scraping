import csv
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:\\Users\\JASBIR-PC\\Desktop\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://www.coursera.org/browse/')

course_link=[]
course_name=[]
course_rating=[]
ratings=[]

def open_new_specialization(link):
	#open tab
	driver.execute_script("window.open('');")
	driver.switch_to.window(driver.window_handles[1])
	driver.get(link)
	try:
		if driver.find_elements_by_xpath('//button[@class="Button_clbp6a-o_O-default_rkuhc4-o_O-md_1jvotax m-t-1 d-block m-x-auto"]/span[@class="Box_120drhm-o_O-centerJustify_1nezfbd-o_O-centerAlign_19zvu2s-o_O-displayflex_poyjc"]')[0].is_displayed():
			driver.find_elements_by_xpath('//button[@class="Button_clbp6a-o_O-default_rkuhc4-o_O-md_1jvotax m-t-1 d-block m-x-auto"]/span[@class="Box_120drhm-o_O-centerJustify_1nezfbd-o_O-centerAlign_19zvu2s-o_O-displayflex_poyjc"]')[0].click()
	except Exception as e:
		print(e)

	WebDriverWait(driver, 10).until(find_courselink)	
	WebDriverWait(driver, 10).until(find_coursename)
	WebDriverWait(driver, 10).until(find_courserating)
	WebDriverWait(driver, 10).until(find_coursereviews)

	print("\n")
	
	driver.close()
	driver.switch_to.window(driver.window_handles[0])

def find_courselink(driver):
		# ele = driver.find_elements_by_xpath('//h3[@class="H2_1pmnvep-o_O-weightBold_uvlhiv-o_O-bold_1byw3y2 m-b-2"]')[3].text
		
		try:
			link=driver.find_elements_by_xpath('//a[@data-e2e="course-link"]')
			for i in range(len(link)):
				course_link.append(link[i].get_attribute("href"))
				print(link[i].get_attribute("href"))
			return True		
		except Exception as e:
			return False 
	
def find_coursename(driver):
		# ele = driver.find_elements_by_xpath('//h3[@class="H2_1pmnvep-o_O-weightBold_uvlhiv-o_O-bold_1byw3y2 m-b-2"]')[3].text
		try:
			name = driver.find_elements_by_xpath('//h3[@class="H2_1pmnvep-o_O-weightBold_uvlhiv-o_O-bold_1byw3y2 m-b-2"]')
			for i in range(len(name)):
				course_name.append(name[i].text)
				print(name[i].text)
			return True		
		except Exception as e:
			return False 
def find_courserating(driver):
		# ele = driver.find_elements_by_xpath('//h3[@class="H2_1pmnvep-o_O-weightBold_uvlhiv-o_O-bold_1byw3y2 m-b-2"]')[3].text
		
		try:
			rating = driver.find_elements_by_css_selector("span.H4_1k76nzj-o_O-weightBold_uvlhiv-o_O-bold_1byw3y2")
			for i in range(len(rating)):
				course_rating.append(rating[i].text)
				print(rating[i].text)
			return True		
		except Exception as e:
			return False			

def find_coursereviews(driver):
		# ele = driver.find_elements_by_xpath('//h3[@class="H2_1pmnvep-o_O-weightBold_uvlhiv-o_O-bold_1byw3y2 m-b-2"]')[3].text
		
		try:
			reviews = driver.find_elements_by_xpath('//div[@class="P_gjs17i-o_O-weightNormal_s9jwp5-o_O-fontBody_56f0wi m-r-1s"]/span')
			for i in range(len(reviews)):
				ratings.append(reviews[i].text)
				print(reviews[i].text)
			return True		
		except Exception as e:
			return False



special =  driver.find_elements_by_xpath('//div[@data-e2e="s12n-card-with-micro-dp"]/div/a')
print(len(special))
special_links = []
for specializations in special:
	ele = specializations.get_attribute("href")
	special_links.append(ele)
print(special_links)
print("SPECIALIZATIONS:"+"\n")
for item in special_links:
	print(item)
	print("\n")



print("========== Srapping Courses from Specializations =============")
#Srapping Courses from Specializations
print("SPECIALIZATIONS:"+"\n")
for specialization in special_links:
	print("opening link " + specialization)
	open_new_specialization(specialization)

fields = ['course_link','course_name', 'course_rating', 'ratings']
print(len(course_link))
print(len(course_name))
print(len(course_rating))
print(len(ratings))

rows = list(zip(course_link,course_name,course_rating,ratings))

with open("specCourse.csv", 'w') as csvfile: 
	csvwriter = csv.writer(csvfile,delimiter=',',lineterminator='\n')
	csvwriter.writerow(fields) 
	csvwriter.writerows(rows)	

driver.close()
driver.quit()