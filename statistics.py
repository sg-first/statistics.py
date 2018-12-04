from sklearn.cluster import KMeans
import numpy as np

def entropy(data): # 应传入归一化后数组
    num,dim = data.shape
    dimsum=data.sum(axis=0) # 不同维度所有数据的和
    dataP=data/dimsum # 各个维度除和，创建权重矩阵
    k=1/np.log(num)
    # 计算熵值
    dataE=dataP*np.log(dataP) # 此时仍为二维
    #dataE=np.nan_to_num(dataE) # 看数据再加这个
    dataE=-k*dataE.sum(axis=0) # 变为一维
    # 计算信息熵冗余度
    dataD=1-dataE
    #计算各个指标（维度）权值
    return dataD/dataD.sum(axis=0)

def kmean(data,classNum):
    estimator = KMeans(n_clusters=classNum)  # 构造聚类器
    estimator.fit(data)  # 聚类
    return estimator.cluster_centers_, estimator.labels_ #返回聚类中心和标签

graRho=0.5 # 分辨系数

def gra(data): # 使用前归一化，比较列放在第一行
    m,n=data.shape
    ck=data[:,0] # 第一列是参考列
    bj=data[:,1:] # 比较列
    m,n2=bj.shape # 求出比较列列数n2
    for i in range(n2):
        bj[:,i]=bj[:,i]-ck
    absbj=np.abs(bj)
    mn=np.min(absbj)
    mx=np.max(absbj)
    ksi= (mn + graRho * mx) / (absbj + graRho * mx) # 求关联系数
    r=np.sum(ksi,axis=0)/m # 求关联度
    return r
