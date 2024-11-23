import os

output_path = './tmp/'

# Function to generate a FLV file with video and audio codecs
def generate_flv_file(file_name):
    video_codec = 'h264'
    audio_codec = 'aac'
    
    file_path = os.path.join(output_path, file_name + '.flv')
    
    # Generate the FLV file with video and audio codecs
    with open(file_path, 'w') as file:
        file.write(f'FLV File: {file_name}\n')
        file.write(f'Video Codec: {video_codec}\n')
        file.write(f'Audio Codec: {audio_codec}\n')
    
    print(f'FLV file "{file_name}.flv" generated with video codec: {video_codec} and audio codec: {audio_codec}')

# Generate a sample FLV file
generate_flv_file('sample_video')