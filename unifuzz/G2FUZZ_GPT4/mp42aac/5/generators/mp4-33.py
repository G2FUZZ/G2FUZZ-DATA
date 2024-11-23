import cv2
import numpy as np
import os
import subprocess

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def generate_scene(filename, width, height, fps, duration, color):
    """
    Generates a scene with specified parameters.
    """
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(filename, fourcc, fps, (width, height))
    total_frames = fps * duration
    
    for _ in range(int(total_frames)):
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        cv2.rectangle(frame, (20, 20), (width-20, height-20), color, -1)
        video.write(frame)
    
    video.release()

def merge_videos(filenames, output_filename):
    """
    Merges videos using ffmpeg.
    """
    filter_str = ''.join([f"[{i}:v:0][{i}:a:0]" for i in range(len(filenames))]) + f"concat=n={len(filenames)}:v=1:a=0[outv][outa]"
    cmd = ['ffmpeg', '-y'] + sum([['-i', f] for f in filenames], []) + ['-filter_complex', filter_str, '-map', '[outv]', '-map', '[outa]', output_filename]
    subprocess.run(cmd)

# Parameters for the scenes
scenes = [
    {'width': 640, 'height': 480, 'fps': 24, 'duration': 5, 'color': (255, 0, 0)},  # Red scene
    {'width': 320, 'height': 240, 'fps': 30, 'duration': 3, 'color': (0, 255, 0)},  # Green scene
    {'width': 1280, 'height': 720, 'fps': 60, 'duration': 4, 'color': (0, 0, 255)},  # Blue scene
]

scene_filenames = []

for i, scene in enumerate(scenes):
    filename = os.path.join(output_dir, f"scene_{i}.mp4")
    generate_scene(filename, **scene)
    scene_filenames.append(filename)

# Output filename for the merged video
output_filename = os.path.join(output_dir, "complex_structure_video.mp4")

# Merge the scenes into a single video
merge_videos(scene_filenames, output_filename)

print(f"Generated video with complex structure: {output_filename}")