import os
import subprocess

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV file with multiple audio tracks, multiple video filters, custom metadata, and watermark overlay
extended_features_flv_path = './tmp/extended_features.flv'
subprocess.run(['ffmpeg', '-y', '-f', 'lavfi', '-i', 'anoisesrc=volume=0.1', '-f', 'lavfi', '-i', 'color=size=1280x720:rate=30', '-f', 'lavfi', '-i', 'sine=frequency=1000:duration=10', '-c:a', 'aac', '-c:a', 'mp3', '-c:v', 'libx264', '-t', '10', '-map', '0:a', '-map', '1:v', '-map', '2:a', '-vf', 'scale=640:360,drawtext=fontfile=Arial.ttf:text=\'Custom Text\':x=10:y=10:fontsize=24:fontcolor=white', '-metadata', 'title=Extended FLV', '-i', 'watermark.png', '-filter_complex', 'overlay=10:10', extended_features_flv_path])

print("FLV file with multiple audio tracks, multiple video filters, custom metadata, and watermark overlay generated successfully.")