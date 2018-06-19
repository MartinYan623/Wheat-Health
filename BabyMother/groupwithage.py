import pandas as pd
import numpy as np
encoding='UTF-8'

data=pd.read_csv('../data/宝妈用户每日体重变化5.22-6.11.csv')
meandata=pd.read_csv('/Users/martin_yan/Desktop/mean_babymother_data5.22-6.11(体重跨度3周).csv',usecols=['用户编号','姓名','年龄','完整记录天数'])
data.drop('uid', inplace=True, axis=1)
data = pd.merge(meandata, data, how='left', on='姓名')

fre=data.groupby('用户编号').count()['姓名'].to_dict()
a,b = list(fre.keys()) , list(fre.values())
fre = pd.DataFrame({'用户编号':a,'实际记录天数':b})

data = pd.merge(fre, data, how='left', on='用户编号')
group=[]
reduce=[]
time=[]
username=[]
age=[]
data=data[data['完整记录天数']>14]
#这里指体重实际记录天数
#data=data[data['实际记录天数']>14]
#data=data[(data['实际记录天数']<10) | (data['完整记录天数']<10)]
data=data.reset_index(drop=True)
print(len(data['用户编号'].unique()))

note=data.duplicated(['姓名'],keep='first')
count1=0
count2=0
count3=0
count4=0
count5=0
print(data)
for i in range(len(data)):
    if ((data.iloc[i]['年龄']>=25) & (data.iloc[i]['年龄']<30)):
        if note[i] == False:
            weight=data.iloc[i]['体重']
            count1=count1+1
        else:
            username.append(data.iloc[i]['姓名'])
            age.append(data.iloc[i]['年龄'])
            reduce.append(weight- data.iloc[i]['体重'])
            time.append(str(data.iloc[i - 1]['日期']) + ' ~ ' + str(data.iloc[i]['日期']))
            group.append("A组(年龄>=25 and 年龄<30)")

    if ((data.iloc[i]['年龄']>=30) & (data.iloc[i]['年龄']<35)):
        if note[i] == False:
            weight = data.iloc[i]['体重']
            count2 = count2 + 1
        else:
            username.append(data.iloc[i]['姓名'])
            age.append(data.iloc[i]['年龄'])
            reduce.append(weight - data.iloc[i]['体重'])
            time.append(str(data.iloc[i - 1]['日期']) + ' ~ ' + str(data.iloc[i]['日期']))
            group.append("B组(年龄>=30 and 年龄<35)")

    if ((data.iloc[i]['年龄']>=35) & (data.iloc[i]['年龄']<40)):
        if note[i] == False:
            weight = data.iloc[i]['体重']
            count3 = count3 + 1
        else:
            username.append(data.iloc[i]['姓名'])
            age.append(data.iloc[i]['年龄'])
            reduce.append(weight - data.iloc[i]['体重'])
            time.append(str(data.iloc[i - 1]['日期']) + ' ~ ' + str(data.iloc[i]['日期']))
            group.append("C组(年龄>=35 and 年龄<40)")

    if ((data.iloc[i]['年龄']>=40) & (data.iloc[i]['年龄']<45)):
        if note[i] == False:
            weight = data.iloc[i]['体重']
            count4 = count4 + 1
        else:
            username.append(data.iloc[i]['姓名'])
            age.append(data.iloc[i]['年龄'])
            reduce.append(weight - data.iloc[i]['体重'])
            time.append(str(data.iloc[i - 1]['日期']) + ' ~ ' + str(data.iloc[i]['日期']))
            group.append("D组(年龄>=40 and 年龄<45)")

    if ((data.iloc[i]['年龄']>=45) & (data.iloc[i]['年龄']<50)):
        if note[i] == False:
            weight = data.iloc[i]['体重']
            count5 = count5 + 1
        else:
            username.append(data.iloc[i]['姓名'])
            age.append(data.iloc[i]['年龄'])
            reduce.append(weight - data.iloc[i]['体重'])
            time.append(str(data.iloc[i - 1]['日期']) + ' ~ ' + str(data.iloc[i]['日期']))
            group.append("E组(年龄>=45 and 年龄<50)")


data = pd.DataFrame({'姓名': username,'年龄':age,'组别':group,'减肥时间段': time,'减重值':reduce})
columns = ['姓名','年龄','组别','减肥时间段','减重值']
print(data)
print(count1)
print(count2)
print(count3)
print(count4)
print(count5)
#dataframe.to_csv('/Users/martin_yan/Desktop/11111111.csv', index=False, encoding="utf_8_sig", columns=columns)
#dataframe.to_excel('/Users/martin_yan/Desktop/11111111.xlsx', index=False, encoding="utf_8_sig", columns=columns)

#data=pd.read_csv('/Users/martin_yan/Desktop/11111111.csv')
username=data.duplicated('姓名',keep='last')
name=[]
group=[]
date=[]
reduce=[]
age=[]
for i in range(len(data)):
    if username[i]==False:
        name.append(data.iloc[i]['姓名'])
        age.append(data.iloc[i]['年龄'])
        group.append(data.iloc[i]['组别'])
        date.append(data.iloc[i]['减肥时间段'])
        reduce.append(data.iloc[i]['减重值'])
dataframe=pd.DataFrame({'姓名':name,'年龄':age,'组别':group,'减肥时间段':date,'减重值':reduce})
columns=['姓名','年龄','组别','减肥时间段','减重值']
dataframe.to_csv('/Users/martin_yan/Desktop/2.csv',index=False, encoding="utf_8_sig",columns=columns)