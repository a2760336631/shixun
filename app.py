
from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px

import csv, re, operator
# from textblob import TextBlob

app = Flask(__name__)

person = {
	'last_name' : 'x',
	'first_name': 'x',
	'address' : 'xx大学',
	'job': '软件工程师',
	'tel': '0000001',
	'email': '11111@qq.com.com',
	'dev':'我叫xx,今年22岁。毕业于xx大学，想求职公司的软件设计师职位。',
	'description' : '本人有比较强的自我学习能力，学习知识速度比较快。性格比较积极乐观，善于与其他人交流沟通。',
	'skill':'精通面向对象编程和计算相关的数学。精通java和python,学习过对Android方面的开发',
	'interests1':'小型独立编码项目（半专业）,音乐,视频,大型多人在线游戏。',
	'work':'一个Android的无障碍应用程序，一个我随意使用的博客平台的桌面主题，以及一个摄影项目，详细描述了城市环境中自然和人工的相互作用。',
	'contact':[
		{
			'way':'电话',
			'lk':'111111'
		},
		{
			'way':'邮箱',
			'lk':'2222@qq.com'
		}
	],
	'social_media' : [
		{
			'link': 'https://www.facebook.com/',
			'icon' : 'fa-facebook-f'
		},
		{
			'link': 'https://github.com/a11111',
			'icon' : 'fa-github'
		},
		{
			'link': 'linkedin.com/in/',
			'icon' : 'fa-linkedin-in'
		},
		{
			'link': 'https://twitter.com/',
			'icon' : 'fa-twitter'
		}
	],
	'img': 'img/img_nono.jpg',
	'experiences' : [
		{
			'title' : 'python爬虫',
			'company': 'xx国际有限公司',
			'description' : '对网页的视频信息进去爬取，并对爬取的数据进行分析，查看热门视频数据与什么相关.',
			'timeframe' : 'July 2018 - November 2019'
		},
		{
			'title' : '购物商城',
			'company': 'xx国际有限公司',
			'description' : '添加登录注册系统和商品添加 ',
			'timeframe' : 'February 2017 - Present'
		},
		{
			'title' : '购票系统',
			'company': 'xx国际有限公司',
			'description' : '添加购票信息和对机票的添加删除',
			'timeframe' : 'October 2015 - October 2016'
		}
	],
	'education' : [
		{
			'university': 'xx大学',
			'degree': '学士',
			'description' : '软件工程专业',
			'mention' : 'Bien',
			'timeframe' : '2015 - 2016'
		}
	],
	'programming_languages' : {
		'HMTL' : ['fa-html5', '100'], 
		'CSS' : ['fa-css3-alt', '100'], 
		'SASS' : ['fa-sass', '90'], 
		'JS' : ['fa-js-square', '90'],
		'Wordpress' : ['fa-wordpress', '80'],
		'Python': ['fa-python', '70'],
		'Mongo DB' : ['fa-database', '60'],
		'MySQL' : ['fa-database', '60'],
		'NodeJS' : ['fa-node-js', '50']
	},
	'languages' : {'French' : 'Native', 'English' : 'Professional', 'Spanish' : 'Professional', 'Italian' : 'Limited Working Proficiency'},
	'interests' : ['Dance', 'Travel', 'Languages']
}

@app.route('/')
def cv(person=person):
	return render_template('index1.html', person=person)




@app.route('/callback', methods=['POST', 'GET'])
def cb():
	return gm(request.args.get('data'))
	 
@app.route('/chart')
def index():
	return render_template('chartsajax.html',  graphJSON=gm(),graphJSON1=gm1(),graphJSON2=gm2(),graphJSON3=gm3(),graphJSON4=gm4(),graphJSON5=gm5())
@app.route('/chart1')
def index1():
	return render_template('histogram.html',  graphJSON=tip(),graphJSON1=tip1(),graphJSON2=tip2(),graphJSON3=tip3(),graphJSON4=tip4())


def gm():
	df = pd.read_csv('penguins2.csv',encoding='gbk')

	# fig = px.line(df[df['country']==country], x="score", y="account")
	fig = px. scatter(df, x="Flipper Length (mm)", y="Body Mass (g)", color ="Species");

	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON
def gm1():
	df = pd.read_csv('penguins2.csv',encoding='gbk')

	# fig = px.line(df[df['country']==country], x="score", y="account")
	fig = px.histogram(df, x="Culmen Depth (mm)", y="Culmen Length (mm)",color="Species")
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON
def gm2():
	df = pd.read_csv('penguins2.csv',encoding='gbk')

	# fig = px.line(df[df['country']==country], x="score", y="account")
	fig = px.scatter_matrix(df, dimensions= ["Body Mass (g)" ,"Flipper Length (mm)","Culmen Depth (mm)","Culmen Length (mm)"],color="Species");
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON
def gm3():
	df = pd.read_csv('penguins2.csv',encoding='gbk')

	# fig = px.line(df[df['country']==country], x="score", y="account")
	fig = px.parallel_coordinates(df, color="species_id", labels={"species_id": "Species",
									"Body Mass (g)": "Body Mass", "Flipper Length (mm)": "Flipper Length",
									"Culmen Depth (mm)": "Culmen Depth", "Culmen Length (mm)": "Culmen Length", },
										color_continuous_scale=px.colors.diverging.Tealrose, color_continuous_midpoint=2)

	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON
