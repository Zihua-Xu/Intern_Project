import joblib
import pandas as pd
import sys
import os

# 解析命令行参数
args = sys.argv[1:]
pkl_source = None
output_folder = None

for arg in args:
    if arg.startswith("pkl.source="):
        pkl_source = arg.split("=")[1]
    elif arg.startswith("csv.output_dir="):
        output_folder = arg.split("=")[1]

if pkl_source is None:
    print("Please provide the path to the .pkl file using the argument: pklsource=...")
    sys.exit(1)

if output_folder is None:
    output_folder = input("Enter the path to the output folder: ")

# 检查文件是否存在
if not os.path.exists(pkl_source):
    print(f"The specified .pkl file '{pkl_source}' does not exist.")
    sys.exit(1)

# Load pkl files
results = joblib.load(pkl_source)

# Create output folder
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Create a empty string to store all label data
label_text = ""

for frame_path, frame_data in results.items():
    # Get frame labels
    frame_label = frame_data.get('label', None)

    # Convert label format to string
    label_info = f"{frame_label}\n"

    # Add label data to label_text
    label_text += label_info

# Extract output filename
output_txt_filename = os.path.join(output_folder, os.path.splitext(os.path.basename(pkl_source))[0] + ".txt")

# Write label_text to txt file
with open(output_txt_filename, 'w') as file:
    file.write(label_text)

print(f"{output_txt_filename} is ready")


# 读取txt文件
with open(output_txt_filename, "r") as file:
    lines = file.readlines()

# 初始化一个列表用于存储所有数据点
data_points = []

# 初始化时间变量
time = 0

# 提取动作及其对应的百分比
for line in lines:
    action_dict = eval(line.strip()) if line.strip() != "None" else {}  # 使用eval将字符串转换为字典，或者如果是 "None" 则使用空字典
    data_point = {"time": time}
    for key, value in action_dict.items():
        for item in value:
            percentage, action = item.split(" : ")
            percentage = int(percentage.replace("%", ""))
            data_point[action] = percentage
    data_points.append(data_point)
    time += 100  # 时间序列增加100，即使是在 "None" 的情况下也会增加

# 创建DataFrame
df = pd.DataFrame(data_points)

# 将缺失值替换为0
df = df.fillna(0)

# 将百分比转换为小数
df = df.apply(lambda x: x / 100)

# 获取输出CSV文件名
output_csv_filename = os.path.join(output_folder, os.path.splitext(os.path.basename(pkl_source))[0] + ".csv")

# 保存为CSV文件
df.to_csv(output_csv_filename, index=False)

print(f"{output_csv_filename} is ready")
