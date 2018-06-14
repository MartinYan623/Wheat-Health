import pandas as pd
from scipy import stats
import numpy as np
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
import statsmodels.api
encoding='UTF-8'
data=pd.read_csv('/Users/martin_yan/Desktop/mean_babymother_data5.22-6.11(体重跨度3周).csv')
#计算方差分析f值 如果要做多因素方差分析在右侧+上其他变量即可
print(data)
model = ols('减重值 ~ 蔬菜摄入量平均分',data).fit()
anovat = anova_lm(model)
print(anovat)
#t检验p值
veg=data[['蔬菜摄入量平均分']]
reduce=data['减重值'].to_frame(name=None)
fit = statsmodels.api.OLS(reduce, veg).fit()
print (fit.params)
print (fit.summary())
