import csv


with open('D:/交通/出租车_统计数据/with_time_length/1500M/30mins以上/tmp/质心坐标文件.csv', 'r', newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    # 读取所有点数据
    points = list(reader)
    with open('D:/交通/出租车_统计数据/with_time_length/1500M/30mins以上/tmp/more_thirty_VIF_test_4.csv', 'r', newline='', encoding='utf-8') as infile2:
        independent = csv.reader(infile2)
        y_data = list(independent)
        for idx, point in enumerate(points):
            point.extend(y_data[idx])

        with open('D:/交通/出租车_统计数据/with_time_length/1500M/30mins以上/tmp/30_60_mgwr_file_4.csv', 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            for new_point in points:
                writer.writerow(new_point)
