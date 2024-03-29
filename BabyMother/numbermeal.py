import pandas as pd
encoding='UTF-8'

#找出用户完整记录的天数
data=pd.read_csv('/Users/martin_yan/Desktop/记录餐数.csv',usecols=[0,2,3,4])
completedata=pd.read_csv('/Users/martin_yan/Desktop/333.csv')
helper=pd.read_csv('../data/宝妈营助理.csv',usecols=[2,3])
#data=data[data['记录日期']>'2018/5/28 0:00']
#删除用户重复记录的行
data = data.drop_duplicates(['uid','记录日期'])
#删除某列值为空的行
data = data.dropna(subset=['姓名'])
data=data.reset_index(drop=True)
username=data.duplicated('uid',keep='last')
count=0
meal=[]
name=[]
for i in range(len(data)):
    if data.iloc[i]['记录餐数']==2:
        count=count+1
    if username[i]==False:
        name.append(data.iloc[i]['姓名'])
        meal.append(count)
        count=0
dataframe=pd.DataFrame({'姓名':name,'完整记录天数':meal})
data = pd.merge(completedata,dataframe, on='姓名')
data = pd.merge(data,helper, on='姓名')
print(data)
columns= ['用户编号', '姓名', '年龄','BMI','记录天数','完整记录天数','水果实际摄入平均量', '水果摄入量平均分', '蔬菜实际摄入平均量', '蔬菜摄入量平均分', '全谷类实际摄入平均量', '全谷类摄入量平均分',
                    '精制谷物摄入平均量', '精制谷物摄入量平均分', '膳食纤维实际摄入平均量', '膳食纤维摄入量平均分', '乳类实际摄入平均量', '乳类摄入量平均分', '总蛋白实际摄入平均量',
                    '总蛋白摄入量平均分', '鱼虾贝壳类及植物蛋白类实际摄入平均量', '鱼虾贝壳类及植物蛋白类摄入量平均分',
                    '不饱和与饱和脂肪酸摄入平均对比值', '不饱和与饱和脂肪酸摄入比平均分', '固态脂肪实际摄入平均量', '固态脂肪摄入量平均分', '钠盐实际摄入平均量', '钠盐摄入量平均分',
                    '添加糖实际摄入平均量', '添加糖摄入量平均分', '轻食日热量平均摄入值','普通日热量平均摄入值','轻食日热量平均对比值','普通日热量平均对比值','总热量摄入量平均分', '三大营养素碳水化合物平均对比值',
                    '三大营养素脂肪平均对比值','三大营养素蛋白质平均对比值', '三大营养素组成平均分', '饮酒实际摄入平均量',
                    '饮酒（酒精量，全天标准）平均分', '饮水平均量', '饮水量平均分','平均得分','初始体重值','减重值','减重百分比','助理名称']
data.to_csv('/Users/martin_yan/Desktop/444.csv',index=False, encoding="utf_8_sig",columns=columns)

