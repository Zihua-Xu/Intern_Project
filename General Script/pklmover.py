import os
import shutil

def copy_all_pkls(source_folder, destination_folder):
    # 创建目标文件夹
    os.makedirs(destination_folder, exist_ok=True)
    
    # 遍历源文件夹及其子文件夹
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.pkl'):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)
                # 检查目标文件夹中是否已经存在同名文件
                if os.path.exists(destination_path):
                    # 如果存在同名文件，则比较文件大小
                    source_size = os.path.getsize(source_path)
                    destination_size = os.path.getsize(destination_path)
                    if source_size > destination_size:
                        # 如果源文件较大，则复制替换目标文件
                        shutil.copy2(source_path, destination_path)
                        print(f"Replaced {destination_path} with {source_path}")
                    else:
                        # 如果目标文件较大，则跳过复制操作
                        print(f"Skipped {source_path} as {destination_path} already exists and is larger")
                else:
                    # 如果目标文件夹中不存在同名文件，则直接复制
                    shutil.copy2(source_path, destination_path)
                    print(f"Copied {source_path} to {destination_path}")

# 设置源文件夹和目标文件夹的路径
source_folder = '.'  # 当前文件夹
destination_folder = './pkl_files'  # 新的文件夹名

# 执行复制操作
copy_all_pkls(source_folder, destination_folder)
