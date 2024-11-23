import os

# Function to write audio data with a specific codec and timestamp to the file
def write_audio_data(file, codec, timestamp, data):
    file.write(f'{timestamp} - {codec} compressed audio data: {data}\n'.encode())

# Function to write video data with timestamp to the file
def write_video_data(file, timestamp, data):
    file.write(f'{timestamp} - Video data: {data}\n'.encode())

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a more complex FLV file with multiple audio and video tracks
with open('./tmp/extended_complex_file.flv', 'wb') as file:
    # Write metadata
    file.write(b'Extended FLV File Metadata\n')

    # Write audio data with different codecs and timestamps
    write_audio_data(file, 'MP3', '00:00:01', 'audio_track1')
    write_audio_data(file, 'AAC', '00:00:03', 'audio_track2')
    write_audio_data(file, 'OPUS', '00:00:05', 'audio_track3')
    
    # Write video data with timestamps
    write_video_data(file, '00:00:02', 'video_track1')
    write_video_data(file, '00:00:04', 'video_track2')
    write_video_data(file, '00:00:06', 'video_track3')