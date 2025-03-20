import csv
import time
import pandas as pd


def extract_columns(input_csv, output_csv, start_column=2):
    with open(input_csv, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)

        with open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)

            for row in reader:
                # 提取从第三列到最后一列的数据
                new_row = row[start_column:]
                writer.writerow(new_row)


def get_vif_file(input_csv, output_csv, start_column=2):
    with open(input_csv, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        # 跳过列名行
        next(reader)
        '''如果是细分时间尺度的 不用跳过0行 因为0行在筛选非0网格阶段已经被排除'''
        # 跳过编号'0'行
        next(reader)
        # 打开要输出的文件
        with open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            # 写列名 这里要根据你的实际变量添加/删减
            writer.writerow(['logistics_density', 'supermarket_density', 'bus_density', 'company_density', 'park_density',
                             'education_density', 'culture_density', 'entertainment_density', 'hospital_density',
                             'bank_density', 'gym_density', 'government_density', 'accommodation_density',
                             'supermarket_distance', 'high_speed_distance', 'bus_distance', 'park_distance',
                             'education_distance', 'culture_distance', 'bank_distance', 'hospital_distance',
                             'logistics_distance'])
            # print("rows numver:", len(reader))
            row_count = 0
            for row in reader:
                if any(row):
                    # 提取从第三列到最后一列的数据
                    new_row = row[start_column:]
                    new_row = list(new_row)
                    variety = 0
                    for idx, data in enumerate(new_row):
                        if idx < 13 and int(new_row[idx]) != 0:
                            variety += 1
                        if idx >= 13:  # 此处要根据POI数量情况修改
                            new_row[idx] = round(float(new_row[idx]), 2)
                            if new_row[idx] == -1.00:
                                new_row[idx] = 20
                            else:
                                new_row[idx] = new_row[idx] / 1000
                    # new_row.append(variety)
                    writer.writerow(new_row)
                    row_count += 1
            print("row_number", row_count)


def replace_value_in_csv(input_csv, output_csv):
    count = 0
    with open(input_csv, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        # 获取列名行
        header = next(reader)
        # 跳过第一行
        next(reader)
        # 读取所有行
        rows = list(reader)

    with open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['logistics_density', 'supermarket_density', 'bus_density', 'company_density', 'park_density',
                         'education_density', 'culture_density', 'entertainment_density', 'hospital_density',
                         'bank_density', 'gym_density', 'government_density', 'accommodation_density',
                         'supermarket_distance', 'high_speed_distance', 'bus_distance', 'park_distane',
                         'education_distance', 'culture_distance', 'bank_distance', 'hospital_distance',
                         'logistics_distance', 'variety'])
        for row in rows:
            # 替换行中的目标值
            new_row = row
            if count < 2:
                print("new_row", new_row)
                count += 1
            variety = 0
            for idx, data in enumerate(new_row):
                if idx < 13 and int(new_row[idx]) != 0:
                    variety += 1
                if idx >= 13:   # 此处要根据POI数量情况修改
                    new_row[idx] = round(float(new_row[idx]), 2)
                    if new_row[idx] == -1.00:
                        new_row[idx] = 20
                    else:
                        new_row[idx] = new_row[idx]/1000
            new_row.append(variety)
            writer.writerow(new_row)


# 输入CSV文件路径
input_csv_path = 'D:/交通/出租车_统计数据/with_time_length/1500M/30mins以上/tmp/more_thirty_match_POIs_3.csv'
# output_csv_path = 'D:/交通/出租车_统计数据/with_time_length/day01/细分时间尺度/0-2mins/0_2mins_POIs_to_VIF_3.csv'

# 输出CSV文件路径
# input_csv_path_1 = output_csv_path
output_csv_path_1 = 'D:/交通/出租车_统计数据/with_time_length/1500M/30mins以上/tmp/more_thirty_VIF_test_4.csv'

# 调用函数，提取第三列到最后一列的数据
# extract_columns(input_csv_path, output_csv_path)
# 调用函数，将CSV文件中的 -1 替换为 10000
# replace_value_in_csv(input_csv_path_1, output_csv_path_1)

get_vif_file(input_csv_path, output_csv_path_1)
