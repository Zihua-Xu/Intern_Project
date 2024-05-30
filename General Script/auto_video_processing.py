import os
import subprocess

# 定义要遍历的文件夹路径
folder_path = "your_folder_path_here"

# 获取文件夹中所有的 mp4 文件
mp4_files = [file for file in os.listdir(folder_path) if file.endswith('.mp4')]

# 定义要重复运行的命令模板
command_template = 'python scripts/demo.py video.source="{}" video.output_dir="{}" render.type=HUMAN_BBOX'

# 遍历所有视频文件
for file in mp4_files:
    # 构建输出文件夹的路径，使用视频文件的名称作为文件夹名
    output_folder = os.path.splitext(file)[0]
    output_folder_path = os.path.join(folder_path, output_folder)
    
    # 创建输出文件夹
    os.makedirs(output_folder_path, exist_ok=True)
    
    # 构建具体的命令
    command = command_template.format(os.path.join(folder_path, file), output_folder_path)
    
    # 执行命令
    subprocess.run(command, shell=True)

# 所有视频都已处理完毕，程序结束
print("all done")
