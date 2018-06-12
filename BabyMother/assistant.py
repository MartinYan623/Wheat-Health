import pandas as pd
encoding='UTF-8'
data=pd.read_csv('/Users/martin_yan/Desktop/3333.csv')
people=data.duplicated(['uid'],keep='last')
print(people)
print(data)
assistant=[]
id=[]
cla=[]
name=[]
for i in range (len(data)):
    if people[i]==True:
        wardens=data.iloc[i]['助理名称']
    else:
        id.append(data.iloc[i]['uid'])
        cla.append(data.iloc[i]['班级'])
        name.append(data.iloc[i]['姓名'])
        assistant.append('1.主管助理: '+data.iloc[i]['助理名称'] +'   2.协管助理: '+wardens)
        wardens='无'

dataframe=pd.DataFrame({'用户编号':id,'班级':cla,'姓名':name,'助理名称':assistant})
columns=['用户编号','班级','姓名','助理名称']
dataframe.to_csv('/Users/martin_yan/Desktop/assistant.csv', index=False, encoding="utf_8_sig",columns=columns)
