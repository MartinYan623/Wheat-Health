import pandas as pd
from scipy import stats
import numpy as np
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
encoding='UTF-8'
data=pd.read_csv('/Users/martin_yan/Desktop/new_babymother_completedata5.22-6.4.csv')
print(data)
model = ols('减重值 ~ 蔬菜摄入量平均分',data).fit()
anovat = anova_lm(model)
print(anovat)