import os

# Create a directory to store the generated FLV files
os.makedirs('tmp', exist_ok=True)

# Generate FLV files with dummy content and Timecode information
for i in range(3):
    file_name = f'./tmp/video_{i}.flv'
    with open(file_name, 'wb') as file:
        # Write dummy FLV content for video
        file.write(b'Dummy FLV content for video ' + str(i).encode())
        
        # Add Timecode information
        timecode_info = b'Timecode information: 00:00:00:00'
        file.write(timecode_info)