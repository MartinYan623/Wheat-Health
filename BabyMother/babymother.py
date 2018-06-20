import pandas as pd
encoding='UTF-8'
data=pd.read_csv('../data/宝妈营数据5.22-5.28.csv',usecols=[0,2,6,7,8,9,12])
data2=pd.read_csv('../data/宝妈营数据5.29-6.4.csv',usecols=[0,2,6,7,8,9,12])
data3=pd.read_csv('../data/宝妈营数据6.5-6.11.csv',usecols=[0,2,6,7,8,9,12])
data4=pd.read_csv('../data/宝妈营数据6.12-6.18.csv',usecols=[0,2,6,7,8,9,12])
data=data.append(data2)
data=data.append(data3)
data=data.append(data4)
#用uid对数据排序，默认升序
#data=data.sort_values(['uid','记录日期'])
data=data[(True-data['rf'].isin(['有氧运动','吸烟']))]
print('宝妈营总人数：'+str(len(data['uid'].unique())))
data = data.drop_duplicates(['uid','记录日期', 'rf'])
data=data.reset_index(drop=True)
username=data.duplicated('uid',keep='last')
date=data.duplicated(['uid','记录日期'],keep='last')
print(data)
userid = []
name = []
f_fruit = []
fruit = []
f_veg = []
veg = []
f_wholegrain = []
wholegrain = []
f_refinegrain = []
refinegrain = []
f_diefiber = []
diefiber = []
f_milk = []
milk = []
f_totalprotein = []
totalprotein = []
f_fishshrimp = []
fishshrimp = []
f_fattyacids = []
fattyacids = []
f_solidfat = []
solidfat = []
f_salt = []
salt = []
f_sugar = []
sugar = []
f_totalheat = []
totalheat = []
f_nutrients = []
nutrients = []
f_alcohol = []
alcohol = []
f_water = []
water = []
time=[]
totalscore=[]
row=0
for i in range(len(data)):
    if data.iloc[i]['rf'] == '水果摄入量':
        fruit.append(data.iloc[i]['rf得分'])
        f_fruit.append(data.iloc[i]['摄入值'])

    if data.iloc[i]['rf'] == '蔬菜摄入量':
        veg.append(data.iloc[i]['rf得分'])
        f_veg.append(data.iloc[i]['摄入值'])

    if data.iloc[i]['rf'] == '全谷类摄入量':
        wholegrain.append(data.iloc[i]['rf得分'])
        f_wholegrain.append(data.iloc[i]['摄入值'])

    if data.iloc[i]['rf'] == '精制谷物摄入量':
        refinegrain.append(data.iloc[i]['rf得分'])
        f_refinegrain.append(data.iloc[i]['摄入值'])

    if data.iloc[i]['rf'] == '膳食纤维摄入量':
        diefiber.append(data.iloc[i]['rf得分'])
        f_diefiber.append(data.iloc[i]['摄入值'])

    if data.iloc[i]['rf'] == '乳类摄入量':
        milk.append(data.iloc[i]['rf得分'])
        f_milk.append(data.iloc[i]['摄入值'])

    if data.iloc[i]['rf'] == '总蛋白摄入量':
        totalprotein.append(data.iloc[i]['rf得分'])
        f_totalprotein.append(data.iloc[i]['摄入值'])

    if data.iloc[i]['rf'] == '鱼虾贝壳类及植物蛋白类摄入量':
        fishshrimp.append(data.iloc[i]['rf得分'])
        f_fishshrimp.append(data.iloc[i]['摄入值'])

    if data.iloc[i]['rf'] == '不饱和与饱和脂肪酸摄入比':
        fattyacids.append(data.iloc[i]['rf得分'])
        f_fattyacids.append(data.iloc[i]['摄入值'])

    if data.iloc[i]['rf'] == '固态脂肪摄入量':
        solidfat.append(data.iloc[i]['rf得分'])
        f_solidfat.append(data.iloc[i]['摄入值'])

    if data.iloc[i]['rf'] == '钠盐摄入量':
        salt.append(data.iloc[i]['rf得分'])
        f_salt.append(data.iloc[i]['摄入值'])

    if data.iloc[i]['rf'] == '添加糖摄入量':
        sugar.append(data.iloc[i]['rf得分'])
        f_sugar.append(data.iloc[i]['摄入值'])

    if data.iloc[i]['rf'] == '总热量摄入量':
        totalheat.append(data.iloc[i]['rf得分'])
        f_totalheat.append(data.iloc[i]['摄入值'])

    if data.iloc[i]['rf'] == '三大营养素组成':
        nutrients.append(data.iloc[i]['rf得分'])
        f_nutrients.append(data.iloc[i]['摄入值'])

    if data.iloc[i]['rf'] == '饮酒（酒精量，全天标准）':
        alcohol.append(data.iloc[i]['rf得分'])
        f_alcohol.append(data.iloc[i]['摄入值'])

    if data.iloc[i]['rf'] == '饮水量':
        water.append(data.iloc[i]['rf得分'])
        f_water.append(data.iloc[i]['摄入值'])

    if date[i]==False:
        time.append(data.iloc[i]['记录日期'])
        name.append(data.iloc[i]['真实姓名'])
        userid.append(data.iloc[i]['uid'])
        totalscore.append(fruit[row]+veg[row]+wholegrain[row]+refinegrain[row]+diefiber[row]+milk[row]+totalprotein[row]+fishshrimp[row]+fattyacids[row]
                      +solidfat[row]+salt[row]+sugar[row]+totalheat[row]+nutrients[row]+alcohol[row]+water[row])
        row=row+1




