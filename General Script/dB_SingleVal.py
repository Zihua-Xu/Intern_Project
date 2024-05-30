import os
import csv
import numpy as np

# 定义一个函数，将复数转换为分贝表示
def complex_to_db(value):
    magnitude = np.abs(value)
    db = 10 * np.log10(magnitude)
    return db

value = complex("3.467168e+08-5.290118e+08j")
# 转换为分贝表示
db_value = complex_to_db(value)

print(db_value)