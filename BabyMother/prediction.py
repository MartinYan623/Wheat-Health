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

train=pd.read_csv('/Users/martin_yan/Desktop/90人 入营得分 5.22-6.25.csv')
plt.rcParams['font.sans-serif']=[u'SimHei']
plt.rcParams['axes.unicode_minus']=False

#选取部分属性作为预测标准
predictors=['记录天数','新饮食得分(100制)','完整记录天数','膳食纤维摄入量平均分','蔬菜摄入量平均分','固态脂肪摄入量平均分','水果摄入量平均分',
'全谷类实际摄入平均量','精制谷物摄入量平均分','水果实际摄入平均量','全谷类摄入量平均分','总热量摄入量平均分','鱼虾贝壳类及植物蛋白类摄入量平均分',
'饮水量平均分','不饱和与饱和脂肪酸摄入平均对比值','不饱和与饱和脂肪酸摄入比平均分','饮水平均量','初始体重值','BMI','三大营养素蛋白质平均对比值',
'膳食纤维实际摄入平均量','钠盐实际摄入平均量','总蛋白摄入量平均分','普通日热量平均摄入值','乳类实际摄入平均量','乳类摄入量平均分','三大营养素碳水化合物平均对比值',
'三大营养素组成平均分','蔬菜实际摄入平均量','鱼虾贝壳类及植物蛋白类实际摄入平均量','轻食日热量平均对比值','总蛋白实际摄入平均量','轻食日热量平均摄入值',
'添加糖摄入量平均分','普通日热量平均对比值','年龄','钠盐摄入量平均分','饮酒实际摄入平均量','添加糖实际摄入平均量','三大营养素脂肪平均对比值',
'精制谷物摄入平均量','固态脂肪实际摄入平均量','饮酒（酒精量，全天标准）平均分']

target=train['减重值']
# 求模型的平均RMSE,并绘图
rmse=[]
pa=[]
sum=0

"""
for i in range(1,100):
    x_train, x_test, y_train, y_test = train_test_split(train[predictors],  target,random_state= i,test_size=.1)
    #forest = RandomForestRegressor(n_estimators =300,criterion='mse',min_samples_leaf=6,max_depth=3,random_state=1,n_jobs=-1)
    #lr=svm.SVR(C=1.0, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma='auto', kernel='rbf', max_iter=-1,shrinking=True, tol=0.001, verbose=False)
    #lr = linear_model.LinearRegression()
    lr = XGBRegressor(max_depth=3,max_leaf_nodes=6)
    model=lr.fit(x_train, y_train)
    prediction = model.predict(x_test)
    print('第'+str(i)+'次尝试')
    print ('RMSE is: \n', mean_squared_error(y_test, prediction))
    rmse.append(mean_squared_error(y_test, prediction))
    sum=sum+mean_squared_error(y_test, prediction)
    pa.append(i)
print('平均rmse值:'+str(sum/100))
print('最大rmse值:'+str(max(rmse)))
print('最小rmse值:'+str(min(rmse)))
plt.title('rmse随参数n的变化图')
plt.xlabel('i')
plt.ylabel('rmse')
plt.plot(pa,rmse,'r', label='broadcast')
plt.show()
"""



"""
# 单个模型试验
lr=RandomForestRegressor(n_estimators =300,criterion='mse',min_samples_leaf=6,max_depth=3,random_state=1,n_jobs=-1),
lr=svm.SVR(C=1.0, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma='auto',kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)
lr=linear_model.LinearRegression()
lr=XGBRegressor(max_depth=5)
model = lr.fit(x_train, y_train)
predictions=model.predict(x_test)
print(predictions)
print(y_test)
print ('RMSE is: \n', mean_squared_error(y_test, predictions))


# 结合运用多模型
for i in range(1,100):
    x_train, x_test, y_train, y_test = train_test_split(train[predictors],  target,random_state= i,test_size=.1)
    algorithms=[
    RandomForestRegressor(n_estimators =300,criterion='mse',min_samples_leaf=6,max_depth=3,random_state=1,n_jobs=-1),
    XGBRegressor(max_depth=3,max_leaf_nodes=6)
    ]
    full_predictions = []
    for lr in algorithms:
        model = lr.fit(x_train, y_train)
        predictions=model.predict(x_test)
        full_predictions.append(predictions)
    predictions = (full_predictions[0]+full_predictions[1])/2
    print('第' + str(i) + '次尝试')
    print ('RMSE is: \n', mean_squared_error(y_test, predictions))
    rmse.append(mean_squared_error(y_test, predictions))
    sum = sum + mean_squared_error(y_test, predictions)
    pa.append(i)
print('平均rmse值:'+str(sum/100))
print('最大rmse值:'+str(max(rmse)))
print('最小rmse值:'+str(min(rmse)))
plt.title('rmse随参数n的变化图')
plt.xlabel('i')
plt.ylabel('rmse')
plt.plot(pa,rmse,'r', label='broadcast')
plt.show()
"""

# 模型权重实验
meanpa=0
for i in range(1,50):
    best=100
    parameter=0
    x_train, x_test, y_train, y_test = train_test_split(train[predictors],  target,random_state= i,test_size=.1)
    algorithms=[
    RandomForestRegressor(n_estimators =300,criterion='mse',min_samples_leaf=6,max_depth=3,random_state=1,n_jobs=-1),
    XGBRegressor(max_depth=3,max_leaf_nodes=6)
    ]
    for a in range(0,10):
        weight=a*0.1
        full_predictions = []
        for lr in algorithms:
            model = lr.fit(x_train, y_train)
            predictions=model.predict(x_test)
            full_predictions.append(predictions)
        predictions = full_predictions[0]*weight+full_predictions[1]*(1-weight)
        print('第' + str(i) + '次尝试')
        print ('RMSE is: \n', mean_squared_error(y_test, predictions))
        now=mean_squared_error(y_test, predictions)
        if now<best:
            best=now
            parameter=weight
        if a==9:
            rmse.append(best)
            sum = sum +best
            meanpa=meanpa+parameter
            pa.append(i)
print('平均rmse值:'+str(sum/50))
print('最大rmse值:'+str(max(rmse)))
print('最小rmse值:'+str(min(rmse)))
print('平均参数:'+str(meanpa/50))
plt.title('rmse随参数n的变化图')
plt.xlabel('i')
plt.ylabel('rmse')
plt.plot(pa,rmse,'r', label='broadcast')
plt.show()

