import pandas as pd
data = pd.read_csv('/Users/martin_yan/Desktop/babymother_data5.22-6.25.csv',usecols=['用户编号','姓名','三大营养素碳水化合物对比值','三大营养素脂肪对比值','三大营养素蛋白质对比值'])
last = data.duplicated('用户编号', keep='last')
bestv=0
va=[]
vb=[]
vc=[]
vd=[]
ve=[]
vf=[]
v=[]
for a in range(35,45):
    for b in range(55,60):
        for c in range(15,20):
            for d in range(35, 40):
                for e in range(12, 16):
                    for f in range(20, 25):

                        countgood = 0
                        day=[]
                        id=[]
                        for i in range (len(data)):
                            numcarbohydrate=data.iloc[i]['三大营养素碳水化合物对比值']
                            numfat=data.iloc[i]['三大营养素脂肪对比值']
                            numprotein=data.iloc[i]['三大营养素蛋白质对比值']
                            if (numcarbohydrate>a) and (numcarbohydrate<b) and (numfat>c) and (numfat<d) and (numprotein>e) and (numprotein<f):
                                countgood=countgood+1
                            if last[i]==False:
                                id.append(data.iloc[i]['用户编号'])
                                day.append(countgood)
                                countgood=0
                        dataframe = pd.DataFrame({'用户编号': id, '三大营养素管理较好天数': day})
                        origianl = pd.read_csv('/Users/martin_yan/Desktop/mean_babymother_data5.22-6.25(体重跨度5周／实际记录平均分).csv',
                                   usecols=['用户编号', '减重值'])
                        new = pd.merge(origianl, dataframe, on='用户编号')
                        print('-----参数a:' + str(a) + ',参数b:' + str(b) + ',参数c:' + str(c) + ',参数d:' + str(d)+ ',参数e:' + str(e)+ ',参数f:' + str(f)+'-------')
                        value = new['减重值'].corr(new['三大营养素管理较好天数'])
                        print(value)
                        va.append(a)
                        vb.append(b)
                        vc.append(c)
                        vd.append(d)
                        ve.append(e)
                        vf.append(f)
                        v.append(value)
                        if value > bestv:
                            bestv = value
                            besta = a
                            bestb = b
                            bestc = c
                            bestd = d
                            beste = e
                            bestf = f
dataframe=pd.DataFrame({'参数a':va,'参数b':vb,'参数c':vc,'参数d':vd,'参数e':ve,'参数f':vf,'相关性值':v})
dataframe=dataframe.sort_values('相关性值',ascending=False)
print(dataframe.head())
print('最好的相关性:'+str(bestv)+',参数a:'+str(besta)+',参数b:'+str(bestb)+',参数c:'+str(bestc)+',参数d:'+str(bestd)+',参数e:'+str(beste)+',参数f:'+str(bestf))