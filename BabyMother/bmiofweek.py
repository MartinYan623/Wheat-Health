import pandas as pd
"""
data=pd.read_csv('../data/宝妈营数据/宝妈用户初始信息表.csv',usecols=[0,1,2,4,5])
data=data[data['用户编号']>44688]
data=data.reset_index(drop=True)
data.rename(columns={'BMI':'初始BMI'}, inplace = True)
data2=pd.read_csv('../data/宝妈营数据/宝妈用户减重表5.22-5.28.csv',usecols=[0,2])
data = pd.merge(data, data2, on='用户编号')
data.rename(columns={'减重值':'第一周减重值'}, inplace = True)
data2=pd.read_csv('../data/宝妈营数据/宝妈用户减重表5.29-6.4.csv',usecols=[0,2])
data = pd.merge(data, data2)
data.rename(columns={'减重值':'第二周减重值'}, inplace = True)
print(data)
"""
data=pd.read_csv('../data/宝妈营数据/宝妈用户每日体重变化5.22-5.28.csv')
data2=pd.read_csv('../data/宝妈营数据/宝妈用户初始信息表.csv',usecols=[1,2,4])
first=data.duplicated(['uid'],keep='first')
last=data.duplicated(['uid'],keep='last')
reduce=[]
name=[]
id=[]
for i in range(len(data)):
    if first[i]==False:
        original=data.iloc[i]['体重']
    if last[i]==False:
        id.append(data.iloc[i]['uid'])
        name.append(data.iloc[i]['姓名'])
        reduce.append(original-data.iloc[i]['体重'])
dataframe=pd.DataFrame({'uid':id,'姓名':name,'第一周减重值':reduce})
dataframe = pd.merge(dataframe, data2, on='姓名')



data=pd.read_csv('../data/宝妈营数据/宝妈用户每日体重变化5.22-6.4.csv')
data=data[data['日期']> '2018/5/27 0:00']
data=data.reset_index(drop=True)
first=data.duplicated(['uid'],keep='first')
last=data.duplicated(['uid'],keep='last')
reduce=[]
id=[]

for i in range(len(data)):
    if first[i]==False:
        original=data.iloc[i]['体重']
    if last[i]==False:
        id.append(data.iloc[i]['uid'])
        reduce.append(original-data.iloc[i]['体重'])

dataframe2=pd.DataFrame({'uid':id,'第二周减重值':reduce})
dataframe21 = pd.merge(dataframe, dataframe2, how='outer')


data=pd.read_csv('../data/宝妈营数据/宝妈用户每日体重变化5.22-6.11.csv')
data=data[data['日期']> '2018/6/1 0:00']
data=data[(True-data['日期'].isin(['2018/6/2 0:00','2018/6/3 0:00']))]
data=data.reset_index(drop=True)
first=data.duplicated(['uid'],keep='first')
last=data.duplicated(['uid'],keep='last')
reduce=[]
id=[]
for i in range(len(data)):
    if first[i]==False:
        original=data.iloc[i]['体重']
    if last[i]==False:
        id.append(data.iloc[i]['uid'])

        reduce.append(original-data.iloc[i]['体重'])
dataframe3=pd.DataFrame({'uid':id,'第三周减重值':reduce})
dataframe31 = pd.merge(dataframe21, dataframe3, how='outer')


data=pd.read_csv('../data/宝妈营数据/宝妈用户每日体重变化5.22-6.18.csv')
data=data[data['日期']> '2018/6/10 0:00']
data=data[data['日期']<'2018/6/2 0:00']
#data=data[(True-data['日期'].isin(['2018/6/2 0:00','2018/6/3 0:00']))]

data=data.reset_index(drop=True)
first=data.duplicated(['uid'],keep='first')
last=data.duplicated(['uid'],keep='last')
reduce=[]
id=[]
for i in range(len(data)):
    if first[i]==False:
        original=data.iloc[i]['体重']
    if last[i]==False:
        id.append(data.iloc[i]['uid'])

        reduce.append(original-data.iloc[i]['体重'])
dataframe4=pd.DataFrame({'uid':id,'第四周减重值':reduce})
dataframe41 = pd.merge(dataframe31, dataframe4, how='outer')



data=pd.read_csv('../data/宝妈营数据/宝妈用户每日体重变化5.22-6.25.csv')
data=data[data['日期']> '2018/6/17 0:00']
data=data[data['日期']< '2018/6/3 0:00']
data=data[(True-data['日期'].isin(['2018/6/2 0:00']))]
print(data)
data=data.reset_index(drop=True)
first=data.duplicated(['uid'],keep='first')
last=data.duplicated(['uid'],keep='last')
reduce=[]
id=[]
for i in range(len(data)):
    if first[i]==False:
        original=data.iloc[i]['体重']
    if last[i]==False:
        id.append(data.iloc[i]['uid'])

        reduce.append(original-data.iloc[i]['体重'])
dataframe5=pd.DataFrame({'uid':id,'第五周减重值':reduce})
dataframe51 = pd.merge(dataframe41, dataframe5, how='outer')
print(dataframe51)
dataframe51.to_csv('/Users/martin_yan/Desktop/整理数据111.csv', index=False, encoding="utf_8_sig")