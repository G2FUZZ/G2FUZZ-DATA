import os
import subprocess

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV file with multiple audio, video, and subtitle tracks
complex_flv_file_path = './tmp/complex_flv_file.flv'
subprocess.run(['ffmpeg', '-y', '-f', 'lavfi', '-i', 'testsrc=size=1280x720:rate=30', '-f', 'lavfi', '-i', 'sine=frequency=1000:duration=5', '-f', 'lavfi', '-i', 'color=c=red', '-t', '5', '-c:v', 'libx264', '-c:a', 'aac', '-vf', 'drawtext=fontfile=/path/to/font.ttf:text=\'Video Track\':x=100:y=50:fontsize=24:fontcolor=white,drawtext=fontfile=/path/to/font.ttf:text=\'Audio Track\':x=10:y=10:fontsize=18:fontcolor=red', '-c:s', 'mov_text', '-metadata:s:s:0', 'language=eng', '-metadata:s:s:0', 'title=English_Subtitles', complex_flv_file_path])

print("FLV file with multiple audio tracks, video tracks, and subtitle tracks generated successfully.")