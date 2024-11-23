import subprocess

# Create an empty mp4 file with audio codec AAC
subprocess.run(['ffmpeg', '-f', 'lavfi', '-i', 'anullsrc', '-t', '5', '-c:a', 'aac', './tmp/audio_aac.mp4'])

# Create an empty mp4 file with audio codec MP3
subprocess.run(['ffmpeg', '-f', 'lavfi', '-i', 'anullsrc', '-t', '5', '-c:a', 'libmp3lame', './tmp/audio_mp3.mp4'])

# Create an empty mp4 file with audio codec AC-3
subprocess.run(['ffmpeg', '-f', 'lavfi', '-i', 'anullsrc', '-t', '5', '-c:a', 'ac3', './tmp/audio_ac3.mp4'])