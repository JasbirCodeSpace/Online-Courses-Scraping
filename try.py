import csv		
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:\\Users\\JASBIR-PC\\Desktop\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://in.udacity.com/course/self-driving-car-fundamentals-featuring-apollo--ud0419')

course_link = []
course_name = []
course_skill =[]
course_price=[]
desc_1 = []
desc_2 = []
images = []
# desc = driver.find_elements_by_xpath('/html/body/ir-root/ir-content/ir-ndop-b/section[10]/ir-nd-features-b/div/div[2]/div/div/h4')
# desc2 = driver.find_elements_by_xpath('/html/body/ir-root/ir-content/ir-ndop-b/section[10]/ir-nd-features-b/div/div[2]/div/div/p')
# desc3 = driver.find_element_by_xpath('//div[@class="nd-syllabus-term__card"]')
# print(desc3.text)
# print(len(desc))
# for d1,d2 in zip(desc,desc2):
# 	print(d1.get_attribute('innerHTML')+'\n'+d2.get_attribute("innerHTML"))
# 	#nd-syllabus-term__card
#driver.find_element_by_xpath('/html/body/ir-root/ir-content/ir-ndop-b/section[22]/ir-faq-hub/div/div/button').click()
#print(driver.find_element_by_xpath('/html/body/ir-root/ir-content/ir-ndop-b/section[22]/ir-faq-hub/div/div/div[2]/div/ul[1]').get_attribute("textContent"))
# ques = driver.find_elements_by_xpath('//div[@class="faq_wrapper"]/ul/li/h6')
# answ = driver.find_elements_by_xpath('//div[@class="faq_wrapper"]/ul/li/div')
# faqs = ""
# for q,a in zip(ques,answ):
# 	faqs = faqs+q.get_attribute("textContent")+'\n'+a.get_attribute("textContent")+"\n\n\n"
# print(faqs)	
faq = driver.find_element_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/h4').get_attribute('textContent')+'\n\n'+driver.find_element_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/ir-why-take-course-summary').get_attribute('textContent')+'\n\n\n'+driver.find_element_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/ir-why-take-course-details-list/h6').get_attribute('textContent')
t = driver.find_elements_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/ir-why-take-course-details-list/ir-why-take-course-details-item')
for x in t:
	temp = temp+"\n"+x.get_attribute("textContent")
faqs.append(temp)	
driver.close()
driver.quit()