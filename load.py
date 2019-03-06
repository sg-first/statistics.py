import csv
import numpy as np

def readCsv(path):
    birth_data = []
    with open(path) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        birth_header = next(csv_reader)  # 读取第一行每一列的标题
        for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
            birth_data.append(row)

    birth_data = [[float(x) for x in row] for row in birth_data]  # 将数据从string形式转换为float形式
    return np.array(birth_data)  # 将list数组转化成array数组便于查看数据结构