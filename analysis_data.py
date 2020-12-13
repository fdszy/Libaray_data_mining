import csv
import jieba
import jieba.analyse
import pyecharts.options as opts
from pyecharts.charts import WordCloud

school_list=[
"社会科学试验班",
"经济管理试验班",
"技术科学试验班",
"自然科学试验班",
"中国语言文学",
"外国语言文学学院",
"新闻学院",
"数学科学学院",
"哲学学院",
"核科学与技术系",
"经济学院",
"基础医学院",
"药学院",
"临床医学院（筹）",
"护理学院",
"历史学类",
"法学院",
"微电子"]

datas = []
for filename in school_list:
    datas.clear()
    data = open(filename + "uid_bookinfo.csv", "r",encoding='UTF-8')
    dataline = csv.reader(data)
    for index, i in enumerate(dataline):
        print(i)
        print(filename)
        print(index)
        if index == 0:
            continue
        words = jieba.analyse.extract_tags(i[3])
        for word in words:
            flag = 0
            for key in datas:
                if word == key[0]:
                    count = int(key[1]) + 1
                    name = key[0]
                    datas.remove(key)
                    datas.append((name, count))
                    flag = 1
                    break
            if (flag == 0):
                dic = (word, "1")
                datas.append(dic)

    (
        WordCloud()
            .add(series_name="常见词分析", data_pair=datas, word_size_range=[6, 66], )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="常见词分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
            .render(filename+"analysis_data.html")
    )
