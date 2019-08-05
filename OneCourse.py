import csv		
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:\\Users\\JASBIR-PC\\Desktop\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://www.coursera.org/browse')

course_name=[]
course_rating=[]
ratings=[]
course_link=[]
i=0
def open_new_course(link,i):
	#open tab

	driver.execute_script("window.open('');")

	driver.switch_to.window(driver.window_handles[1])
	driver.implicitly_wait(10)
	driver.get(link)

	try:
		if driver.find_elements_by_xpath('//button[@class="Button_clbp6a-o_O-default_rkuhc4-o_O-md_1jvotax m-t-1 d-block m-x-auto"]/span[@class="Box_120drhm-o_O-centerJustify_1nezfbd-o_O-centerAlign_19zvu2s-o_O-displayflex_poyjc"]')[0].is_displayed():
			driver.find_elements_by_xpath('//button[@class="Button_clbp6a-o_O-default_rkuhc4-o_O-md_1jvotax m-t-1 d-block m-x-auto"]/span[@class="Box_120drhm-o_O-centerJustify_1nezfbd-o_O-centerAlign_19zvu2s-o_O-displayflex_poyjc"]')[0].click()

		print('1')
		course_name.append(driver.find_element_by_xpath('//h1[@class="H2_1pmnvep-o_O-weightNormal_s9jwp5-o_O-fontHeadline_1uu0gyz max-text-width-xl m-b-1s"]').text)
		print('2')
		course_rating.append(driver.find_element_by_css_selector("span.H4_1k76nzj-o_O-weightBold_uvlhiv-o_O-bold_1byw3y2").text)
		print('3')
		ratings.append(driver.find_element_by_xpath('//div[@class="P_gjs17i-o_O-weightNormal_s9jwp5-o_O-fontBody_56f0wi m-r-1s"]/span').text)
		
		#print(course_name[i-1])
		#print(course_rating[i-1])
		#print(ratings[i-1])
		
		
		#print("\n")
		#coursera_solo.write(course_name+"\n")
		#coursera_solo.write(course_rating+"\n")
		#coursera_solo.write(ratings+"\n")
		#coursera_solo.write("\n\n")
	except Exception as e:
		print(e)
	# WebDriverWait(driver, 10).until(
	# 	EC.visibility_of(driver.find_element_by_xpath('//h1[@class="H2_1pmnvep-o_O-weightNormal_s9jwp5-o_O-fontHeadline_1uu0gyz max-text-width-xl m-b-1s"]').text)
	
	# )

	driver.close()
	driver.switch_to.window(driver.window_handles[0])


courses = driver.find_elements_by_xpath('//div[@data-e2e="course-card-with-micro-dp"]/div/a')
course_links = []
print(len(courses))
for course in courses:
	ele = course.get_attribute("href")
	course_links.append(ele)
print(course_links)



#coursera_solo.write("ALL COURSES:"+"\n")
for course in course_links:
	print("opening link " + course)
	print('check1')
	course_link.append(course)
	print('check2')
	open_new_course(course,i)

print("Done")






fields = ['course_link','course_name', 'course_rating', 'ratings']
#rows = [list(a) for a in zip(course_name, course_rating,ratings)]
print(course_link)
print(course_name)
print(course_rating)
print(ratings)

print(len(course_link))
print(len(course_name))
print(len(course_rating))
print(len(ratings))

rows = list(zip(course_link,course_name,course_rating,ratings))

with open("openCourse1.csv", 'w') as csvfile: 
	csvwriter = csv.writer(csvfile,delimiter=',',lineterminator='\n')
	csvwriter.writerow(fields) 
	csvwriter.writerows(rows)	