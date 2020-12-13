import csv
import pyecharts.options as opts
from pyecharts.charts import Bar3D


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

date = [
    "2017",
    "2018",
    "2019",
    "2020"
]

time_data = []

for big_index,filename in enumerate(school_list):
    data = open(filename + "uid_bookinfo.csv", "r",encoding='UTF-8')
    dataline = csv.reader(data)
    seven_count = 0
    eight_count = 0
    nine_count = 0
    ten_count = 0
    for index,i in enumerate(dataline):
        if(i[5][0:4] == '2017'):
            seven_count += 1
        if(i[5][0:4] == '2018'):
            eight_count += 1
        if(i[5][0:4] == '2019'):
            nine_count += 1
        if(i[5][0:4] == '2020'):
            ten_count += 1
    time_data.append([big_index,0,seven_count])
    time_data.append([big_index,1,eight_count])
    time_data.append([big_index,2,nine_count])
    time_data.append([big_index,3,ten_count])
print(time_data)
(
    Bar3D(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(
        series_name="",
        data=time_data,
        xaxis3d_opts=opts.Axis3DOpts(type_="category", data=school_list),
        yaxis3d_opts=opts.Axis3DOpts(type_="category", data=date),
        zaxis3d_opts=opts.Axis3DOpts(type_="value"),
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(
            max_=800,
            range_color=[
                "#313695",
                "#4575b4",
                "#74add1",
                "#abd9e9",
                "#e0f3f8",
                "#ffffbf",
                "#fee090",
                "#fdae61",
                "#f46d43",
                "#d73027",
                "#a50026",
            ],
        )
    )
    .render("analysis_time.html")
)

