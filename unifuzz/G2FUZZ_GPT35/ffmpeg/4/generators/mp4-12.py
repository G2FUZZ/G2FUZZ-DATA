import subprocess

# Create an empty mp4 file with audio codec AAC and aspect ratio information
subprocess.run(['ffmpeg', '-f', 'lavfi', '-i', 'anullsrc', '-vf', 'setsar=16:9', '-t', '5', '-c:a', 'aac', './tmp/audio_aac_aspect_ratio.mp4'])

# Create an empty mp4 file with audio codec MP3 and aspect ratio information
subprocess.run(['ffmpeg', '-f', 'lavfi', '-i', 'anullsrc', '-vf', 'setsar=16:9', '-t', '5', '-c:a', 'libmp3lame', './tmp/audio_mp3_aspect_ratio.mp4'])

# Create an empty mp4 file with audio codec AC-3 and aspect ratio information
subprocess.run(['ffmpeg', '-f', 'lavfi', '-i', 'anullsrc', '-vf', 'setsar=16:9', '-t', '5', '-c:a', 'ac3', './tmp/audio_ac3_aspect_ratio.mp4'])