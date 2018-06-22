import re;
import time;
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
#abcd四个参数找热量评价的上下限值
encoding='UTF-8'
plt.rcParams['font.sans-serif']=[u'SimHei']
plt.rcParams['axes.unicode_minus']=False
data=pd.read_csv('/Users/martin_yan/Desktop/每日热量统计.csv',usecols=[0,1,3,5,6])
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
vc=[]
vd=[]
v=[]
origianl=pd.read_csv('/Users/martin_yan/Desktop/mean_babymother_data5.22-6.18.csv',usecols=['姓名','减重值'])
#根据自定义标准去统计用户管理热量较好的天数
for a in range(20,25):
    for b in range(20,25):
        x1 = []
        for c in range(5,12):
            for d in range(5,12):
                day = []
                name = []
                countlight = 0
                countnormal = 0
                for i in range(len(data)):
                    number = data.iloc[i]['对比值']
                    if data.iloc[i]['是否为轻食日']==1:
                        if (number>(100-a)) and (number<(100+b)):
                            countlight=countlight+1
                    else:
                        if (number>(100-c)) and (number<(100+d)):
                            countnormal=countnormal+1
                    if last[i]==False:
                        day.append(countnormal+countlight)
                        name.append(data.iloc[i]['姓名'])
                        countnormal=0
                        countlight=0
                dataframe=pd.DataFrame({'姓名':name,'热量管理较好天数':day})
                new = pd.merge(origianl, dataframe, on='姓名')
                print('-----参数a:'+str(a)+',参数b:'+str(b)+',参数c:'+str(c)+',参数d:'+str(d)+'-------')
                value=new['减重值'].corr(new['热量管理较好天数'])
                print(value)
                x1.append(value)
                va.append(a)
                vb.append(b)
                vc.append(c)
                vd.append(d)
                v.append(value)
                if value>bestv:
                    bestv=value
                    besta=a
                    bestb=b
                    bestc = c
                    bestd = d

            X.append(x1)

dataframe=pd.DataFrame({'参数a':va,'参数b':vb,'参数c':vc,'参数d':vd,'相关性值':v})
dataframe=dataframe.sort_values('相关性值',ascending=False)
print(dataframe.head())
print('最好的相关性:'+str(bestv)+',参数a:'+str(besta)+',参数b:'+str(bestb)+',参数c:'+str(bestc)+',参数d:'+str(bestd))
#设置热图大小
plt.figure(1,figsize=(12,8))
#设置热图标题
plt.title(u'热量对比值区间分析')
#绘制热图
sns.heatmap(X)
plt.show()