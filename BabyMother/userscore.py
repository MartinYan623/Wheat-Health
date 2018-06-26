import pandas as pd
import numpy as np
import math
encoding='UTF-8'

"""
#得到的分数是在str内，提取出str中用户的每日分数
data = pd.read_csv('../data/用户界面得分.csv')
print(data)
id=[]
name=[]
userscore=[]
time=[]
for i in range(len(data)):
    id.append(data.iloc[i]['uid'])
    name.append(data.iloc[i]['姓名'])
    time.append(data.iloc[i]['记录时间'])
    content=data.iloc[i]['日报文案']
    s=[]
    for x in content:
        if x.isdigit():
            s.append(x)
    score=0
    degree=0
    for i in range(len(s)-1,-1,-1):
        score=int(s[i])*math.pow(10,degree)+score
        degree=degree+1
    userscore.append(int(score))
dataframe=pd.DataFrame({'用户编号':id,'姓名':name,'今日得分':userscore,'记录日期':time})
columns = ['用户编号', '姓名','今日得分','记录日期']
dataframe.to_csv('/Users/martin_yan/Desktop/score.csv', index=False, encoding="utf_8_sig",columns=columns)
"""

data = pd.read_csv('../data/score.csv')
data=data[data['记录日期']>'2018/6/11 0:00']
data=data[data['记录日期']< '2018/6/3 0:00']
data=data[(True-data['记录日期'].isin(['2018/6/2 0:00']))]
data = data.drop_duplicates(['用户编号','记录日期'],keep='first')
data=data.reset_index(drop=True)

first=data.duplicated(['用户编号'],keep='first')
last=data.duplicated(['用户编号'],keep='last')
meanscore=[]
id=[]
name=[]
score=0
for i in range (len(data)):
    score=data.iloc[i]['今日得分']+score
    if last[i]==False:
        id.append(data.iloc[i]['用户编号'])
        name.append(data.iloc[i]['姓名'])
        meanscore.append(score/14)
        score=0
dataframe=pd.DataFrame({'用户编号':id,'姓名':name,'最后14天平均得分':meanscore})

data2 = pd.read_csv('/Users/martin_yan/Desktop/宝妈用户减重表5.22-6.25(全部).csv',usecols=[0,2,3])
dataframe2 = pd.merge(dataframe, data2, on='用户编号')
print(dataframe2)

#找出用户完整记录的天数
data=pd.read_csv('/Users/martin_yan/Desktop/123.csv',usecols=[0,2,3,4])
#删除用户重复记录的行
data = data.drop_duplicates(['uid','记录日期'])
#删除某列值为空的行
data = data.dropna(subset=['姓名'])
data=data.reset_index(drop=True)
username=data.duplicated('uid',keep='last')
count=0
meal=[]
name=[]
for i in range(len(data)):
    if data.iloc[i]['记录餐数']==2:
        count=count+1
    if username[i]==False:
        name.append(data.iloc[i]['姓名'])
        meal.append(count)
        count=0
dataframe3=pd.DataFrame({'姓名':name,'完整记录天数':meal})
data = pd.merge(dataframe2,dataframe3, on='姓名')
columns = ['用户编号', '姓名','BMI','最后14天平均得分','减重值','完整记录天数']
data.to_csv('/Users/martin_yan/Desktop/fdfdf.csv', index=False, encoding="utf_8_sig",columns=columns)
print(data)
print(data[(data['最后14天平均得分']>69.9) & (data['减重值']<4)& (data['BMI']>22)& (data['完整记录天数']>27)])



