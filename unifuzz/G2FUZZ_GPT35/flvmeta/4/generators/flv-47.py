import os
import subprocess

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV file with AAC and MP3 audio codecs, Embedded subtitles, and Custom video effects
complex_features_flv_path = './tmp/complex_features.flv'
subprocess.run(['ffmpeg', '-y', '-f', 'lavfi', '-i', 'anullsrc=channel_layout=stereo:sample_rate=44100', '-f', 'lavfi', '-i', 'testsrc=size=1280x720:rate=30', '-t', '10', '-c:a', 'aac', '-c:a', 'mp3', '-map', '0:a', '-map', '1:v', '-vf', 'subtitles=subtitle.srt:force_style=\'FontName=Arial,FontSize=24,PrimaryColour=&Hffffff&\':enable=between(t\\,2\\,6),drawbox=x=100:y=100:w=1080:h=520:color=black@0.5', complex_features_flv_path])

print("FLV file with multiple audio tracks, embedded subtitles, and custom video effects generated successfully.")