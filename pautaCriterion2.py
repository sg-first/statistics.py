import math
import numpy as np

mean=0

def SetMean(listNum): # 每个维度的均值
    global mean
    mean=np.mean(listNum,axis=0)

def StandardDeviation(listNum): # 每个维度的标准差（一维和二维张量这个函数是一样的）
    listXi=listNum-mean
    listXi=listXi*listXi

    sumXi=listXi.sum(axis=0)
    d2=sumXi/(listNum.shape[0]-1)
    return math.sqrt(d2)

def GetGood(listNum):
    sd3=StandardDeviation(listNum)*3 # 三倍标准差
    for j in range(listNum.shape[1]): # 遍历所有维度
        for i in range(listNum.shape[0]): # 遍历所有元素
            if math.fabs(listNum[i,j]-mean)>=sd3[j]: # 偏差大于三倍标准差
                listNum=np.delete(listNum, i, axis=0) # 该元素一行删除
        return listNum

def GetGoodList(listNum): # 接口函数其实只有这一个
    SetMean(listNum)
    while(True):
        num=listNum.shape[0]
        listNum=GetGood(listNum)
        if(listNum.shape[0]==num): # 循环到不能再剔除数据为止
            break
    return listNum