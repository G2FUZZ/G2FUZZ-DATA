import os
import subprocess

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV file with multiple audio tracks, video filters, custom metadata, watermark overlay, and subtitle overlay
complex_flv_path = './tmp/complex_file.flv'
subprocess.run(['ffmpeg', '-y', '-f', 'lavfi', '-i', 'anoisesrc=volume=0.1', '-f', 'lavfi', '-i', 'color=size=1280x720:rate=30', '-f', 'lavfi', '-i', 'sine=frequency=1000:duration=10', '-i', 'input_subtitle.srt', '-c:a', 'aac', '-c:a', 'mp3', '-c:v', 'libx264', '-t', '10', '-map', '0:a', '-map', '1:v', '-map', '2:a', '-vf', 'scale=640:360,drawtext=fontfile=Arial.ttf:text=\'Custom Text\':x=10:y=10:fontsize=24:fontcolor=white', '-metadata', 'title=Complex FLV', '-i', 'watermark.png', '-i', 'subtitle.srt', '-filter_complex', 'overlay=10:10,subtitles=subtitle.srt', complex_flv_path])

print("FLV file with multiple audio tracks, video filters, custom metadata, watermark overlay, and subtitle overlay generated successfully.")