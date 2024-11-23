import os

output_path = './tmp/'

def generate_flv_file(file_name, video_codec='h264', audio_codec='aac', resolution='1920x1080'):
    file_path = os.path.join(output_path, file_name)
    
    # Code for generating FLV file with specified codecs and resolution
    with open(file_path, 'w') as file:
        file.write(f'FLV File: {file_name}\n')
        file.write(f'Video Codec: {video_codec}\n')
        file.write(f'Audio Codec: {audio_codec}\n')
        file.write(f'Resolution: {resolution}\n')
    
    print(f'FLV file "{file_name}" generated with video codec "{video_codec}", audio codec "{audio_codec}", and resolution "{resolution}".')

# Generate FLV file with custom features
generate_flv_file('sample.flv', video_codec='vp9', audio_codec='opus', resolution='1280x720')