def gm4():
	df = pd.read_csv('penguins2.csv',encoding='gbk')

	# fig = px.line(df[df['country']==country], x="score", y="account")
	fig = px.density_contour(df, x="Culmen Depth (mm)", y= "Culmen Length (mm)" ,color="Species")
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON
def gm5():
	df = pd.read_csv('penguins2.csv',encoding='gbk')

	# fig = px.line(df[df['country']==country], x="score", y="account")
	fig =px.density_heatmap( df,x="Culmen Depth (mm)",y="Culmen Length (mm)",  marginal_y="rug",marginal_x="histogram"   )
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON
def tip():
	df = pd.read_csv('tips.csv',encoding='gbk')
	total_bill_byday = df.groupby(by="day")["total_bill"].sum().reset_index()
	# fig = px.line(df[df['country']==country], x="score", y="account")
	fig = px.pie(total_bill_byday, # 绘图数据
			 names="day",  # 每个组的名字
			 values="total_bill"  # 组的取值
			)
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON
def tip1():
	df = pd.read_csv('tips.csv',encoding='gbk')
	# fig = px.line(df[df['country']==country], x="score", y="account")
	fig=px.histogram(
		df,  # 绘图数据
		x="sex",  # 指定两个数轴
		y="tip",
		histfunc="avg",  # 直方图函数：均值
		color="smoker",  # 颜色取值
		barmode="group",  # 柱状图模式
		facet_row="time",  # 横纵纵轴的字段设置
		facet_col="day",
		category_orders={"day":["Thur","Fri","Sat","Sun"],  # 分类
										 "time":["Lunch","Dinner"]})
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON
def tip2():
	df = pd.read_csv('tips.csv',encoding='gbk')
	# fig = px.line(df[df['country']==country], x="score", y="account")
	fig=px.box(df,  # 数据集
			 x="day",  # 横轴数据
			 y="total_bill",  # 纵轴数据
			 color="smoker",  # 颜色
			 notched=True)  # 连接处的锥形部分显示出来
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON
def tip3():
	df = pd.read_csv('tips.csv',encoding='gbk')
	# fig = px.line(df[df['country']==country], x="score", y="account")
	fig=px. violin(df, y="tip",x="smoker" ,color="sex",box=True, points="all",hover_data=df.columns)
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON
def tip4():
	df = pd.read_csv('tips.csv',encoding='gbk')
	# fig = px.line(df[df['country']==country], x="score", y="account")
	fig=px.parallel_categories(
    df,  # 传入数据
    color="size",  # 颜色取值
    color_continuous_scale=px.colors.sequential.Inferno # 颜色变化趋势
)
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON
@app.route('/senti')
def main():
	text = ""
	values = {"positive": 0, "negative": 0, "neutral": 0}

	with open('ask_politics.csv', 'rt') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
		for idx, row in enumerate(reader):
			if idx > 0 and idx % 2000 == 0:
				break
			if  'text' in row:
				nolinkstext = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '', row['text'], flags=re.MULTILINE)
				text = nolinkstext

			blob = TextBlob(text)
			for sentence in blob.sentences:
				sentiment_value = sentence.sentiment.polarity
				if sentiment_value >= -0.1 and sentiment_value <= 0.1:
					values['neutral'] += 1
				elif sentiment_value < 0:
					values['negative'] += 1
				elif sentiment_value > 0:
					values['positive'] += 1

	values = sorted(values.items(), key=operator.itemgetter(1))
	top_ten = list(reversed(values))
	if len(top_ten) >= 11:
		top_ten = top_ten[1:11]
	else :
		top_ten = top_ten[0:len(top_ten)]

	top_ten_list_vals = []
	top_ten_list_labels = []
	for language in top_ten:
		top_ten_list_vals.append(language[1])
		top_ten_list_labels.append(language[0])

	graph_values = [{
					'labels': top_ten_list_labels,
					'values': top_ten_list_vals,
					'type': 'pie',
					'insidetextfont': {'color': '#FFFFFF',
										'size': '14',
										},
					'textfont': {'color': '#FFFFFF',
										'size': '14',
								},
					}]

	layout = {'title': '<b>意见挖掘</b>'}

	return render_template('sentiment.html', graph_values=graph_values, layout=layout)


if __name__ == '__main__':
	app.run(debug= True,port=5000,threaded=True)
