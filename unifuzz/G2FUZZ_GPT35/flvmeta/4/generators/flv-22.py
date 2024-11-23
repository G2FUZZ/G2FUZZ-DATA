import os
import subprocess

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV file with AAC audio codec
aac_file_path = './tmp/audio_aac.flv'
subprocess.run(['ffmpeg', '-y', '-f', 'lavfi', '-i', 'anullsrc=channel_layout=stereo:sample_rate=44100', '-t', '5', '-c:a', 'aac', '-g', '25', aac_file_path])

# Generate FLV file with MP3 audio codec
mp3_file_path = './tmp/audio_mp3.flv'
subprocess.run(['ffmpeg', '-y', '-f', 'lavfi', '-i', 'anullsrc=channel_layout=stereo:sample_rate=44100', '-t', '5', '-c:a', 'mp3', '-g', '25', mp3_file_path])

print("FLV files with AAC and MP3 audio codecs generated successfully with Keyframe indexing.")