import os

def generate_flv_file(file_name, resolution='1920x1080', audio_bitrate='320k'):
    # Generate a sample flv file
    command = f'ffmpeg -f lavfi -i testsrc=size={resolution}:rate=1 -f lavfi -i sine=frequency=1000:duration=5 -c:v libx264 -b:v 1M -c:a aac -b:a {audio_bitrate} {file_name}.flv'
    
    os.system(command)
    print(f'Generated {file_name}.flv with resolution {resolution} and audio bitrate {audio_bitrate}')

# Usage
generate_flv_file('./tmp/sample_video', resolution='1280x720', audio_bitrate='256k')