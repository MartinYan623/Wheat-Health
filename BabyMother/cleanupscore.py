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

data=pd.read_csv('/Users/martin_yan/Desktop/babymother_data5.22-6.25.csv',usecols=['用户编号','姓名','记录日期','总得分'])
data = data.drop_duplicates(['用户编号','记录日期'])
info=pd.read_csv('/Users/martin_yan/Desktop/mean_babymother_data5.22-6.25(总表／实际记录平均分).csv',usecols=['姓名','平均得分'])
data = pd.merge(data, info, on='姓名')
print(len(data['姓名'].unique()))
username=data.duplicated('用户编号',keep='last')
count=1
score=[]

for i in range(0,35):
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
    if data.iloc[i]['记录日期']=='2018/6/5 0:00':
        score[14]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/6 0:00':
        score[15]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/7 0:00':
        score[16]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/8 0:00':
        score[17]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/9 0:00':
        score[18]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/10 0:00':
        score[19]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/11 0:00':
        score[20]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/12 0:00':
        score[21]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/13 0:00':
        score[22]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/14 0:00':
        score[23]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/15 0:00':
        score[24]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/16 0:00':
        score[25]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/17 0:00':
        score[26]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/18 0:00':
        score[27]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/19 0:00':
        score[28]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/20 0:00':
        score[29]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/21 0:00':
        score[30]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/22 0:00':
        score[31]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/23 0:00':
        score[32]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/24 0:00':
        score[33]=data.iloc[i]['总得分']
    if data.iloc[i]['记录日期']=='2018/6/25 0:00':
        score[34]=data.iloc[i]['总得分']

    if username[i]==False:
        sec = True
        if count > 1:
            sec = False
        name=data.iloc[i]['姓名']
        id=data.iloc[i]['用户编号']
        mean=data.iloc[i]['平均得分']
        dataframe = pd.DataFrame({'用户编号':[id],'姓名':[name],'5.22':[score[0]],'5.23':[score[1]],'5.24':[score[2]],'5.25':[score[3]],'5.26':[score[4]],'5.27': [score[5]],'5.28':[score[6]],
                                  '5.29':[score[7]],'5.30':[score[8]],'5.31':[score[9]],'6.1': [score[10]],'6.2':[score[11]],'6.3':[score[12]],'6.4':[score[13]],
                                  '6.5':[score[14]],'6.6':[score[15]],'6.7': [score[16]],'6.8':[score[17]],'6.9':[score[18]],'6.10':[score[19]],'6.11':[score[20]],
                                  '6.12': [score[21]],'6.13': [score[22]], '6.14': [score[23]], '6.15': [score[24]], '6.16': [score[25]],'6.17': [score[26]], '6.18': [score[27]],
                                  '6.19': [score[28]], '6.20': [score[29]], '6.21': [score[30]], '6.22': [score[31]],'6.23': [score[32]], '6.24': [score[33]],'6.25': [score[34]],'平均得分':[mean]})

        columns = ['用户编号', '姓名', '5.22','5.23','5.24','5.25','5.26','5.27','5.28','5.29','5.30','6.1','6.2','6.3','6.4','6.5',
                   '6.6','6.7','6.8','6.9','6.10','6.11','6.12','6.13','6.14','6.15','6.16','6.17','6.18','6.19','6.20','6.21',
                   '6.22','6.23','6.24','6.25','平均得分']
        dataframe.to_csv('/Users/martin_yan/Desktop/cleanup_score5.22-6.25.csv', index=False,columns=columns,
                          encoding="utf_8_sig",mode='a',header=sec)
        score = []
        for i in range(0, 35):
            score.append('NaN')
        count=count+1