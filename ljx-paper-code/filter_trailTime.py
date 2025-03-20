import os
import csv

# 定义要读取的 CSV 文件路径
csv_files = ["../data/driving_time_1.csv", "../data/driving_time_2.csv", "../data/driving_time_3.csv", "../data/driving_time_4.csv"]

five_mins = 0
ten_mins = 0
fifteen_mins = 0
twenty_mins = 0
thirty_mins = 0
forty_mins = 0
fifty_mins = 0
one_hour = 0

five_trailName = []
five_beginTime = []

ten_trailName = []
ten_beginTime = []

fifteen_trailName = []
fifteen_beginTime = []

twenty_trailName = []
twenty_beginTime = []

thirty_trailName = []
thirty_beginTime = []

forty_trailName = []
forty_beginTime = []

fifty_trailName = []
fifty_beginTime = []

one_hour_trailName = []
one_hour_beginTime = []

for filename in csv_files:
    # 打开 CSV 文件进行读取
    with open(filename, "r", newline='', encoding='utf-8') as csvfile:
        # 创建 CSV reader 对象
        reader = csv.reader(csvfile)

        # 逐行读取 CSV 文件
        for row in reader:
            # 提取每行的最后一个数据进行处理
            seconds = float(row[-1])
            if seconds <= 300:
                five_mins += 1
                five_trailName.append(row[0])
                five_beginTime.append(row[1])
            elif seconds <= 600:
                ten_mins += 1
                ten_trailName.append(row[0])
                ten_beginTime.append(row[1])
            elif seconds <= 900:
                fifteen_mins += 1
                fifteen_trailName.append(row[0])
                fifteen_beginTime.append(row[1])
            elif seconds <= 1200:
                twenty_mins += 1
                twenty_trailName.append(row[0])
                twenty_beginTime.append(row[1])
            elif seconds <= 1800:
                thirty_mins += 1
                thirty_trailName.append(row[0])
                thirty_beginTime.append(row[1])
            elif seconds <= 2400:
                forty_mins += 1
                forty_trailName.append(row[0])
                forty_beginTime.append(row[1])
            elif seconds <= 3000:
                fifty_mins += 1
                fifty_trailName.append(row[0])
                fifty_beginTime.append(row[1])
            else:
                one_hour += 1
                one_hour_trailName.append(row[0])
                one_hour_beginTime.append(row[1])

output_files = ["../data/different_trailTime/five_trail.csv", "../data/different_trailTime/ten_trail.csv", "../data/different_trailTime/fifteen_trail.csv", "../data/different_trailTime/twenty_trail.csv",
                "../data/different_trailTime/thirty_trail.csv", "../data/different_trailTime/forty_trail.csv", "../data/different_trailTime/fifty_trail.csv", "../data/different_trailTime/one_hour_trail.csv"]

filename_list = [five_trailName, ten_trailName, fifteen_trailName, twenty_trailName, thirty_trailName, forty_trailName, fifty_trailName, one_hour_trailName]
beginTime_list = [five_beginTime, ten_beginTime, fifteen_beginTime, twenty_beginTime, thirty_beginTime, forty_beginTime, fifty_beginTime, one_hour_beginTime]

for i in range(len(output_files)):

    # 打开输出 CSV 文件，以追加模式写入
    with open(output_files[i], "a", newline='', encoding='utf-8') as csvfile:
        # 创建 CSV writer 对象
        writer = csv.writer(csvfile)

        trailName = filename_list[i]
        beginTime = beginTime_list[i]
        # 写入 CSV 文件的标题行
        writer.writerow(["trailFilename", "beginTime"])

        for j in range(len(trailName)):
            writer.writerow([trailName[j], beginTime[j]])

