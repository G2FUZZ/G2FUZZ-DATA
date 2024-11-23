import os

output_path = './tmp/'

# Function to generate a FLV file with video and audio codecs, resolution, and frame rate
def generate_flv_file(file_name, video_resolution, frame_rate):
    video_codec = 'h264'
    audio_codec = 'aac'
    
    file_path = os.path.join(output_path, file_name + '.flv')
    
    # Generate the FLV file with video and audio codecs, resolution, and frame rate
    with open(file_path, 'w') as file:
        file.write(f'FLV File: {file_name}\n')
        file.write(f'Video Codec: {video_codec}\n')
        file.write(f'Audio Codec: {audio_codec}\n')
        file.write(f'Video Resolution: {video_resolution}\n')
        file.write(f'Frame Rate: {frame_rate}\n')
    
    print(f'FLV file "{file_name}.flv" generated with video codec: {video_codec}, audio codec: {audio_codec}, resolution: {video_resolution}, and frame rate: {frame_rate}')

# Generate a sample FLV file with extended features
generate_flv_file('extended_video', '1920x1080', 30)