import pandas as pd


"""
# 将旧评分标准变为HEI分值
data = pd.read_csv('../data/宝妈营数据6.19-6.25.csv')
#data.drop(['营id','PB','对比值','推荐满分区间'], inplace=True, axis=1)
#data = data[(data['RF'].isin(['水果摄入量', '蔬菜摄入量','膳食纤维摄入量','固态脂肪摄入量','三大营养素组成','饮酒（酒精量，全天标准）','添加糖摄入量','钠盐摄入量']))]
#data = data.drop_duplicates(['记录日期', 'RF'])
for i in range(len(data)):
    if data.iloc[i]['rf'] == '水果摄入量':
           data.loc[i,'rf满分参考']=10
           data.loc[i,'rf得分']= data.iloc[i]['rf得分'] *2
    if data.iloc[i]['rf'] == '蔬菜摄入量':
           data.loc[i, 'rf满分参考'] = 10
           data.loc[i,'rf得分'] = data.iloc[i]['rf得分']*2
    if data.iloc[i]['rf'] == '膳食纤维摄入量':
            data.loc[i, 'rf满分参考'] = 10
            data.loc[i, 'rf得分'] = data.iloc[i]['rf得分'] * 2
    if data.iloc[i]['rf'] == '固态脂肪摄入量':
            data.loc[i, 'rf满分参考'] = 10
            data.loc[i, 'rf得分'] = data.iloc[i]['rf得分'] *2
    if data.iloc[i]['rf'] == '钠盐摄入量':
            data.loc[i, 'rf满分参考'] = 10
            data.loc[i, 'rf得分'] = data.iloc[i]['rf得分'] * 2
    if data.iloc[i]['rf'] == '三大营养素组成':
            data.loc[i, 'rf满分参考'] = 5
            data.loc[i, 'rf得分'] = data.iloc[i]['rf得分'] / 2
    if data.iloc[i]['rf'] == '饮酒（酒精量，全天标准）':
            data.loc[i, 'rf满分参考'] = 5
            data.loc[i, 'rf得分'] = data.iloc[i]['rf得分'] / 2
    if data.iloc[i]['rf'] == '添加糖摄入量':
            data.loc[i, 'rf满分参考'] = 5
            data.loc[i, 'rf得分'] = data.iloc[i]['rf得分'] / 2
print(data)
data.to_csv('/Users/martin_yan/Desktop/new_宝妈营数据6.19-6.25.csv', index=False, encoding="utf_8_sig")
"""

#升降某些指标的分值
data = pd.read_csv('/Users/martin_yan/Desktop/90人 入营得分 5.22-6.25.csv')
newdiefiber =[]
newveg=[]
newsolidfat=[]
newsalt=[]
newtotalprotein=[]
newnutrients=[]
newtotalscore=[]
weight=[]
best=0
parameter=0
for a in range(0,100):
    a=a*0.01
    for i in range (len(data)):
        leftscore=data.iloc[i]['饮食均衡得分(120分)']-(data.iloc[i]['蔬菜摄入量平均分']+data.iloc[i]['膳食纤维摄入量平均分']+data.iloc[i]['固态脂肪摄入量平均分']+
                                       data.iloc[i]['钠盐摄入量平均分']+data.iloc[i]['乳类摄入量平均分']+data.iloc[i]['三大营养素组成平均分'])
        newsubscore=((data.iloc[i]['蔬菜摄入量平均分']+data.iloc[i]['膳食纤维摄入量平均分']+data.iloc[i]['固态脂肪摄入量平均分'])/30*a+\
                    (data.iloc[i]['钠盐摄入量平均分']+data.iloc[i]['乳类摄入量平均分']+data.iloc[i]['三大营养素组成平均分'])/25*(1-a))*55
        newbalanced=newsubscore+leftscore
        newtotalscore.append(newbalanced/120*90+data.iloc[i]['总热量摄入量平均分']/10*10)
        weight.append(data.iloc[i]['减重值'])
    dataframe=pd.DataFrame({'新总分(100分制)':newtotalscore,'减重值':weight})
    corr=dataframe['新总分(100分制)'].corr(dataframe['减重值'])
    print(corr)
    if corr>best:
        best=corr
        parameter=a
print('最好的相关性是:'+str(corr)+'  分值升降系数a为:'+str(a))
