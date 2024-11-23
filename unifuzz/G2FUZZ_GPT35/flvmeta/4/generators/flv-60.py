import os
import subprocess

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV file with multiple audio, video, and subtitle tracks with specific configurations
complex_flv_file_path = './tmp/extended_complex_flv_file.flv'
subprocess.run(['ffmpeg', 
                '-y',
                '-f', 'lavfi', '-i', 'testsrc=size=1280x720:rate=30', 
                '-f', 'lavfi', '-i', 'sine=frequency=1000:duration=5', 
                '-f', 'lavfi', '-i', 'color=c=blue',
                '-f', 'lavfi', '-i', 'anoisesrc=r=48000:cl=.5', 
                '-f', 'lavfi', '-i', 'mandelbrot=size=1280x720', 
                '-t', '10', 
                '-c:v', 'libx264', 
                '-c:a:0', 'aac', 
                '-c:a:1', 'mp3', 
                '-vf', 'drawtext=fontfile=/path/to/font.ttf:text=\'Video Track\':x=100:y=50:fontsize=24:fontcolor=white,drawtext=fontfile=/path/to/font.ttf:text=\'Audio Track 1\':x=10:y=10:fontsize=18:fontcolor=red,drawtext=fontfile=/path/to/font.ttf:text=\'Audio Track 2\':x=10:y=30:fontsize=18:fontcolor=green', 
                '-c:s:0', 'mov_text', 
                '-c:s:1', 'mov_text', 
                '-metadata:s:s:0', 'language=eng', 
                '-metadata:s:s:0', 'title=English_Subtitles', 
                '-metadata:s:s:1', 'language=eng', 
                '-metadata:s:s:1', 'title=Additional_Subtitles', 
                complex_flv_file_path])

print("Extended FLV file with multiple audio tracks, video tracks, and subtitle tracks with specific configurations generated successfully.")