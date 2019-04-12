import csv

def readCsv(path):
    birth_data = []
    with open(path) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        for row in csv_reader:  # 将csv文件中的数据保存到birth_data中
            birth_data.append(row)

    birth_data = [[float(x) for x in row] for row in birth_data]  # 将数据从string形式转换为float形式
    return birth_data  # 将list数组转化成array数组便于查看数据结构

def writeFile(filePath, content):
    print('Write info to file:Start...')
    # 将文件内容写到文件中
    with open(filePath, 'a', encoding='utf-8') as f:
        f.write(content)
        print('Write info to file:end...')

def readFile(filePath):
    with open(filePath, 'r') as f:
        return f.read()

def saveCsv(path,list):
    content=''
    for i in list:
        for j in i:
            content+=str(j)+','
        content+='\n'
    writeFile(path,content)
