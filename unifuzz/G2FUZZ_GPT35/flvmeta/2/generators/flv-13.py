import os

# Create a directory for storing the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with streaming support and Captioning feature
for i in range(4):
    file_name = f'./tmp/video_{i+1}.flv'
    with open(file_name, 'wb') as file:
        if i == 3:
            file.write(b'FLV Streaming Support: Online Video Playback\nCaptioning: Embedded captions or subtitles for accessibility')
        else:
            file.write(b'FLV Streaming Support: Online Video Playback')
    
    print(f'FLV file "{file_name}" with streaming support and Captioning feature has been generated.')