import csv
import pyecharts.options as opts
from pyecharts.charts import Line


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

change_count = []
total_count = []

for filename in school_list:
    temp_change_count = 0
    temp_total_count = 0
    name_count = 0
    data = open(filename+"uid_pas.csv","r")
    dataline = csv.reader(data)

    for index,i in enumerate(dataline):
        if(index != 0):
            if(i[1] == "fail"):
                temp_change_count += 1
            temp_total_count += 1

    change_count.append(temp_change_count)
    total_count.append(temp_total_count)

(
    Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add_xaxis(xaxis_data=school_list)
    .add_yaxis(
        series_name="总采样人数",
        y_axis=total_count,
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="min", name="最小值"),
            ]
        ),
        markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(type_="average", name="平均值")]
        ),
    )
    .add_yaxis(
        series_name="更改密码人数",
        y_axis=change_count,
        markpoint_opts=opts.MarkPointOpts(
            data=[opts.MarkPointItem(value=-2, name="周最低", x=1, y=-1.5)]
        ),
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_="average", name="平均值"),
                opts.MarkLineItem(symbol="none", x="90%", y="max"),
                opts.MarkLineItem(symbol="circle", type_="max", name="最高点"),
            ]
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="各院系改密码人数占总人数", subtitle="已做隐私化处理"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        toolbox_opts=opts.ToolboxOpts(is_show=True),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    )
    .render("analysis_password.html")
)