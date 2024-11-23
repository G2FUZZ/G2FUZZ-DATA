import os

# Define the 'ani' file content
ani_content = b'\x00\x00\x01\x00\x02\x00\x10\x00\x10\x00\x00\x00\x00\x00\x00\x00'

# Create the 'ani' files
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

for i in range(3):
    file_path = f'./tmp/ani_file_{i}.ani'
    with open(file_path, 'wb') as file:
        file.write(ani_content)

print("Generated 'ani' files successfully.")