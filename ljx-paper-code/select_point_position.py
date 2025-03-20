import csv
import time

'''
该文件用于生成 "质心坐标文件"
'''

# 记录了要筛选的渔网点的文件
point_file = 'D:/交通/出租车_统计数据/with_time_length/1500M/30mins以上/tmp/more_thirty_select.csv'
# 记录了渔网每个质心坐标的文件
fishnet_position = 'D:/交通/出租车_统计数据/with_time_length/1500M/渔网质心坐标.csv'

Data = []
with open(point_file, 'r', newline='') as file:
    reader = csv.reader(file)
    next(reader)
    with open(fishnet_position, 'r', newline='') as p_file:
        positions = csv.reader(p_file)
        next(positions)
        for point in reader:
            site = []
            for pos in positions:
                # 找到该点对应的渔网质心
                if point[0] == pos[0]:
                    # 添加编号
                    site.append(pos[0])
                    # 添加x坐标
                    site.append(pos[1])
                    # 添加y坐标
                    site.append(pos[2])
                    # 添加因变量
                    site.append(point[1])
                    Data.append(site)
                    break


# 把信息填入csv文件并输出
output_file = 'D:/交通/出租车_统计数据/with_time_length/1500M/30mins以上/tmp/质心坐标文件.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['fishnet_FID', 'center_X', 'center_Y', 'number'])
    for site in Data:
        if int(site[0]) == 0:
            continue
        writer.writerow([site[0], site[1], site[2], site[3]])
    print("保存坐标点数:", len(Data))
    print("文件已保存到:", output_file)

