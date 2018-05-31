import pandas as pd
encoding='UTF-8'
data=pd.read_csv('data/用户初始体重表.csv')
meandata=pd.read_csv('/Users/martin_yan/Desktop/mean_babymother_data.csv')
#删除早于2018／5／22的体重数据
data=data[data['日期']> '2018/5/21 0:00']
#打印满足条件的用户初始体重表里的人数
print(len(data['uid'].unique()))
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
data.to_csv('/Users/martin_yan/Desktop//babymother_completedata.csv', index=False, encoding="utf_8_sig")
