import joblib
import json
import os
import sys
import glob


def find_pkl(output_dir):
    folder_path = os.path.join(".", output_dir, "results")
    pkl_files = glob.glob(os.path.join(folder_path, "*.pkl"))

    if pkl_files:
        main_function(pkl_files)
    else:
        print("No .pkl files found in the specified output directory.")

def main_function(pkl_dir):
    results = joblib.load(pkl_dir)

    dict = {}

    for outer_key, outer_value in results.items():
        for inner_key, inner_value in outer_value.items():
            if inner_key == 'label': 
                dict[outer_key] = inner_value

    #print(dict())

    with open('label.json', 'w') as json_file:
        json.dump(dict, json_file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pkl_reader.py video.output_dir")
        sys.exit(1)

    output_dir = sys.argv[1]
    find_pkl(output_dir)

'''
results = joblib.load(pkl_dir)

dict = {}

for outer_key, outer_value in results.items():
    for inner_key, inner_value in outer_value.items():
        if inner_key == 'label': 
            dict[outer_key] = inner_value

#print(dict())

with open('label.json', 'w') as json_file:
    json.dump(dict, json_file, indent=4) 


for key1, value1 in results.items():
    print(f"Outer Key: {key1}")
    for key2, value2 in value1.items():
        print(f"Inner Key: {key2}, Inner Value: {value2}")


##print(results.items())
        

formatted_results = {}
for frame_path, frame_data in results.items():
    formatted_frame_data = {
        '2d_joints': frame_data.get('2d_joints', []),
        '3d_joints': frame_data.get('3d_joints', []),
        'annotations': frame_data.get('annotations', []),
        'appe': frame_data.get('appe', []),
        'bbox': frame_data.get('bbox', []),
        'camera': frame_data.get('camera', []),
        'camera_bbox': frame_data.get('camera_bbox', []),
        'center': frame_data.get('center', []),
        'class_name': frame_data.get('class_name', []),
        'conf': frame_data.get('conf', []),
        'frame_path': frame_path,
        'loca': frame_data.get('loca', []),
        'mask': frame_data.get('mask', []),
        'pose': frame_data.get('pose', []),
        'scale': frame_data.get('scale', []),
        'shot': frame_data.get('shot', 0),
        'size': frame_data.get('size', []),
        'smpl': frame_data.get('smpl', []),
        'tid': frame_data.get('tid', []),
        'time': frame_data.get('time', 0),
        'tracked_bbox': frame_data.get('tracked_bbox', []),
        'tracked_ids': frame_data.get('tracked_ids', []),
        'tracked_time': frame_data.get('tracked_time', [])
    }
    formatted_results[frame_path] = formatted_frame_data

print(formatted_results)
'''