import re;
import time;
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
encoding='UTF-8'
plt.rcParams['font.sans-serif']=[u'SimHei']
plt.rcParams['axes.unicode_minus']=False

"""
#热量统计准备
data=pd.read_csv('../data/宝妈营数据5.22-5.28.csv',usecols=[0,2,6,7,9,10,12])
data2=pd.read_csv('../data/宝妈营数据5.29-6.4.csv',usecols=[0,2,6,7,9,10,12])
data3=pd.read_csv('../data/宝妈营数据6.5-6.11.csv',usecols=[0,2,6,7,9,10,12])
data4=pd.read_csv('../data/宝妈营数据6.12-6.18.csv',usecols=[0,2,6,7,9,10,12])
data5=pd.read_csv('../data/宝妈营数据6.19-6.25.csv',usecols=[0,2,6,7,9,10,12])
data=data.append(data2)
data=data.append(data3)
data=data.append(data4)
data=data.append(data5)
data=data.sort_values(['uid','记录日期'])
data=data[data['uid']>44687]
data=data[data['rf']=='总热量摄入量']
data=data.reset_index(drop=True)
data.to_csv('/Users/martin_yan/Desktop/11.csv', index=False, encoding="utf_8_sig")

"""

"""
data=pd.read_csv('/Users/martin_yan/Desktop/每日热量统计.csv',usecols=[0,1,3,5,6])
data = data.drop_duplicates(['uid','记录日期'])
light=pd.read_csv('../data/轻食日统计.csv')
data = pd.merge(data, light, on='姓名')
print(len(data['姓名'].unique()))
lightday=[]

# 判断某天是否为用户的轻食日
for i in range(len(data)):
    month=data.iloc[i]['记录日期'].split('/')[1]
    day=data.iloc[i]['记录日期'].split('/')[2].split(' ')[0]
    light1=data.iloc[i]['轻食日1']
    light2=data.iloc[i]['轻食日2']
    anyday=datetime.datetime(2018,int(month),int(day)).strftime("%w")
    if int(light1)==int(anyday) or int(light2)==int(anyday):
        lightday.append(1)
    else:
        lightday.append(0)
data['是否为轻食日']=lightday
first=data.duplicated('uid',keep='first')
last=data.duplicated('uid',keep='last')

X=[]
bestv=0
va=[]
vb=[]
v=[]
#根据自定义标准去统计用户管理热量较好的天数
#ab两个参数找热量评价的上下限值
#a为轻食日的上下区间参数，b为普通日的上下区间参数
for a in range(1,30):
    x1=[]
    for b in range(1,15):
        day = []
        name = []
        countlight = 0
        countnormal = 0
        for i in range(len(data)):
            number = data.iloc[i]['对比值']
            if data.iloc[i]['是否为轻食日']==1:
                if (number>(100-a)) and (number<(100+a)):
                    countlight=countlight+1
            else:
                if (number>(100-b)) and (number<(100+b)):
                    countnormal=countnormal+1
            if last[i]==False:
                day.append(countnormal+countlight)
                name.append(data.iloc[i]['姓名'])
                countnormal=0
                countlight=0
        dataframe=pd.DataFrame({'姓名':name,'热量管理较好天数':day})
        origianl=pd.read_csv('/Users/martin_yan/Desktop/mean_babymother_data5.22-6.25(体重跨度5周／实际记录平均分).csv',usecols=['姓名','减重值'])
        new = pd.merge(origianl, dataframe, on='姓名')
        print('-----参数a:'+str(a)+',参数b:'+str(b)+'-------')
        value=new['减重值'].corr(new['热量管理较好天数'])
        print(value)
        x1.append(value)
        va.append(a)
        vb.append(b)
        v.append(value)
        if value>bestv:
            bestv=value
            besta=a
            bestb=b

    X.append(x1)
dataframe=pd.DataFrame({'参数a':va,'参数b':vb,'相关性值':v})
dataframe=dataframe.sort_values('相关性值',ascending=False)
print(dataframe.head())
print('最好的相关性:'+str(bestv)+',参数a:'+str(besta)+',参数b:'+str(bestb))
#设置热图大小
plt.figure(1,figsize=(12,8))
#设置热图标题
plt.title(u'热量对比值区间分析')
#绘制热图
sns.heatmap(X)
plt.show()

"""

data=pd.read_csv('/Users/martin_yan/Desktop/每日热量统计.csv',usecols=[0,1,3,5,6])
data = data.drop_duplicates(['uid','记录日期'])
light=pd.read_csv('../data/轻食日统计.csv')
data = pd.merge(data, light, on='姓名')
print(len(data['姓名'].unique()))
lightday=[]

# 判断某天是否为用户的轻食日
for i in range(len(data)):
    month=data.iloc[i]['记录日期'].split('/')[1]
    day=data.iloc[i]['记录日期'].split('/')[2].split(' ')[0]
    light1=data.iloc[i]['轻食日1']
    light2=data.iloc[i]['轻食日2']
    anyday=datetime.datetime(2018,int(month),int(day)).strftime("%w")
    if int(light1)==int(anyday) or int(light2)==int(anyday):
        lightday.append(1)
    else:
        lightday.append(0)
data['是否为轻食日']=lightday
last=data.duplicated('uid',keep='last')

lightday = []
normalday=[]
name = []
countnormal=0
countlight =0
for i in range(len(data)):
    number = data.iloc[i]['对比值']
    if data.iloc[i]['是否为轻食日'] == 1:
        if (number > 73.99) and (number < 126.01):
            countlight = countlight + 1
    else:
        if (number > 89.99) and (number < 110.01):
            countnormal = countnormal + 1
    if last[i] == False:
        normalday.append(countnormal)
        lightday.append(countlight)
        name.append(data.iloc[i]['姓名'])
        countnormal = 0
        countlight = 0
dataframe=pd.DataFrame({'姓名':name,'轻食日热量管理较好天数':lightday,'普通日热量管理较好天数':normalday})
origianl=pd.read_csv('/Users/martin_yan/Desktop/精选用户数据2.csv')
new = pd.merge(origianl, dataframe, on='姓名')
print(new)
numeric_features = new.select_dtypes(include=[np.number])
# 默认为pearson相关系数,另外选择method=spearman表示spearman相关系数等级皮尔逊相关系数，而method=kendall表示另外一种秩相关系数
corr = numeric_features.corr()
print (corr['减重值'].sort_values(ascending=False), '\n')



