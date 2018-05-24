import pandas as pd


for num in range(0,12):
    data = pd.read_csv('data/%d.csv' % num)
    #data.drop(['营id','PB','对比值','推荐满分区间'], inplace=True, axis=1)
    #data = data[(data['RF'].isin(['水果摄入量', '蔬菜摄入量','膳食纤维摄入量','固态脂肪摄入量','三大营养素组成','饮酒（酒精量，全天标准）','添加糖摄入量','钠盐摄入量']))]
    #data = data.drop_duplicates(['记录日期', 'RF'])
    for i in range(len(data)):
        if data.iloc[i]['RF'] == '水果摄入量':
           data.loc[i,'满分']=10
           data.loc[i,'实际得分']= data.iloc[i]['实际得分'] *2
        if data.iloc[i]['RF'] == '蔬菜摄入量':
           data.loc[i, '满分'] = 10
           data.loc[i,'实际得分'] = data.iloc[i]['实际得分']*2
        if data.iloc[i]['RF'] == '膳食纤维摄入量':
            data.loc[i, '满分'] = 10
            data.loc[i, '实际得分'] = data.iloc[i]['实际得分'] * 2
        if data.iloc[i]['RF'] == '固态脂肪摄入量':
            data.loc[i, '满分'] = 10
            data.loc[i, '实际得分'] = data.iloc[i]['实际得分'] * 2
        if data.iloc[i]['RF'] == '钠盐摄入量':
            data.loc[i, '满分'] = 10
            data.loc[i, '实际得分'] = data.iloc[i]['实际得分'] * 2
        if data.iloc[i]['RF'] == '三大营养素组成':
            data.loc[i, '满分'] = 5
            data.loc[i, '实际得分'] = data.iloc[i]['实际得分'] / 2
        if data.iloc[i]['RF'] == '饮酒（酒精量，全天标准）':
            data.loc[i, '满分'] = 5
            data.loc[i, '实际得分'] = data.iloc[i]['实际得分'] / 2
        if data.iloc[i]['RF'] == '添加糖摄入量':
            data.loc[i, '满分'] = 5
            data.loc[i, '实际得分'] = data.iloc[i]['实际得分'] / 2

    print(data)
    data.to_csv('/Users/martin_yan/Desktop/new_%d.csv' %num, index=False, encoding="utf_8_sig")