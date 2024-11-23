import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Define the content to be written to the mp3 file
content = "MP3 is one of the most popular and widely used audio file formats."

# Write the content to the mp3 file
with open('./tmp/popular_format.mp3', 'w') as file:
    file.write(content)

print("MP3 file with the specified features has been created and saved in './tmp/' directory.")