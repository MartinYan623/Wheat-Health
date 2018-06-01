import pandas as pd
import numpy as np
encoding='UTF-8'

data=pd.read_csv('data/用户初始体重表.csv')
find=pd.read_csv('/Users/martin_yan/Desktop/222.csv')

#删除早于2018／5／22的体重数据
data=data[data['日期']> '2018/5/21 0:00']
#打印满足条件的用户初始体重表里的人数
print(len(data['uid'].unique()))
data.drop_duplicates('uid','first',inplace=True)
#对数据重新index编号
data=data.reset_index(drop=True)
data = pd.merge(find, data, how='left', on='姓名')
bmi=[]
for i in range(len(data)):
    height=data.iloc[i]['身高']
    weight=data.iloc[i]['体重']
    bmi.append(weight/pow(height/100,2))
data['BMI']=bmi
data.drop(['日期','uid'], inplace=True, axis=1)
print(data)
data.to_csv('/Users/martin_yan/Desktop/addBMI.csv', index=False, encoding="utf_8_sig")