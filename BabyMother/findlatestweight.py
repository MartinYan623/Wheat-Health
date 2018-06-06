import pandas as pd
encoding='UTF-8'
data=pd.read_csv('../data/height.csv',usecols=[0,1,4,5])
data2=pd.read_csv('../data/用户初始体重表.csv')
data=data.append(data2)
data=data[data['日期']> '2018/5/21 0:00']
data = data.drop_duplicates(['uid','日期'],keep='last')
data=data.sort_values(['uid','日期'],ascending=True)
data=data.reset_index(drop=True)
print(data)
data.to_csv('/Users/martin_yan/Desktop/1111111.csv', index=False, encoding="utf_8_sig")

"""
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
"""
