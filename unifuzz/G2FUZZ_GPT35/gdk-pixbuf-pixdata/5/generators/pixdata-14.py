import os

# Create the directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Generate the 'pixdata' file with the specified feature
data = "Embedded resources: Other data or files included within the 'pixdata' file."
file_path = './tmp/pixdata.txt'

with open(file_path, 'w') as file:
    file.write(data)

print(f"File saved at: {file_path}")