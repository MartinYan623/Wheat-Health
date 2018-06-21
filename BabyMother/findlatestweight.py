import pandas as pd
import openpyxl
encoding='UTF-8'

"""
data=pd.read_csv('../data/height.csv',usecols=[0,1,4,5])
data2=pd.read_csv('../data/宝妈用户初始体重表.csv')
data=data.append(data2)
data=data[data['日期']> '2018/5/21 0:00']
data = data.drop_duplicates(['uid','日期'],keep='last')
data=data.sort_values(['uid','日期'],ascending=True)
data=data.reset_index(drop=True)
print(data)
data.to_csv('/Users/martin_yan/Desktop/1111111.csv', index=False, encoding="utf_8_sig")


date=data.duplicated(['uid'],keep='last')
print(date)
uid=[]
name=[]
height=[]
weight=[]
time=[]
for i in range(len(data)):
    if date[i]==False:
        uid.append(data.iloc[i]['uid'])
        name.append(data.iloc[i]['真实姓名'])
        height.append(data.iloc[i]['身高'])
        weight.append(data.iloc[i]['体重'])
        time.append(data.iloc[i]['记录日期'])
dataframe = pd.DataFrame({'用户编号':uid, '姓名':name, '身高':height,'体重':weight,'记录日期':time})
columns = ['用户编号', '姓名', '身高','体重','记录日期']
dataframe.to_csv('/Users/martin_yan/Desktop/height2.csv', index=False, encoding="utf_8_sig",columns=columns)


#找出某些减重值情况不好的用户 输出为excel文件
data=pd.read_csv('/Users/martin_yan/Desktop/mean_babymother_data5.22-6.11(21天平均分 体重跨度3周).csv',usecols=['姓名','BMI','减重值','平均得分','年龄'])
data[(data['BMI']>22) & (data['年龄']<36)]
data.to_excel('/Users/martin_yan/Desktop/1.xlsx', index=False, encoding="utf_8_sig",header=True)
"""

data=pd.read_csv('../data/宝妈用户每日体重变化5.22-6.18.csv')
data2=pd.read_csv('../data/宝妈用户初始信息表.csv',usecols=['姓名','BMI'])
data = pd.merge(data, data2, on='姓名')
data = data.drop_duplicates(['uid','日期'],keep='last')
data=data.reset_index(drop=True)
#data=data[data['日期']>'2018/5/28 0:00']
#data=data[data['日期']< '2018/6/5 0:00']
#data=data[(True-data['日期'].isin(['2018/6/10 0:00','2018/6/11 0:00','2018/6/12 0:00','2018/6/13 0:00','2018/6/14 0:00','2018/6/15 0:00','2018/6/16 0:00','2018/6/17 0:00','2018/6/18 0:00']))]
data=data[(True-data['日期'].isin(['2018/6/12 0:00','2018/6/13 0:00','2018/6/14 0:00','2018/6/15 0:00','2018/6/16 0:00','2018/6/17 0:00','2018/6/18 0:00']))]
fre=data.groupby('uid').count()['姓名'].to_dict()
a,b = list(fre.keys()) , list(fre.values())
fre = pd.DataFrame({'uid':a,'实际记录天数':b})
#fre_series=data['用户编号'].value_counts()
#fre = fre_series.to_frame('实际记录天数')
data = pd.merge(fre, data, how='left', on='uid')
data=data[data['实际记录天数']>17]
print(len(data['uid'].unique()))
data=data.reset_index(drop=True)
first=data.duplicated(['姓名'],keep='first')
last=data.duplicated(['姓名'],keep='last')
reduce=[]
id=[]
name=[]
day=[]
BMI=[]
for i in range(len(data)):
    if first[i]==False:
        original=data.iloc[i]['体重']
    if last[i]==False:
        id.append(data.iloc[i]['uid'])
        name.append(data.iloc[i]['姓名'])
        day.append(data.iloc[i]['实际记录天数'])
        reduce.append(original-data.iloc[i]['体重'])
        if data.iloc[i]['BMI']>24:
            BMI.append('A组(BMI>24)')
        else:
            BMI.append('B组(BMI<=24)')
dataframe=pd.DataFrame({'用户编号':id,'姓名':name,'实际记录天数':day,'减重值':reduce,'BMI':BMI})
columns=['用户编号','姓名','实际记录天数','减重值','BMI']
print(dataframe)
dataframe.to_csv('/Users/martin_yan/Desktop/累积第三周减重值情况.csv', index=False, encoding="utf_8_sig",columns=columns)