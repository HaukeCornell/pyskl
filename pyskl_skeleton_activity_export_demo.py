# ! This file has to be run from the pyskl repository for correct parsing of relative paths

# Used to pass input files and output directory to the pyskl scripts used for processing video 
# works for both activity and just skeleton scripts 
# Script skeleton: Audit_Skeletons/Scripts/export_skeleton_from_video.py
# Script activity: pyskl/demo/demo_skeleton.py

# Individual files can be processed like the demo specifies: 
# https://github.com/kennymckormick/pyskl/blob/main/demo/demo_skeleton.py
# `python demo/demo_skeleton.py demo/ntu_sample.avi demo/demo.mp4`


import os
import subprocess

input_dir = '/media/farlab/Seagate Portable Drive/dev/Audit_Skeletons/Public_Test_Data/Defaced_VideoSnippets'
output_dir = '/media/farlab/Seagate Portable Drive/dev/Audit_Skeletons/Public_Test_Data/Skeleton_From_Video'

# Make sure output directory exists
os.makedirs(output_dir, exist_ok=True)

# List all files in the input directory
for file in os.listdir(input_dir):
    if file.endswith(".mp4"):
        input_file = os.path.join(input_dir, file)
        output_file = os.path.join(output_dir, file)

        # Construct the command
        cmd = [# 'python', 'demo/demo_skeleton.py',
            'python', 'demo/export_skeleton_from_video.py',
            input_file, output_file
        ]

        # Execute the command
        subprocess.run(cmd, check=True)
