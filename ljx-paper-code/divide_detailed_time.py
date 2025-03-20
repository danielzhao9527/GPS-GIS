import csv
import os


def read_data_file(folder_paths, start, stop, result):
    target = 0
    for folder_path in folder_paths:
        # 获取文件夹下所有文件的列表
        files = os.listdir(folder_path)

        # 过滤出CSV文件
        csv_files = [f for f in files if f.endswith('.csv')]

        # 依次读取每个CSV文件
        for csv_file in csv_files:
            file_path = os.path.join(folder_path, csv_file)
            with open(file_path , "r", newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    if len(row) >= 2:
                        number = 0
                        grid_number = int(row[0])
                        for i in range(1, len(row)):
                            if float(row[i]) > start and float(row[i]) <= stop:
                                number += 1
                        result[grid_number] += number
    return target

def write_data_file(output_path, result):
    with open(output_path, 'w', newline='') as savefile:
        writer = csv.writer(savefile)
        # 写入列名
        writer.writerow(['fishnet_FID', 'number'])
        # 逐行写入数据
        for FID in range(len(result)):
            writer.writerow([FID, result[FID]])


def main():
    result = [0] * 59000
    '''时间长度选择  (] 包尾不包头'''
    start = 6 * 60
    stop = 8 * 60
    '''所有要读取的文件所在的文件夹'''
    folder_path = ['D:/交通/出租车_统计数据/with_time_length/500M/5mins/time',
                   'D:/交通/出租车_统计数据/with_time_length/500M/10mins/time']
    read_data_file(folder_path, start, stop, result)

    '''输出保存文件'''
    output_path = 'D:/交通/出租车_统计数据/with_time_length/500M/细分时间尺度/6-8mins/mgwr_test/6_8mins.csv'
    write_data_file(output_path, result)


if __name__ == "__main__":
    main()