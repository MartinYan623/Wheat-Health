import pandas as pd
encoding='UTF-8'
data=pd.read_csv("data/1.csv")
data.drop(['营id','PB','实际值','对比值','推荐满分区间'], inplace=True, axis=1)
data=data[(True-data['RF'].isin(['有氧运动','吸烟']))]
data=data.drop_duplicates()
userid=[]
name=[]
fruit=[]
veg=[]
wholegrain=[]
refinegrain=[]
diefiber=[]
milk=[]
totalprotein=[]
fishshrimp=[]
fattyacids=[]
solidfat=[]
salt=[]
sugar=[]
totalheat=[]
nutrients=[]
alcohol=[]
water=[]
for i in range(0, len(data)):
    if data.iloc[i]['RF']=='水果摄入量':
        fruit.append(data.iloc[i]['实际得分'])

    if data.iloc[i]['RF']=='蔬菜摄入量':
        veg.append(data.iloc[i]['实际得分'])

    if data.iloc[i]['RF']=='全谷类摄入量':
        wholegrain.append(data.iloc[i]['实际得分'])

    if data.iloc[i]['RF'] == '精制谷物摄入量':
        refinegrain.append(data.iloc[i]['实际得分'])

    if data.iloc[i]['RF'] == '膳食纤维摄入量':
        diefiber.append(data.iloc[i]['实际得分'])

    if data.iloc[i]['RF'] == '乳类摄入量':
        milk.append(data.iloc[i]['实际得分'])

    if data.iloc[i]['RF'] == '总蛋白摄入量':
        totalprotein.append(data.iloc[i]['实际得分'])

    if data.iloc[i]['RF'] == '鱼虾贝壳类及植物蛋白类摄入量':
        fishshrimp.append(data.iloc[i]['实际得分'])

    if data.iloc[i]['RF'] == '不饱和与饱和脂肪酸摄入比':
        fattyacids.append(data.iloc[i]['实际得分'])

    if data.iloc[i]['RF'] == '固态脂肪摄入量':
        solidfat.append(data.iloc[i]['实际得分'])

    if data.iloc[i]['RF'] == '钠盐摄入量':
        salt.append(data.iloc[i]['实际得分'])

    if data.iloc[i]['RF'] == '添加糖摄入量':
        sugar.append(data.iloc[i]['实际得分'])

    if data.iloc[i]['RF'] == '总热量摄入量':
        totalheat.append(data.iloc[i]['实际得分'])

    if data.iloc[i]['RF'] == '三大营养素组成':
        nutrients.append(data.iloc[i]['实际得分'])

    if data.iloc[i]['RF'] == '饮酒（酒精量，全天标准）':
        alcohol.append(data.iloc[i]['实际得分'])

    if data.iloc[i]['RF'] == '饮水量':
        water.append(data.iloc[i]['实际得分'])
totalscore=[]
time=data['记录日期'].unique()
for i in range(0,len(time)):
    userid.append(data.iloc[1][0])
    name.append(data.iloc[1]['姓名'])
    totalscore.append(fruit[i]+veg[i]+wholegrain[i]+refinegrain[i]+diefiber[i]+milk[i]+totalprotein[i]+fishshrimp[i]+fattyacids[i]
                      +solidfat[i]+salt[i]+sugar[i]+totalheat[i]+nutrients[i]+alcohol[i]+water[i])



dataframe = pd.DataFrame({'用户编号': userid , '姓名':name, '记录日期':time, '水果摄入量得分': fruit,'蔬菜摄入量得分':veg,'全谷类摄入量得分':wholegrain,'精制谷物摄入量得分':refinegrain,
                          '膳食纤维摄入量得分':diefiber,'乳类摄入量得分':milk,'总蛋白摄入量得分':totalprotein,'鱼虾贝壳类及植物蛋白类摄入量得分':fishshrimp,'不饱和与饱和脂肪酸摄入比得分':fattyacids,
    '固态脂肪摄入量得分':solidfat,'钠盐摄入量得分':salt,'添加糖摄入量得分':sugar,'总热量摄入量得分':totalheat,'三大营养素组成得分':nutrients,'饮酒（酒精量，全天标准）得分':alcohol,'饮水量得分':water,'总得分':totalscore})

columns = ['用户编号','姓名','记录日期','水果摄入量得分','蔬菜摄入量得分','全谷类摄入量得分','精制谷物摄入量得分','膳食纤维摄入量得分','乳类摄入量得分','总蛋白摄入量得分','鱼虾贝壳类及植物蛋白类摄入量得分'
    ,'不饱和与饱和脂肪酸摄入比得分','固态脂肪摄入量得分','钠盐摄入量得分','添加糖摄入量得分','总热量摄入量得分','三大营养素组成得分','饮酒（酒精量，全天标准）得分','饮水量得分','总得分']
dataframe.to_csv("/Users/martin_yan/Desktop/data.csv",index=False,encoding="utf_8_sig",columns=columns)



