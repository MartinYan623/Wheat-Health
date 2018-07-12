import pandas as pd
encoding='UTF-8'

"""
#获得用户的初始信息表
data=pd.read_csv('/Users/martin_yan/Desktop/123.csv')
print(data)
first=data.duplicated(['uid'],keep='first')
bmi=[]
id=[]
name=[]
height=[]
weight=[]
day=[]
for i in range (len(data)):
    if first[i]==False:
        id.append(data.iloc[i]['uid'])
        name.append(data.iloc[i]['姓名'])
        height.append(data.iloc[i]['身高'])
        weight.append(data.iloc[i]['体重'])
        day.append(data.iloc[i]['记录日期'])
        bmi.append(data.iloc[i]['体重']/pow(data.iloc[i]['身高']/100,2))

dataframe=pd.DataFrame({'用户编号':id,'姓名':name,'初始体重':weight,'日期':day,'身高':height,'BMI':bmi})
columns = ['用户编号', '姓名', '初始体重','日期','身高','BMI']
dataframe.to_csv('/Users/martin_yan/Desktop/宝妈轻享用户初始信息表.csv', index=False, encoding="utf_8_sig", columns=columns)
"""

"""
#获得用户的轻食日
data=pd.read_csv('/Users/martin_yan/Desktop/222.csv')
print(data)
first=data.duplicated(['uid'],keep='first')
last=data.duplicated(['uid'],keep='last')

day1=[]
day2=[]
name=[]
id=[]
for i in range(len(data)):
    if last[i]==False:
        name.append(data.iloc[i]['姓名'])
        id.append(data.iloc[i]['uid'])
        day2.append(data.iloc[i]['轻食日'])
    if first[i]==False:
        day1.append(data.iloc[i]['轻食日'])
print(len(name))
print(len(id))
print(len(day1))
print(len(day2))
dataframe=pd.DataFrame({'用户编号':id,'姓名':name,'轻食日1':day1,'轻食日2':day2})
columns = ['用户编号', '姓名', '轻食日1','轻食日2']
dataframe.to_csv('/Users/martin_yan/Desktop/宝妈轻享轻食日统计.csv', index=False, encoding="utf_8_sig", columns=columns)
"""

data=pd.read_csv('../data/宝妈营轻享/宝妈营轻享数据.csv')
data2=pd.read_csv('../data/宝妈营轻享/宝妈轻享用户初始信息表.csv',usecols=[0])
data.rename(columns={'uid':'用户编号'}, inplace = True)
data = pd.merge(data, data2, on='用户编号')

data=data[data['rf'].isin(['总热量摄入量'])]
print(data)
data.to_csv('/Users/martin_yan/Desktop/dsdsdd.csv', index=False, encoding="utf_8_sig")