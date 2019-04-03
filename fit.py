import scipy.stats as stats

def normFit(mean,std):
    result = stats.norm(mean, std)
    pdf=lambda x : result.pdf(x)
    cdf=lambda x : result.cdf(x)
    return pdf,cdf