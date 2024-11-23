import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a more complex FLV file with audio and video data interleaved
def generate_complex_flv_file(file_path):
    # Simulating audio and video data for demonstration purposes
    audio_data = b'Audio data...'
    video_data = b'Video data...'
    
    with open(file_path, 'wb') as file:
        # Write audio and video data interleaved in a sequential order
        for i in range(5):  # Simulating multiple frames of audio and video data
            file.write(audio_data)
            file.write(video_data)
    
    print('Complex FLV file with audio and video data generated successfully.')

# Generate a complex FLV file with audio and video data interleaved
generate_complex_flv_file('./tmp/complex.flv')