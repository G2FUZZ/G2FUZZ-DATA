import os
import random
import time

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Define the content for the FLV files with ActionScript code
def generate_flv_content(file_num):
    flv_content = f"""
    FLV File Format
    File Number: {file_num}
    Features:
    1. Video codecs: H.263, VP6, VP6F, H264
    2. Audio codecs: MP3, AAC, Linear PCM
    3. Scripting Support: FLV files can include ActionScript code for creating interactive applications and games embedded within the video content.
    
    Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}
    """
    return flv_content

# Generate FLV files with the specified features and metadata
for i in range(5):
    file_name = f'./tmp/file_{i+1}.flv'
    with open(file_name, 'w') as f:
        f.write(generate_flv_content(i+1))

print('FLV files with metadata generated successfully.')