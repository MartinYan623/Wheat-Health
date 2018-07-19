import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
import xlrd
import statsmodels.api as sm
plt.rcParams['font.sans-serif']=[u'SimHei']
plt.rcParams['axes.unicode_minus']=False
dta=pd.read_excel('/Users/martin_yan/Desktop/陈翔体重变化.xlsx')
print(dta)

dta=np.array(dta['体重'],dtype=np.float)
dta=pd.Series(dta)
dta.index = pd.Index(sm.tsa.datetools.dates_from_range('2001','2035'))
fig = plt.figure(figsize=(12, 8))


# 时间序列的差分d,需要得到一个平稳时间序列(方差小)
# 一阶差分不行可以用二阶
diff1 = dta.diff(1)
# 通过自相关图和偏相关图去找寻合适的p,q
ax1=fig.add_subplot(211)
# 自相关图决定系数q
fig = sm.graphics.tsa.plot_acf(dta,lags=20,ax=ax1)
ax2 = fig.add_subplot(212)
# 偏相关图决定系数p
fig = sm.graphics.tsa.plot_pacf(dta,lags=20,ax=ax2)


# AR模型：自相关系数拖尾，偏自相关系数截尾；
# MA模型：自相关系数截尾，偏自相关函数拖尾；
# ARMA模型：自相关函数和偏自相关函数均拖尾。

# 赤池信息准则的方法是寻找可以最好地解释数据但包含最少自由参数的模型。
# 不仅仅包括AIC准则，目前选择模型常用如下准则：
# AIC=-2 ln(L) + 2 k 中文名字：赤池信息量 akaike information criterion
# BIC=-2 ln(L) + ln(n)*k 中文名字：贝叶斯信息量 bayesian information criterion
# HQ=-2 ln(L) + ln(ln(n))*k hannan-quinn criterion
# 分别打印AIC、BIC和HQ
#print(sm.tsa.arma_order_select_ic(dta,max_ar=5,max_ma=5,ic='aic')['aic_min_order'])
#print(sm.tsa.arma_order_select_ic(dta,max_ar=5,max_ma=5,ic='bic')['bic_min_order'])
#print(sm.tsa.arma_order_select_ic(dta,max_ar=5,max_ma=5,ic='hqic')['hqic_min_order'])



arma_mod80 = sm.tsa.ARMA(dta,(3,3)).fit()
print(arma_mod80.aic,arma_mod80.bic,arma_mod80.hqic)
print(arma_mod80.summary2())

# 观察是否符合正态分布，绘制QQ图
resid = arma_mod80.resid
print(stats.normaltest(resid))
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
fig = qqplot(resid, line='q', ax=ax, fit=True)

# 德宾-沃森（Durbin-Watson）检验。德宾-沃森检验,简称D-W检验
# 是目前检验自相关性最常用的方法，但它只使用于检验一阶自相关性
# 当DW值显著的接近于O时，则存在正自相关性
# 而接近于２时，则不存在（一阶）自相关性
# 当DW值显著的接近于4时，则存在负自相关性
print(sm.stats.durbin_watson(arma_mod80.resid.values))

predict_dta = arma_mod80.predict('2035', '2045', dynamic=True)
print(predict_dta)
fig, ax = plt.subplots(figsize=(12, 8))
ax = dta.ix['2000':].plot(ax=ax)
fig = arma_mod80.plot_predict('2035', '2045', dynamic=True, ax=ax, plot_insample=False)
plt.title('用户体重变化情况及预测')
plt.xlabel('时间')
plt.ylabel('体重值(KG)')
plt.show()
