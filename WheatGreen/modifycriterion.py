import pandas as pd


data = pd.read_csv('data/宝妈营数据5.22-5.29.csv')
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
            data.loc[i, 'rf得分'] = data.iloc[i]['rf得分'] * 2
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
data.to_csv('/Users/martin_yan/Desktop/new_宝妈营得分.csv', index=False, encoding="utf_8_sig")