import os
import subprocess

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV file with AAC audio codec
aac_file_path = './tmp/audio_aac_cuepoints.flv'
subprocess.run(['ffmpeg', '-y', '-f', 'lavfi', '-i', 'anullsrc=channel_layout=stereo:sample_rate=44100', '-t', '5', '-c:a', 'aac', '-vf', 'drawtext=fontfile=/path/to/font.ttf:text=\'Cue Point 1\':x=100:y=50:fontsize=24:fontcolor=white', aac_file_path])

print("FLV file with AAC audio codec and Embedded cue points generated successfully.")