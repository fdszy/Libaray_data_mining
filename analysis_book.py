import csv
import pyecharts.options as opts
from pyecharts.charts import Radar

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
"信息科学与工程学院",
"基础医学院",
"药学院",
"临床医学院（筹）",
"护理学院",
"历史学类",
"法学院",
"微电子"]

total_list = []

for filename in school_list:
    temp_total_list = []
    wenke = 0
    like = 0
    jiangwan = 0
    zhangjiang = 0
    fenglin = 0
    data = open(filename + "uid_bookinfo.csv", "r",encoding='UTF-8')
    dataline = csv.reader(data)
    name_count = []
    for index,i in enumerate(dataline):
        if(index != 0):
            if('文科馆' in i[6]):
                wenke += 1
            if('理科馆' in i[6]):
                like += 1
            if('医科馆' in i[6]):
                fenglin += 1
            if('江湾' in i[6]):
                jiangwan += 1
            if('张江' in i[6]):
                zhangjiang += 1

    temp_total_list.append(wenke)
    temp_total_list.append(like)
    temp_total_list.append(fenglin)
    temp_total_list.append(zhangjiang)
    temp_total_list.append(jiangwan)

    newlist = []

    newlist.append(temp_total_list)

    total_list.append(newlist)

data.close()

(
    Radar(init_opts=opts.InitOpts(width="1280px", height="720px", bg_color="#CCCCCC"))
    .add_schema(
        schema=[
            opts.RadarIndicatorItem(name="文科馆", max_=1800),
            opts.RadarIndicatorItem(name="理科馆", max_=1000),
            opts.RadarIndicatorItem(name="江湾图书馆", max_=600),
            opts.RadarIndicatorItem(name="枫林图书馆", max_=600),
            opts.RadarIndicatorItem(name="张江图书馆", max_=600),
        ],
        splitarea_opt=opts.SplitAreaOpts(
            is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
        ),
        textstyle_opts=opts.TextStyleOpts(color="#fff"),
    )

    .add(
        series_name="社会科学试验班",
        data=total_list[0],
        linestyle_opts=opts.LineStyleOpts(color="red"),
    )

    .add(
        series_name="经济管理试验班",
        data=total_list[1],
        linestyle_opts=opts.LineStyleOpts(color="yellow"),
    )

    .add(
        series_name="技术科学试验班",
        data=total_list[2],
        linestyle_opts=opts.LineStyleOpts(color="black"),
    )

    .add(
        series_name="自然科学试验班",
        data=total_list[3],
        linestyle_opts=opts.LineStyleOpts(color="green"),
    )

    .add(
        series_name="中国语言文学",
        data=total_list[4],
        linestyle_opts=opts.LineStyleOpts(color="pink"),
    )

    .add(
        series_name="外国语言文学学院",
        data=total_list[5],
        linestyle_opts=opts.LineStyleOpts(color="orange"),
    )

    .add(
        series_name="新闻学院",
        data=total_list[6],
        linestyle_opts=opts.LineStyleOpts(color="cerulean"),
    )

    .add(
        series_name="数学科学学院",
        data=total_list[7],
        linestyle_opts=opts.LineStyleOpts(color="purple"),
    )

    .add(
        series_name="哲学学院",
        data=total_list[8],
        linestyle_opts=opts.LineStyleOpts(color="camel"),
    )

    .add(
        series_name="核科学与技术系",
        data=total_list[9],
        linestyle_opts=opts.LineStyleOpts(color="brown"),
    )

    .add(
        series_name="经济学院",
        data=total_list[10],
        linestyle_opts=opts.LineStyleOpts(color="amber"),
    )

    .add(
        series_name="基础医学院",
        data=total_list[11],
        linestyle_opts=opts.LineStyleOpts(color="gray"),
    )

    .add(
        series_name="药学院",
        data=total_list[12],
        linestyle_opts=opts.LineStyleOpts(color="blue"),
    )

    .add(
        series_name="临床医学院（筹）",
        data=total_list[13],
        linestyle_opts=opts.LineStyleOpts(color="silver"),
    )

    .add(
        series_name="护理学院",
        data=total_list[14],
        linestyle_opts=opts.LineStyleOpts(color="tan"),
    )

    .add(
        series_name="历史学类",
        data=total_list[15],
        linestyle_opts=opts.LineStyleOpts(color="beige"),
    )

    .add(
        series_name="法学院",
        data=total_list[16],
        linestyle_opts=opts.LineStyleOpts(color="khaki"),
    )

    .add(
        series_name="微电子",
        data=total_list[17],
        linestyle_opts=opts.LineStyleOpts(color="navy"),
    )

    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))

    .render("analysis_book.html")
)

