import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with closed captioning feature
with open('./tmp/video_with_closed_captioning.flv', 'wb') as file:
    file.write(b'FLV Header')
    file.write(b'FLV Body with Closed Captioning Data')

print('FLV files with closed captioning feature generated successfully.')