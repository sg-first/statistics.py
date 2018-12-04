import math
import numpy as np

mean=0

def SetMean(listNum):
    global mean
    mean=listNum.sum(axis=0) / listNum.shape[0]

def StandardDeviation(listNum):
    listXi=listNum-mean
    listXi=listXi*listXi

    sumXi=listXi.sum(axis=0)
    d2=sumXi/(listNum.shape[0]-1)
    return math.sqrt(d2)

def GetGood(listNum):
    sd3=StandardDeviation(listNum)*3 # 三倍标准差
    for i in range(listNum.shape[0]):
        if math.fabs(listNum[i]-mean)>=sd3: # 偏差大于三倍标准差
            listNum=np.delete(listNum, i, axis=0)
    return listNum

def GetGoodList(listNum): # 接口函数其实只有这一个
    SetMean(listNum)
    while(True):
        num=listNum.shape[0]
        listNum=GetGood(listNum)
        if(listNum.shape[0]==num): # 循环到不能再剔除数据为止
            break
    return listNum