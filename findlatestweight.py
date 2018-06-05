import pandas as pd
encoding='UTF-8'
data=pd.read_csv('data/height.csv')
print(data)
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