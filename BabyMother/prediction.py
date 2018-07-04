import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier,GradientBoostingRegressor,AdaBoostClassifier
from sklearn.svm import SVR
from sklearn.kernel_ridge import KernelRidge
from xgboost import XGBRegressor


train=pd.read_csv('/Users/martin_yan/Desktop/mean_babymother_data5.22-6.25(体重跨度5周／实际记录平均分).csv')

#选取部分属性作为预测标准
predictors=['膳食纤维摄入量平均分','蔬菜摄入量平均分','平均得分','添加糖摄入量平均分','固态脂肪摄入量平均分','精制谷物摄入量平均分',
'总蛋白摄入量平均分','记录天数','不饱和与饱和脂肪酸摄入平均对比值']

#找出存在nan的行号
#print(np.where(np.isnan(train['体重']))[0])
#根据行号去删除某些行
#train.drop([2,12] ,axis=0, inplace=True)

target=train['减重值']
x_train, x_test, y_train, y_test = train_test_split(train[predictors], target, test_size=.1)
lr=linear_model.LinearRegression()
#lr=linear_model.RidgeCV(alphas=np.logspace(-3, 2, 100)),
#lr=XGBRegressor(max_depth=5)
model = lr.fit(x_train, y_train)
predictions=model.predict(x_test)
print(predictions)
print(y_test)
print ('RMSE is: \n', mean_squared_error(y_test, predictions))

