#http://202.120.227.11/F?func=login-session&bor_library=FDU50&login_source=bor-info&bor_id=&bor_verification=

from selenium import webdriver
import time

driver =  webdriver.Chrome()
stu_book_info = {}
all_info = []

def crawlerbody(uid) :
    '''
    爬虫主体结构。根据传入的uid试图登录图书馆。
    登陆成功或失败会进行下一步操作
    args:
    uid int
    '''
    driver.get("http://202.120.227.11/F?func=login-session&bor_library=FDU50&login_source=bor-info&bor_id=&bor_verification=")
    #print(driver.page_source)
    time.sleep(1)
    uidstr=str(uid)
    driver.find_element_by_name("bor_id").send_keys(uidstr)
    driver.find_element_by_name("bor_verification").send_keys("1111")
    driver.find_element_by_xpath("/html/body/form/center/table[1]/tbody/tr[4]/td/input[1]").click()
    #
    time.sleep(1)
    #观察有没有登陆成功
    isok= driver.find_element_by_id("feedbackbar").text
    print(isok)
    if isok=="" :
        print(uidstr+":登陆成功")
        base_info_record(driver)

    else :
        print(uidstr+"登录失败")
    driver.quit()

def base_info_record(driver):
    '''
    记录该学号的有关信息，保存在学号+姓名的csv文件中
    '''
    stu_name_info = driver.find_element_by_xpath('//*[@id="baseinfo"]/a[1]/table[1]/tbody/tr/td[2]').get_attribute('textContent')
    stu_maj_info = driver.find_element_by_xpath('//*[@id="baseinfo"]/a[1]/table[1]/tbody/tr[2]/td[2]').get_attribute('textContent')
    book_num = int(driver.find_element_by_xpath('//*[@id="history"]/table/tbody/tr[2]/td[2]/a').get_attribute('textContent'))
    driver.find_element_by_xpath('//*[@id="history"]/table/tbody/tr[2]/td[2]/a').click()
    book_info_record(driver, book_num,stu_name_info,stu_maj_info)

def book_info_record(driver,book_num,stu_name_info,stu_maj_info):
    '''
    记录该学号的历史借阅情况，保存在还没想好的地方
    '''
    for i in range(0,book_num):
        book_info_writer = driver.find_element_by_xpath('/html/body/center/table[2]/tbody/tr['+ str(i+2)+']/td[2]').get_attribute('textContent')
        book_info_name = driver.find_element_by_xpath('/html/body/center/table[2]/tbody/tr['+str(i+2)+']/td[3]').get_attribute('textContent')
        borrow_time = driver.find_element_by_xpath('/html/body/center/table[2]/tbody/tr['+ str(i+2)+']/td[5]').get_attribute('textContent')

        stu_book_info['stu_name'] = stu_name_info.lstrip()
        stu_book_info['stu_maj'] = stu_maj_info.lstrip()
        stu_book_info['writer'] = book_info_writer
        stu_book_info['bookname'] = book_info_name
        stu_book_info['borrowtime'] = borrow_time
        all_info.append(stu_book_info.copy())
        stu_book_info.clear()

crawlerbody(17307130113)
print(all_info)