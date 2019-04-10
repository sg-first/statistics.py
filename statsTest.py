import statsmodels.stats.weightstats as stats1
import scipy.stats as stats2

alpha=0.05

# 原假设：均值小于参数
def z_test(x,mean):
    z, p = stats1.ztest(x, value=mean)
    return p, p>alpha

# 原假设：均值小于参数
def t_test(x,mean):
    t, p = stats2.ttest_1samp(x, popmean=mean)
    return p, p>alpha

# 检验两个正态总体均值差
def t_test2(x1,x2,eq_Var=True):
    t, p = stats2.ttest_ind(x1,x2,equal_var=eq_Var)
    return p, p>alpha # 如果p小，是拒绝原假设，认为二者不同，即可以通过该属性区分

def chis2_test(x,exp=None): # 观测频数和期望频数，衡量二者差距
    s, p = stats2.chisquare(x,exp)
    return p, p>alpha # 如果p小，是拒绝原假设，认为二者不同

# 检验两个分布抽样有多大概率不存在差异（总体均值相等）
def ranksum_test(x,y):
    s, p = stats2.ranksums(x, y)
    return p, p>alpha # 如果p小，是拒绝原假设，认为二者不同