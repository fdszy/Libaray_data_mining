#http://202.120.227.11/F?func=login-session&bor_library=FDU50&login_source=bor-info&bor_id=&bor_verification=
import csv
from selenium import webdriver
import time

driver =  webdriver.Chrome()
stu_book_info = {}
#all_info = []
#
def crawlerbody(uid,password) :
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
    driver.find_element_by_name("bor_verification").send_keys(password)
    driver.find_element_by_xpath("/html/body/form/center/table[1]/tbody/tr[4]/td/input[1]").click()
    #
    time.sleep(1)
    #观察有没有登陆成功
    isok= driver.find_element_by_id("feedbackbar").text
    if isok=="" :
        #print(uidstr+":登陆成功")
        uid_pas_csv.writerow([uidstr,password])
        base_info_record(driver)

    else :
        #print(uidstr+":登录失败")
        uid_pas_csv.writerow([uidstr,'fail'])
    #driver.quit()

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
    记录该学号的历史借阅情况
    '''

    #网页只会显示100本书，所以这里不能超过100
    if book_num >100 :
        book_num=100

    for i in range(0,book_num):
        book_info_writer = driver.find_element_by_xpath('/html/body/center/table[2]/tbody/tr['+ str(i+2)+']/td[2]').get_attribute('textContent')

        book_info_name = driver.find_element_by_xpath('/html/body/center/table[2]/tbody/tr['+str(i+2)+']/td[3]').get_attribute('textContent')


#

        borrow_time = driver.find_element_by_xpath('/html/body/center/table[2]/tbody/tr['+ str(i+2)+']/td[5]').get_attribute('textContent')

        #driver.find_element_by_xpath('/html/body/center/table[2]/tbody/tr['+str(i+2)+']/td[1]/a').click()
        #book_index=driver.find_element_by_xpath("/html/body/center/table[2]/tbody/tr[3]/td[2]").get_attribute('textContent')
        #driver.back()       
        
        branch_of_lib=driver.find_element_by_xpath('/html/body/center/table[2]/tbody/tr['+ str(i+2)+']/td[10]').get_attribute('textContent')

        stu_book_info['stu_name'] = stu_name_info.lstrip()
        stu_book_info['stu_maj'] = stu_maj_info.lstrip()
        stu_book_info['writer'] = book_info_writer
        stu_book_info['bookname'] = book_info_name
        #todo
        stu_book_info['borrowtime'] = borrow_time

        stu_name= stu_name_info.lstrip()
        stu_maj= stu_maj_info.lstrip()
        writer= book_info_writer
        bookname= book_info_name
        bookindex="nan"
        borrowtime= borrow_time
        branchoflib=branch_of_lib

        #all_info.append(stu_book_info.copy())
        #stu_book_info.clear()
        uid_bookinfo_csv.writerow([stu_name,stu_maj,writer,bookname,bookindex,borrowtime,branchoflib])


school_list=[
("709","社会科学试验班"),
("710","经济管理试验班"),
("713","技术科学试验班"),
("711","自然科学试验班"),
("011","中国语言文学"),
("012","外国语言文学学院"),
("013","新闻学院"),
("018","数学科学学院"),
("016","哲学学院"),
("020","核科学与技术系"),
("068","经济学院"),
("072","信息科学与工程学院"),
("101","基础医学院"),
("103","药学院"),
("105","临床医学院（筹）"),
("117","护理学院"),
("708","历史学类"),
("027","法学院"),
("075","微电子")]

jd=0

for i in school_list :
    print(i[0])
    uid_pas = open(i[1]+'uid_pas.csv','w')
    uid_pas_csv=csv.writer(uid_pas)
    uid_pas_csv.writerow(['uid','password'])


    uid_bookinfo = open(i[1]+'uid_bookinfo.csv','w')
    uid_bookinfo_csv=csv.writer(uid_bookinfo)
    uid_bookinfo_csv.writerow(['sut_name','stu_maj','writer','bookname','bookindex','borrowtime','branchoflib'])
    for j in range(1,51):
        try:
            crawlerbody(   int("1730"+i[0]+"0000")  + j ,1111)
        except BaseException as e:
            print("出现异常")
            print(e)
            print("1730"+i[0]+"0000")
        jd=jd+1
        print(jd/(19*50))
        print(str(jd)+"/"+str(19*50))

crawlerbody(16307110315,1112)
#print(all_info)