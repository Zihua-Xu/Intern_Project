import os
import shlex

def process_pkl_files(input_folder, output_folder):
    pkl_files = [f for f in os.listdir(input_folder) if f.endswith('.pkl')]
    
    for pkl_file in pkl_files:
        pkl_path = os.path.join(input_folder, pkl_file)
        csv_file = os.path.splitext(pkl_file)[0] + '.csv'
        csv_path = os.path.join(output_folder, csv_file)
        # 将文件名转义并构建命令
        pkl_path_escaped = shlex.quote(pkl_path)
        csv_path_escaped = shlex.quote(csv_path)
        command = f"python pkl_to_csv.py pkl.source={pkl_path_escaped} csv.output_dir={csv_path_escaped}"
        os.system(command)

input_folder = 'pkl_files'
output_folder = 'csv_files'
process_pkl_files(input_folder, output_folder)
