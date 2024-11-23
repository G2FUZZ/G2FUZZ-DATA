import os
import random
import time

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Define the content for the FLV files with ActionScript code
def generate_flv_content(file_num):
    metadata = {
        'title': f'Title of File {file_num}',
        'author': 'John Doe',
        'description': 'This is a sample FLV file with extended metadata.',
        'duration': random.randint(60, 600),
        'resolution': '1280x720',
        'bitrate': '2500 kbps',
        'framerate': '30 fps',
        'creation_date': time.strftime('%Y-%m-%d'),
        'tags': ['FLV', 'Metadata', 'ActionScript'],
        'custom_data': {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3'
        }
    }

    flv_content = f"""
    FLV File Format
    File Number: {file_num}
    Title: {metadata['title']}
    Author: {metadata['author']}
    Description: {metadata['description']}
    Duration: {metadata['duration']} seconds
    Resolution: {metadata['resolution']}
    Bitrate: {metadata['bitrate']}
    Framerate: {metadata['framerate']}
    Creation Date: {metadata['creation_date']}
    Tags: {', '.join(metadata['tags'])}
    Custom Data:
    {metadata['custom_data']}
    
    Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}
    """
    return flv_content

# Generate FLV files with the specified features and metadata
for i in range(5):
    file_name = f'./tmp/file_{i+1}.flv'
    with open(file_name, 'w') as f:
        f.write(generate_flv_content(i+1))

print('FLV files with extended metadata generated successfully.')