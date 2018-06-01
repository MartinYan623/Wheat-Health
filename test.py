import pandas as pd
import numpy as np
encoding='UTF-8'
data=pd.read_csv('data/用户初始体重表.csv')
meandata=pd.read_csv('/Users/martin_yan/Desktop/mean_babymother_data.csv',usecols=['BMI','姓名','用户编号'])

#删除早于2018／5／22的体重数据
data=data[data['日期']> '2018/5/21 0:00']
#打印满足条件的用户初始体重表里的人数
print(len(data['uid'].unique()))
"""
#去掉除每个人第一个记录日期外的重复行
people=data.drop_duplicates('uid','first',inplace=True)
#删除不需要的列
data.drop(['日期','uid'], inplace=True, axis=1)
#对数据重新index编号
data=data.reset_index(drop=True)
#以姓名来左连接两个表
data = pd.merge(meandata, data, how='left', on='姓名')
change=[]
#计算出每个人的减重百分比
for i in range(len(data)):
    original=data.iloc[i]['体重']
    reduce=data.iloc[i]['减重值']
    change.append(reduce/original)
data['减重百分比']=change
data.to_csv('/Users/martin_yan/Desktop/new_babymother_completedata.csv', index=False, encoding="utf_8_sig")
"""

data=data.drop_duplicates(['uid','日期'])
data.drop(['uid'], inplace=True, axis=1)
data = pd.merge(meandata, data, how='left', on='姓名')
#删除体重值为nan的行
indexs = list(data[np.isnan(data['体重'])].index)
data = data.drop(indexs)
fre=data.groupby('用户编号').count()['姓名'].to_dict()
a,b = list(fre.keys()) , list(fre.values())
fre = pd.DataFrame({'用户编号':a,'实际记录天数':b})

#fre_series=data['用户编号'].value_counts()
#fre = fre_series.to_frame('实际记录天数')
data = pd.merge(fre, data, how='left', on='用户编号')
print(data)
group=[]
reduce=[]
time=[]
username=[]
data=data[data['实际记录天数']>6]
data=data.reset_index(drop=True)
note=data.duplicated(['姓名'],keep='first')

for i in range(len(data)):
    if data.iloc[i]['BMI']>24:
        if note[i] == False:
            pass
        else:
            username.append(data.iloc[i]['姓名'])
            reduce.append(data.iloc[i-1]['体重'] - data.iloc[i]['体重'])
            time.append(str(data.iloc[i - 1]['日期']) + ' ~ ' + str(data.iloc[i]['日期']))
            group.append("A组(BMI>24)")
    else:
        if note[i] == False:
            pass
        else:
            username.append(data.iloc[i]['姓名'])
            reduce.append(data.iloc[i-1]['体重'] - data.iloc[i]['体重'])
            time.append(str(data.iloc[i - 1]['日期']) + ' ~ ' + str(data.iloc[i]['日期']))
            group.append("B组(BMI<=24)")

dataframe = pd.DataFrame({'姓名': username, '组别':group,'减肥时间段': time,'减重值':reduce})
columns = ['姓名','组别','减肥时间段','减重值']
print(dataframe)
dataframe.to_csv('/Users/martin_yan/Desktop/11111111.csv', index=False, encoding="utf_8_sig", columns=columns)
