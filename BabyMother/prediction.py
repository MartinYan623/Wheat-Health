import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectFromModel
from sklearn.kernel_ridge import KernelRidge
from xgboost import XGBRegressor
from sklearn import svm
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression as LR
import pgmpy

train=pd.read_csv('/Users/martin_yan/Desktop/饮食均分与减重值离群点删除-总表入营得分.csv')
plt.rcParams['font.sans-serif']=[u'SimHei']
plt.rcParams['axes.unicode_minus']=False
#选取部分属性作为预测标准
predictors=['记录天数','平均得分','完整记录天数','膳食纤维摄入量平均分','蔬菜摄入量平均分','固态脂肪摄入量平均分','水果摄入量平均分',
'全谷类实际摄入平均量','精制谷物摄入量平均分','水果实际摄入平均量','全谷类摄入量平均分','总热量摄入量平均分','鱼虾贝壳类及植物蛋白类摄入量平均分',
'饮水量平均分','不饱和与饱和脂肪酸摄入平均对比值','不饱和与饱和脂肪酸摄入比平均分','饮水平均量','初始体重值','BMI','三大营养素蛋白质平均对比值',
'膳食纤维实际摄入平均量','钠盐实际摄入平均量','总蛋白摄入量平均分','普通日热量平均摄入值','乳类实际摄入平均量','乳类摄入量平均分','三大营养素碳水化合物平均对比值',
'三大营养素组成平均分','蔬菜实际摄入平均量','鱼虾贝壳类及植物蛋白类实际摄入平均量','轻食日热量平均对比值','总蛋白实际摄入平均量','轻食日热量平均摄入值',
'添加糖摄入量平均分','普通日热量平均对比值','年龄','钠盐摄入量平均分','饮酒实际摄入平均量','添加糖实际摄入平均量','三大营养素脂肪平均对比值',
'精制谷物摄入平均量','固态脂肪实际摄入平均量','饮酒（酒精量，全天标准）平均分']

#找出存在nan的行号
#print(np.where(np.isnan(train['体重']))[0])
#根据行号去删除某些行
#train.drop([2,12] ,axis=0, inplace=True)


target=train['减重值']
x_train, x_test, y_train, y_test = train_test_split(train[predictors], target,test_size=.1)


"""

algorithms=[
RandomForestRegressor(n_estimators =300,criterion='mse',min_samples_leaf=6,max_depth=3,random_state=1,n_jobs=-1),
#svm.SVR(C=1.0, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma='auto',kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)
]
full_predictions = []
for lr in algorithms:
    model = lr.fit(x_train, y_train)
    predictions=model.predict(x_test)
    full_predictions.append(predictions)
predictions = full_predictions[0]
print(predictions)
print(y_test)
print ('RMSE is: \n', mean_squared_error(y_test, predictions))



#lr=linear_model.LinearRegression()
#lr=linear_model.RidgeCV(alphas=np.logspace(-3, 2, 100)),
#lr=XGBRegressor(max_depth=5)
model = lr.fit(x_train, y_train)
predictions=model.predict(x_test)
print(predictions)
print(y_test)
print ('RMSE is: \n', mean_squared_error(y_test, predictions))


clf = svm.SVR(C=1.0, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma='auto',kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)
model=clf.fit(x_train, y_train)
prediction=model.predict(x_test)
print(prediction)
print(y_test)
print ('RMSE is: \n', mean_squared_error(y_test, prediction))


rmse=[]
pa=[]
for i in range(1,10):
    forest = RandomForestRegressor(n_estimators =300,criterion='mse',min_samples_leaf=6,max_depth=3,random_state=1,n_jobs=-1)
    model=forest.fit(x_train, y_train)
    prediction = model.predict(x_test)
    print('第'+str(i)+'次尝试')
    #print(prediction)
    #print(y_test)
    #print ('RMSE is: \n', mean_squared_error(y_test, prediction))
    rmse.append(mean_squared_error(y_test, prediction))
    pa.append(i)

plt.title('rmse随参数n的变化图')
plt.xlabel('n')
plt.ylabel('rmse')
plt.plot(pa,rmse,'r', label='broadcast')
plt.show()

for i in range(0,50):
    target=train['减重值']
    x_train, x_test, y_train, y_test = train_test_split(train[predictors], target,random_state=i, test_size=.1)

    algorithms=[
    RandomForestRegressor(n_estimators =300,criterion='mse',min_samples_leaf=6,max_depth=3,random_state=1,n_jobs=-1),
    #svm.SVR(C=1.0, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma='auto',kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)
    linear_model.LinearRegression()
    ]

    full_predictions = []
    best=100
    parameter=0
    for j in range(0,100):
        for lr in algorithms:
            a=j*0.01
            model = lr.fit(x_train, y_train)
            predictions=model.predict(x_test)
            full_predictions.append(predictions)
        predictions = (full_predictions[0]*a + full_predictions[1]*(1-a))
        print ('RMSE is: \n', mean_squared_error(y_test, predictions))
        rmse=mean_squared_error(y_test, predictions)
        if rmse<best:
            best=rmse
            parameter=a

    print('最小的rmse值:'+str(best)+',最好的权重a:'+str(parameter))

"""



