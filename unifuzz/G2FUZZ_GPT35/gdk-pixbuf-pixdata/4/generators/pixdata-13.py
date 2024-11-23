import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate the content for the pixdata file
content = "13. Color profile: Information about the color characteristics of the image for accurate color reproduction."

# Save the content to a file
file_path = os.path.join(directory, 'pixdata.txt')
with open(file_path, 'w') as file:
    file.write(content)

print(f"File 'pixdata.txt' containing the feature has been saved in the './tmp/' directory.")