dataframe = pd.DataFrame({'用户编号': userid, '姓名': name, '记录日期': time,
                              '水果摄入实际量': f_fruit, '水果摄入量得分': fruit,
                              '蔬菜摄入实际量': f_veg, '蔬菜摄入量得分': veg,
                              '全谷类摄入实际量': f_wholegrain, '全谷类摄入量得分': wholegrain,
                              '精制谷物摄入实际量': f_refinegrain, '精制谷物摄入量得分': refinegrain,
                              '膳食纤维摄入实际量': f_diefiber, '膳食纤维摄入量得分': diefiber,
                              '乳类摄入实际量': f_milk, '乳类摄入量得分': milk,
                              '总蛋白摄入实际量': f_totalprotein, '总蛋白摄入量得分': totalprotein,
                              '鱼虾贝壳类及植物蛋白类摄入实际量': f_fishshrimp, '鱼虾贝壳类及植物蛋白类摄入量得分': fishshrimp,
                              '不饱和与饱和脂肪酸实际摄入量': f_fattyacids, '不饱和与饱和脂肪酸摄入比得分': fattyacids,
                              '固态脂肪摄入实际量': f_solidfat, '固态脂肪摄入量得分': solidfat,
                              '钠盐摄入实际量': f_salt, '钠盐摄入量得分': salt,
                              '添加糖摄入实际量': f_sugar, '添加糖摄入量得分': sugar,
                              '总热量摄入实际量': f_totalheat, '总热量摄入量得分': totalheat,
                              '三大营养素摄入实际量': f_nutrients, '三大营养素组成得分': nutrients,
                              '饮酒摄入实际量': f_alcohol, '饮酒（酒精量，全天标准）得分': alcohol,
                              '饮水量': f_water, '饮水量得分': water,'总得分':totalscore
                              })

columns = ['用户编号', '姓名', '记录日期', '水果摄入实际量', '水果摄入量得分', '蔬菜摄入实际量', '蔬菜摄入量得分', '全谷类摄入实际量', '全谷类摄入量得分', '精制谷物摄入实际量',
               '精制谷物摄入量得分', '膳食纤维摄入实际量', '膳食纤维摄入量得分', '乳类摄入实际量', '乳类摄入量得分', '总蛋白摄入实际量', '总蛋白摄入量得分', '鱼虾贝壳类及植物蛋白类摄入实际量',
               '鱼虾贝壳类及植物蛋白类摄入量得分'
        , '不饱和与饱和脂肪酸实际摄入量', '不饱和与饱和脂肪酸摄入比得分', '固态脂肪摄入实际量', '固态脂肪摄入量得分', '钠盐摄入实际量', '钠盐摄入量得分', '添加糖摄入实际量', '添加糖摄入量得分',
               '总热量摄入实际量', '总热量摄入量得分', '三大营养素摄入实际量', '三大营养素组成得分', '饮酒摄入实际量', '饮酒（酒精量，全天标准）得分', '饮水量', '饮水量得分','总得分']
dataframe.to_csv('/Users/martin_yan/Desktop/new_babymother_data5.22-6.18.csv', index=False, encoding="utf_8_sig", columns=columns)



