import statsmodels.stats.weightstats as stats1
import scipy.stats as stats2

alpha=0.05

def z_test(x,mu):
    z, p = stats1.ztest(x, value=mu)
    return p, p>alpha

def t_test(x,mu):
    t, p = stats2.ttest_1samp(x, popmean=mu)
    return p, p>alpha

def t_test2(x1,x2):
    t, p = stats2.ttest_ind(x1,x2)
    return p, p>alpha  # 如果p小，是拒绝原假设，认为二者不同，即可以通过该属性区分