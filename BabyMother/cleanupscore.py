import pandas as pd
import datetime
from datetime import timedelta
from dateutil.parser import parse
import time
encoding='UTF-8'
"""
t = datetime.datetime(2018,5,2)
t=t.strftime('%Y/%m/%d')
date_time = datetime.datetime.strptime(t,'%Y/%m/%d')
nextday=date_time+datetime.timedelta(1)
print(nextday)
"""

data=pd.read_csv('/Users/martin_yan/Desktop/new_babymother_data5.22-6.4.csv',usecols=['用户编号','姓名','记录日期','总得分'])
#info=pd.read_csv('../data/用户信息表3.csv',usecols=['姓名'])
info=pd.read_csv('/Users/martin_yan/Desktop/new_mean_babymother_data5.22-6.4.csv',usecols=['姓名','平均得分'])
data = pd.merge(data, info, on='姓名')
print(len(data['姓名'].unique()))
username=data.duplicated('用户编号',keep='last')
count=1
score=[]

for i in range(0,14):
    score.append('NaN')

for i in range(len(data)):
    if data.iloc[i]['记录日期']=='2018/5/22 0:00':
        score[0]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/5/23 0:00':
        score[1]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/5/24 0:00':
        score[2]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/5/25 0:00':
        score[3]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/5/26 0:00':
        score[4]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/5/27 0:00':
        score[5]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/5/28 0:00':
        score[6]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/5/29 0:00':
        score[7]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/5/30 0:00':
        score[8]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/5/31 0:00':
        score[9]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/1 0:00':
        score[10]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/2 0:00':
        score[11]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/3 0:00':
        score[12]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/4 0:00':
        score[13]=data.iloc[i]['总得分']
    if username[i]==False:
        sec = True
        if count > 1:
            sec = False
        name=data.iloc[i]['姓名']
        id=data.iloc[i]['用户编号']
        mean=data.iloc[i]['平均得分']
        dataframe = pd.DataFrame({'用户编号':[id],'姓名':[name],'5.22':[score[0]],'5.23':[score[1]],'5.24':[score[2]],'5.25':[score[3]],'5.26':[score[4]],
                                  '5.27': [score[5]],'5.28':[score[6]],'5.29':[score[7]],'5.30':[score[8]],'5.31':[score[9]],
                                  '6.1': [score[10]],'6.2':[score[11]],'6.3':[score[12]],'6.4':[score[13]],'平均得分':[mean]})

        columns = ['用户编号', '姓名', '5.22','5.23','5.24','5.25','5.26','5.27','5.28','5.29','5.30','6.1','6.2','6.3','6.4','平均得分']
        dataframe.to_csv('/Users/martin_yan/Desktop/cleanup_score.csv', index=False,columns=columns,
                          encoding="utf_8_sig",mode='a',header=sec)
        score = []
        for i in range(0, 14):
            score.append('NaN')
        count=count+1