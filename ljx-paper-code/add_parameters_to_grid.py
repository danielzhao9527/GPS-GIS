import csv

def extract_substring(file_path):
    # 使用 rfind 方法找到最后一个 '/' 的位置
    start = file_path.rfind('/') + 1
    # 使用 find 方法找到 '.txt' 的位置
    end = file_path.find('.txt')
    # 截取 '/' 到 '.txt' 之间的字符段
    return file_path[start:end]


def get_line_num(readfile):
    line_num = 0
    with open(readfile, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            line_num += 1
    print("该文件的行数为：", line_num)
    return line_num+10


POIs_path = [

  'D:/交通/出租车_统计数据/POIs/密度/物流速递密度.txt', 'D:/交通/出租车_统计数据/POIs/密度/超级市场密度.txt',
  'D:/交通/出租车_统计数据/POIs/密度/公交站密度.txt', 'D:/交通/出租车_统计数据/POIs/密度/公司企业密度.txt',
  'D:/交通/出租车_统计数据/POIs/密度/公园景区密度.txt', 'D:/交通/出租车_统计数据/POIs/密度/教育服务密度.txt',
  'D:/交通/出租车_统计数据/POIs/密度/文化设施密度.txt', 'D:/交通/出租车_统计数据/POIs/密度/休闲娱乐密度.txt',
  'D:/交通/出租车_统计数据/POIs/密度/医院密度.txt', 'D:/交通/出租车_统计数据/POIs/密度/银行密度.txt',
  'D:/交通/出租车_统计数据/POIs/密度/运动场馆密度.txt', 'D:/交通/出租车_统计数据/POIs/密度/政府机关单位密度.txt',
  'D:/交通/出租车_统计数据/POIs/密度/住宿服务密度.txt',
  'D:/交通/出租车_统计数据/POIs/质心距离20km版/超级市场到质心距离.txt', 'D:/交通/出租车_统计数据/POIs/质心距离20km版/高铁站到质心距离.txt',
  'D:/交通/出租车_统计数据/POIs/质心距离20km版/公交站到质心距离.txt', 'D:/交通/出租车_统计数据/POIs/质心距离20km版/公园景区到质心距离.txt',
  'D:/交通/出租车_统计数据/POIs/质心距离20km版/教育服务到质心距离.txt', 'D:/交通/出租车_统计数据/POIs/质心距离20km版/文化设施到质心距离.txt',
  'D:/交通/出租车_统计数据/POIs/质心距离20km版/银行到质心距离.txt', 'D:/交通/出租车_统计数据/POIs/质心距离20km版/医院到质心距离.txt',
  'D:/交通/出租车_统计数据/POIs/质心距离20km版/物流速递到质心距离.txt'
]

POIs_path_1500 = [

  'D:/交通/出租车_统计数据/with_time_length/1500M/密度/物流速递密度.txt', 'D:/交通/出租车_统计数据/with_time_length/1500M/密度/超级市场密度.txt',
  'D:/交通/出租车_统计数据/with_time_length/1500M/密度/公交站密度.txt', 'D:/交通/出租车_统计数据/with_time_length/1500M/密度/公司企业密度.txt',
  'D:/交通/出租车_统计数据/with_time_length/1500M/密度/公园景区密度.txt', 'D:/交通/出租车_统计数据/with_time_length/1500M/密度/教育服务密度.txt',
  'D:/交通/出租车_统计数据/with_time_length/1500M/密度/文化设施密度.txt', 'D:/交通/出租车_统计数据/with_time_length/1500M/密度/休闲娱乐密度.txt',
  'D:/交通/出租车_统计数据/with_time_length/1500M/密度/医院密度.txt', 'D:/交通/出租车_统计数据/with_time_length/1500M/密度/银行密度.txt',
  'D:/交通/出租车_统计数据/with_time_length/1500M/密度/运动场馆密度.txt', 'D:/交通/出租车_统计数据/with_time_length/1500M/密度/政府机关单位密度.txt',
  'D:/交通/出租车_统计数据/with_time_length/1500M/密度/住宿服务密度.txt',
  'D:/交通/出租车_统计数据/with_time_length/1500M/质心距离/超级市场到质心距离.txt', 'D:/交通/出租车_统计数据/with_time_length/1500M/质心距离/地铁站到质心距离.txt',
  'D:/交通/出租车_统计数据/with_time_length/1500M/质心距离/公交站到质心距离.txt', 'D:/交通/出租车_统计数据/with_time_length/1500M/质心距离/公园景区到质心距离.txt',
  'D:/交通/出租车_统计数据/with_time_length/1500M/质心距离/教育服务到质心距离.txt', 'D:/交通/出租车_统计数据/with_time_length/1500M/质心距离/文化设施到质心距离.txt',
  'D:/交通/出租车_统计数据/with_time_length/1500M/质心距离/银行到质心距离.txt', 'D:/交通/出租车_统计数据/with_time_length/1500M/质心距离/医院到质心距离.txt',
  'D:/交通/出租车_统计数据/with_time_length/1500M/质心距离/物流速递到质心距离.txt'
]

POIs_path_500 = [

  'D:/交通/出租车_统计数据/with_time_length/500M/密度/物流速递密度.txt', 'D:/交通/出租车_统计数据/with_time_length/500M/密度/超级市场密度.txt',
  'D:/交通/出租车_统计数据/with_time_length/500M/密度/公交站密度.txt', 'D:/交通/出租车_统计数据/with_time_length/500M/密度/公司企业密度.txt',
  'D:/交通/出租车_统计数据/with_time_length/500M/密度/公园景区密度.txt', 'D:/交通/出租车_统计数据/with_time_length/500M/密度/教育服务密度.txt',
  'D:/交通/出租车_统计数据/with_time_length/500M/密度/文化设施密度.txt', 'D:/交通/出租车_统计数据/with_time_length/500M/密度/休闲娱乐密度.txt',
  'D:/交通/出租车_统计数据/with_time_length/500M/密度/医院密度.txt', 'D:/交通/出租车_统计数据/with_time_length/500M/密度/银行密度.txt',
  'D:/交通/出租车_统计数据/with_time_length/500M/密度/运动场馆密度.txt', 'D:/交通/出租车_统计数据/with_time_length/500M/密度/政府机关单位密度.txt',
  'D:/交通/出租车_统计数据/with_time_length/500M/密度/住宿服务密度.txt',
  'D:/交通/出租车_统计数据/with_time_length/500M/质心距离/超级市场到质心距离.txt', 'D:/交通/出租车_统计数据/with_time_length/500M/质心距离/地铁站到质心距离.txt',
  'D:/交通/出租车_统计数据/with_time_length/500M/质心距离/公交站到质心距离.txt', 'D:/交通/出租车_统计数据/with_time_length/500M/质心距离/公园景区到质心距离.txt',
  'D:/交通/出租车_统计数据/with_time_length/500M/质心距离/教育服务到质心距离.txt', 'D:/交通/出租车_统计数据/with_time_length/500M/质心距离/文化设施到质心距离.txt',
  'D:/交通/出租车_统计数据/with_time_length/500M/质心距离/银行到质心距离.txt', 'D:/交通/出租车_统计数据/with_time_length/500M/质心距离/医院到质心距离.txt',
  'D:/交通/出租车_统计数据/with_time_length/500M/质心距离/物流速递到质心距离.txt'
]

grid_num = []
'''获取要读取的文件的行数'''
lines_num = get_line_num('D:/交通/出租车_统计数据/with_time_length/500M/local_Moran_I/building_moranI.csv')
statistics = [[] for _ in range(lines_num)]
fishnet_data = 'D:/交通/出租车_统计数据/with_time_length/500M/local_Moran_I/building_moranI.csv'
with open(fishnet_data, 'r', newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    # next(reader)  # 跳过第一行
    for idx, row in enumerate(reader):
        statistics[idx].extend(row)
        if idx != 0:
            grid_num.append(int(row[0]))


'''修改要添加的POIs文件列表'''
for txt_path in POIs_path_500:
    with open(txt_path, 'r') as txtfile:
        print(txt_path)
        next(txtfile)
        # 添加列名
        column_name = extract_substring(txt_path)
        statistics[0].append(column_name)
        # 遍历 txt 文件的每一行数据
        for line in txtfile:
            # 去除行末的换行符，并将行拆分为列表（按逗号分隔）
            txt_data = line.strip().split(',')
            # 检查该编号是否在统计网格内
            for idx, num in enumerate(grid_num):
                if int(float(txt_data[1])) == num:
                    statistics[idx+1].append(txt_data[-1])


output_path = 'D:/交通/出租车_统计数据/with_time_length/500M/local_Moran_I/building_moranI.csv'
with open(output_path, 'w', newline='', encoding='utf-8') as savefile:
    writer = csv.writer(savefile)
    for i in range(len(statistics)):
        writer.writerow(statistics[i])

