import os
import datetime

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate FLV file with additional complex features
metadata = {
    'title': 'Advanced FLV Video',
    'author': 'John Doe',
    'creation_date': str(datetime.datetime.now())
}

feature = f"Metadata:\nTitle: {metadata['title']}\nAuthor: {metadata['author']}\nCreation Date: {metadata['creation_date']}\n\n" \
          "Advanced Features:\nReal-time Streaming: FLV files support real-time streaming of audio and video content, allowing for seamless playback over the internet.\n" \
          "Customizable Skins: FLV files can be embedded with customizable video player skins to enhance the viewing experience."

file_path = os.path.join(directory, 'generated_advanced_flv_file.flv')

with open(file_path, 'w') as file:
    for key, value in metadata.items():
        file.write(f"{key}: {value}\n")
    file.write("\n")
    file.write(feature)

print(f"FLV file with advanced features including metadata and real-time streaming has been generated and saved at: {file_path}")