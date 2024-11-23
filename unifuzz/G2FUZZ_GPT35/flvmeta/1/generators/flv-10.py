import os

# Define the data to be included in the FLV file
custom_data = b'Custom data: FLV files can include custom data tags for specific applications or features.'

# Create a new FLV file with the custom data
file_path = './tmp/custom_data.flv'
with open(file_path, 'wb') as file:
    file.write(b'\x46\x4c\x56\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00')
    file.write(custom_data)

print(f'FLV file with custom data saved at: {file_path}')