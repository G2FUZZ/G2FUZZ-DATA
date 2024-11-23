import subprocess

# Create a dummy mp4 file with commonly used AAC audio codec
subprocess.run(['ffmpeg', '-f', 'lavfi', '-i', 'anullsrc', '-t', '5', '-c:a', 'aac', './tmp/audio_aac.mp4'])