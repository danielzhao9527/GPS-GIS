import os
import csv
import time

# 定义表示渔网编号的列表
fishnet = [0] * 14829
fishnet_epoch = [0] * 14829

startTime_list = [[] for _ in range(14830)]

processed_count = 0
# 打开记录了 文件名 的 csv文件
catalogue_file = '../data/different_trailTime/five_trail_sub_file/output_1.csv'
with open(catalogue_file, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # 跳过第一行

    # 遍历 "文件名" CSV文件的每一行数据
    for row in reader:
        # 获取文件名（文件名在每行的第一个位置）和 出发时间
        target_filename = row[0]
        Time = row[1]
        sub_time = Time[11:16]
        # print("filename:", target_filename)
        passed_grid = []
        # 读取文本文件并处理每一行
        with open('../data/five_nodes_distribution.txt', 'r') as file:
            # 遍历 txt 文件的每一行数据
            for line in file:
                # 去除行末的换行符，并将行拆分为列表（按逗号分隔）
                txt_data = line.strip().split(',')
                # 获取第三个数据，并检查是否等于文件名
                if len(txt_data) >= 3 and txt_data[2] == target_filename:
                    grid_num = int(txt_data[6])
                    # print("grid_num:", grid_num)
                    # 判断 本段轨迹中 是否已经经过该网格 如没经过 添加记录
                    if fishnet_epoch[grid_num] == 0:
                        fishnet[grid_num] += 1
                        # 填加时间
                        startTime_list[grid_num].append(sub_time)
                        fishnet_epoch[grid_num] = 1
                        # 记录本段轨迹中已被记录过的网格
                        passed_grid.append(grid_num)
                        # print("fishnet[", grid_num, "]:", fishnet[grid_num])
        for x in passed_grid:
            fishnet_epoch[x] = 0
        processed_count += 1
        if processed_count % 1000 == 0:
            print("已处理文件数：", processed_count)


# 保存统计情况到csv文件中
output_path = '../data/fishnet_trailTime/five_minutes_1.csv'
with open(output_path, 'w', newline='') as savefile:
    writer = csv.writer(savefile)
    # 写入列名
    writer.writerow(['fishnet_FID', 'number'])
    # 逐行写入数据
    for FID in range(len(fishnet)):
        writer.writerow([FID, fishnet[FID]])

time_file = '../data/fishnet_trailTime/five_minutes_startTime_1.csv'
with open(time_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for index, sublist in enumerate(startTime_list):
        writer.writerow([index] + sublist)

