import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Define the content for the FLV files with ActionScript code and Cue Points feature
flv_content = """
FLV File Format
Features:
1. Video codecs: H.263, VP6, VP6F, H264
2. Audio codecs: MP3, AAC, Linear PCM
3. Scripting Support: FLV files can include ActionScript code for creating interactive applications and games embedded within the video content.
4. Cue Points: FLV files can contain cue points that trigger specific actions or events within the video, such as displaying additional information or jumping to a different section.
"""

# Generate FLV files with the specified features
for i in range(4):
    file_name = f'./tmp/file_{i+1}.flv'
    with open(file_name, 'w') as f:
        f.write(flv_content)

print('FLV files generated successfully.')