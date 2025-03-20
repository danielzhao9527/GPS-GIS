import csv

'''该文件用于筛选掉车辆经过数为0的网格'''


fishnet_data = 'D:/交通/出租车_统计数据/with_time_length/1500M/30mins以上/tmp/more_thirty_minutes_all.csv'
output_file = 'D:/交通/出租车_统计数据/with_time_length/1500M/30mins以上/tmp/more_thirty_select.csv'
with open(output_file, 'w', newline='') as savefile:
    writer = csv.writer(savefile)
    # 写入列名
    writer.writerow(['fishnet_FID', 'number'])
    # 逐行写入数据
    with open(fishnet_data, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        next(reader)  # 跳过第一行
        for row in reader:
            if int(row[1]) != 0:
                writer.writerow([row[0], row[1]])
