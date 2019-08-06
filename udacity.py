import csv		
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:\\Users\\JASBIR-PC\\Desktop\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://in.udacity.com/courses/all')

course_link = []
course_name = []
course_skill =[]
course_time=[]
course_price=[]
desc_1 = []
desc_2 = []
desc_3=[]
course_image=[]
faqs=[]

def open_course(link):
	driver.execute_script("window.open('');")
	driver.switch_to.window(driver.window_handles[1])
	driver.implicitly_wait(1)
	driver.get(link)

	try:
		print("#case 1")
		course_name.append(driver.find_element_by_xpath('//h1[@class="ng-star-inserted"]').text)
		#course_price.append(driver.find_element_by_xpath('//*[@id="nanodegreeEnrollmentSectionIn"]/div/ir-degree-pricing/div/div/ir-degree-pricing-card/div/div[2]/div/span').text)
		desc_1.append(driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-ndop-b/section[3]/ir-nd-hero-video/div/div[2]/div/h6[2]').text)
		desc_2.append(driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-ndop-b/section[3]/ir-nd-hero-video/div/div[2]/div/p').text)
		#course_time.append(driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-ndop-b/section[5]/ir-nd-overview/div/ul/li[1]').text)
		#desc_3.append(driver.find_element_by_xpath('/html/body/ir-root/ir-content/ir-ndop-b/section[9]/ir-nd-why/div/div[1]').text)
		ques = driver.find_elements_by_xpath('//div[@class="faq_wrapper"]/ul/li/h6')
		answ = driver.find_elements_by_xpath('//div[@class="faq_wrapper"]/ul/li/div')
		faq = ""
		for q,a in zip(ques,answ):
			faq = faq+q.get_attribute("textContent")+'\n'+a.get_attribute("textContent")+"\n\n\n"
		faqs.append(faq)	
		print(course_name[-1])
		print(desc_1[-1])
		print(desc_2[-1])
		#print(course_time[-1])
		print(faqs[-1])
		print("")
		#print(course_price[-1])
	except Exception as e:
		try:
			print("#case 2")
			course_name.append(driver.find_element_by_xpath('//div[@class="content"]/h1').text)
			desc_1.append("NA")		
				
			try:
				temp = driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-ndop-b/section[3]/ir-nanodegree-summary-banner/div/div[2]/div[1]/p').get_attribute("innerText")
				print("try2")
				desc_2.append(temp)
			except Exception as e:
				try:
					temp = driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-ndop-b/section[3]/ir-nd-hero-video/div/div[2]/div/p').text
					print("try3")
					desc_2.append(temp)
				except Exception as e :
					print(e)	
			ques = driver.find_elements_by_xpath('//div[@class="faq_wrapper"]/ul/li/h6')
			answ = driver.find_elements_by_xpath('//div[@class="faq_wrapper"]/ul/li/div')

			faq = ""
			for q,a in zip(ques,answ):
				faq = faq+q.get_attribute("textContent")+'\n'+a.get_attribute("textContent")+"\n\n\n"
			faqs.append(faq)
			print(course_name[-1])
			print(desc_1[-1])
			print(desc_2[-1])
			print(faqs[-1])
			print("")
		except Exception as e:
			try:
				print("#case 3")
				course_name.append(driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-ndop-in/section[3]/ir-new-nanodegree-summary-banner/div/div/div/h1').text)
				#course_price.append(driver.find_element_by_xpath('//*[@id="nanodegreeEnrollmentSectionIn"]/div/ir-degree-pricing/div/div/ir-degree-pricing-card/div/div[2]/div/span').text)
				desc_1.append("NA")
				desc_2.append(driver.find_element_by_xpath('/html/body/ir-root/ir-content/ir-ndop-in/section[3]/ir-new-nanodegree-summary-banner/div/div/div[1]/p').text)
				ques = driver.find_elements_by_xpath('//div[@class="faq_wrapper"]/ul/li/h6')
				answ = driver.find_elements_by_xpath('//div[@class="faq_wrapper"]/ul/li/div')				
				faq = ""
				for q,a in zip(ques,answ):
					faq = faq+q.get_attribute("textContent")+'\n'+a.get_attribute("textContent")+"\n\n\n"
				faqs.append(faq)					
				print(course_name[-1])
				print(desc_1[-1])
				print(desc_2[-1])
				print(faqs[-1])
				#print(course_price[-1])
				print("")

			except Exception as e:
				try:
					print("#case 4")
					course_name.append(driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-course-overview/section[2]/div/ir-course-hero/ir-course-title-card/h1').text)
					desc_1.append("NA")
					desc_2.append(driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-course-overview/section[3]/div/ir-product-summary/div/p').get_attribute("innerText"))
					faq = driver.find_element_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/h4').get_attribute('textContent')+'\n\n'+driver.find_element_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/ir-why-take-course-summary').get_attribute('textContent')+'\n\n\n'+driver.find_element_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/ir-why-take-course-details-list/h6').get_attribute('textContent')
					t = driver.find_elements_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/ir-why-take-course-details-list/ir-why-take-course-details-item')
					temp=faq
					for x in t:
						temp = temp+"\n"+x.get_attribute("textContent")
					faqs.append(temp)	
					print(course_name[-1])
					print(desc_1[-1])
					print(desc_2[-1])
					print(faqs[-1])
					print("")
				except Exception as e:
					try:
						print("#case 5")
						course_name.append(driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-course-in/section/ir-cop-banner/section/div[2]/h1').text)

						desc_1.append("NA")
						desc_2.append(driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-course-in/section/section[1]/ir-cop-course-details/div/div[2]/div/div[1]/div/p').get_attribute("innerText"))
						faq = driver.find_element_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/h4').get_attribute('textContent')+'\n\n'+driver.find_element_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/ir-why-take-course-summary').get_attribute('textContent')+'\n\n\n'+driver.find_element_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/ir-why-take-course-details-list/h6').get_attribute('textContent')
						t = driver.find_elements_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/ir-why-take-course-details-list/ir-why-take-course-details-item')
						temp=faq
						for x in t:
							temp = temp+"\n"+x.get_attribute("textContent")
						faqs.append(temp)						
						print(course_name[-1])
						print(desc_1[-1])
						print(desc_2[-1])
						print(faqs[-1])
						print("")
					except Exception as e:
						try:
							print("#case 6")
							course_name.append(driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-course-overview/section[2]/div/ir-course-hero/ir-course-title-card/h1').text)

							desc_1.append(driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-course-overview/section[2]/div/ir-course-hero/ir-course-title-card/p').get_attribute("innerText"))
							desc_2.append(driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-course-overview/section[3]/div/ir-product-summary/div').get_attribute("innerText"))
							faq = driver.find_element_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/h4').get_attribute('textContent')+'\n\n'+driver.find_element_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/ir-why-take-course-summary').get_attribute('textContent')+'\n\n\n'+driver.find_element_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/ir-why-take-course-details-list/h6').get_attribute('textContent')
							t = driver.find_elements_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/ir-why-take-course-details-list/ir-why-take-course-details-item')
							temp=faq
							for x in t:
								temp = temp+"\n"+x.get_attribute("textContent")
							faqs.append(temp)								
							print(course_name[-1])
							print(desc_1[-1])
							print(desc_2[-1])
							print(faqs[-1])
							print("")
						except Exception as e:
							course_link.remove(link)
								
						
	driver.close()
	driver.switch_to.window(driver.window_handles[0])

courses = driver.find_elements_by_xpath('//h3[@class="card-heading"]/a')
images = driver.find_elements_by_xpath('/html/body/ir-root/ir-content/ir-course-catalog/section[3]/div/div[2]/ir-course-card-catalog/div/div/div/div/ir-catalog-card/div/div[1]/div[1]/div[1]/a/div')
skills = driver.find_elements_by_xpath('/html/body/ir-root/ir-content/ir-course-catalog/section[3]/div/div[2]/ir-course-card-catalog/div/div/div/div/ir-catalog-card/div/div[1]/div[1]/div[2]/div[2]/div[1]')
#course_level = driver.find_elements_by_xpath

print(len(images))
for image in images:
	course_image.append(image.value_of_css_property('background-image')[5:-2])

print(len(skills))
for skill in skills:
	course_skill.append(skill.text)

print(len(courses))
for course in courses:
	course_link.append(course.get_attribute('href'))
	print(course_link[-1])
	open_course(course_link[-1])
	

	
fields = ['course_link','course_name','course_image','Description_1','Description_2','faq']


rows = list(zip(course_link,course_name,course_image,desc_1,desc_2,faqs))

with open("udacity.csv", 'w') as csvfile: 
	csvwriter = csv.writer(csvfile,delimiter=',',lineterminator='\n')
	csvwriter.writerow(fields) 
	csvwriter.writerows(rows)	
driver.close()
driver.quit()