import os
import subprocess

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV file with multiple audio tracks and custom metadata
complex_file_path = './tmp/complex_file.flv'
subprocess.run(['ffmpeg', '-y',
                '-f', 'lavfi', '-i', 'anullsrc=channel_layout=stereo:sample_rate=44100',  # Audio track 1
                '-f', 'lavfi', '-i', 'sine=frequency=1000:duration=5',  # Audio track 2
                '-f', 'lavfi', '-i', 'color=c=red:s=1280x720',  # Video track
                '-c:v', 'libx264', '-preset', 'medium', '-tune', 'film',
                '-c:a:0', 'aac', '-b:a:0', '192k',  # AAC audio codec for track 1
                '-c:a:1', 'mp3', '-b:a:1', '128k',  # MP3 audio codec for track 2
                '-map', '0:a', '-map', '1:a', '-map', '2:v',
                '-metadata', 'title=Complex FLV File',
                '-movflags', 'frag_keyframe+empty_moov',
                complex_file_path])

print("FLV file with multiple audio tracks and custom metadata generated successfully.")