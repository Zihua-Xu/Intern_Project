import os
import csv
import numpy as np

# 定义一个函数，将复数转换为分贝表示
def complex_to_db(value):
    magnitude = np.abs(value)
    db = 10 * np.log10(magnitude)
    return db

# 定义一个函数，将字符串中的 'i' 替换为 'j'
def replace_i_with_j(value_str):
    return value_str.replace('i', 'j')

# 指定文件夹路径
folder_path = 'Data Collection\RF Station 1\RF1 csv_new'

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        print(f"Processing file: {filename}")

        # 读取CSV文件
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)

        # 遍历CSV文件中的每个值，并进行替换和转换
        for i in range(len(data)):
            for j in range(len(data[i])):
                # 替换 'i' 为 'j'
                data[i][j] = replace_i_with_j(data[i][j])
                try:
                    # 尝试将值转换为复数
                    value = complex(data[i][j])
                    # 转换为分贝表示
                    db_value = complex_to_db(value)
                    data[i][j] = db_value
                except ValueError:
                    # 如果值无法转换为复数，则跳过
                    pass

        # 将转换后的数据写回CSV文件
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

print("Conversion complete.")
