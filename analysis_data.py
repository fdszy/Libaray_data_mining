import os
import argparse
from selenium import webdriver
import time
import pyecharts.options as opts
from pyecharts.charts import WordCloud
import jieba
import jieba.analyse

parser = argparse.ArgumentParser()
parser.add_argument('--userstring',default='17307130121')

opt = parser.parse_args()


def crawlerbody(uid, password):
    '''
    爬虫主体结构。根据传入的uid试图登录图书馆。
    登陆成功或失败会进行下一步操作
    args:
    uid int
    '''
    driver.get(
        "http://202.120.227.11/F?func=login-session&bor_library=FDU50&login_source=bor-info&bor_id=&bor_verification=")
    # print(driver.page_source)
    time.sleep(1)
    uidstr = str(uid)
    driver.find_element_by_name("bor_id").send_keys(uidstr)
    driver.find_element_by_name("bor_verification").send_keys(password)
    driver.find_element_by_xpath("/html/body/form/center/table[1]/tbody/tr[4]/td/input[1]").click()
    #
    time.sleep(1)
    # 观察有没有登陆成功
    isok = driver.find_element_by_id("feedbackbar").text
    if isok == "":
        print(uidstr+":登陆成功")
        base_info_record(driver)

    else:
        print(uidstr+":登录失败")
    # driver.quit()


def base_info_record(driver):
    '''
    记录该学号的有关信息，保存在学号+姓名的csv文件中
    '''
    stu_name_info = driver.find_element_by_xpath('//*[@id="baseinfo"]/a[1]/table[1]/tbody/tr/td[2]').get_attribute(
        'textContent')
    stu_maj_info = driver.find_element_by_xpath('//*[@id="baseinfo"]/a[1]/table[1]/tbody/tr[2]/td[2]').get_attribute(
        'textContent')
    book_num = int(
        driver.find_element_by_xpath('//*[@id="history"]/table/tbody/tr[2]/td[2]/a').get_attribute('textContent'))
    driver.find_element_by_xpath('//*[@id="history"]/table/tbody/tr[2]/td[2]/a').click()
    book_info_record(driver, book_num, stu_name_info, stu_maj_info)


def book_info_record(driver, book_num, stu_name_info, stu_maj_info):
    '''
    记录该学号的历史借阅情况
    '''
    data = []
    # 网页只会显示100本书，所以这里不能超过100
    if book_num > 100:
        book_num = 100

    for i in range(0, book_num):
        book_info_writer = driver.find_element_by_xpath(
            '/html/body/center/table[2]/tbody/tr[' + str(i + 2) + ']/td[2]').get_attribute('textContent')

        book_info_name = driver.find_element_by_xpath(
            '/html/body/center/table[2]/tbody/tr[' + str(i + 2) + ']/td[3]').get_attribute('textContent')

        #

        borrow_time = driver.find_element_by_xpath(
            '/html/body/center/table[2]/tbody/tr[' + str(i + 2) + ']/td[5]').get_attribute('textContent')

        # driver.find_element_by_xpath('/html/body/center/table[2]/tbody/tr['+str(i+2)+']/td[1]/a').click()
        # book_index=driver.find_element_by_xpath("/html/body/center/table[2]/tbody/tr[3]/td[2]").get_attribute('textContent')
        # driver.back()

        branch_of_lib = driver.find_element_by_xpath(
            '/html/body/center/table[2]/tbody/tr[' + str(i + 2) + ']/td[10]').get_attribute('textContent')



        stu_name = stu_name_info.lstrip()
        stu_maj = stu_maj_info.lstrip()
        writer = book_info_writer
        bookname = book_info_name
        bookindex = "nan"
        borrowtime = borrow_time
        branchoflib = branch_of_lib

        words = jieba.analyse.extract_tags(bookname, topK=2, withWeight=False)
        for word in words:
            flag = 0
            for key in data:

                if word == key[0]:
                    count = int(key[1])+1
                    name = key[0]
                    data.remove(key)
                    data.append((name,count))
                    flag = 11
                    break
            if(flag == 0):
                dic = (word,"1")
                data.append(dic)

    (
        WordCloud()
            .add(series_name="常见词分析", data_pair=data, word_size_range=[6, 66],)
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="常见词分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
            .render("analysis_data.html")
    )




if __name__ == "__main__":
    driver = webdriver.Chrome()
    crawlerbody(opt.userstring, 1111)
    driver.close()