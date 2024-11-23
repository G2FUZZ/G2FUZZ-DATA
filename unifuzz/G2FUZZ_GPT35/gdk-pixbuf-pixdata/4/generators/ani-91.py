import os

# Define the 'ani' file content with additional data for each file
ani_content_1 = b'\x00\x00\x01\x00\x02\x00\x10\x00\x10\x00\x00\x00\x00\x00\x00\x00'
ani_content_2 = b'\x01\x01\x02\x02\x03\x03\x04\x04\x05\x05\x06\x06\x07\x07\x08\x08'
ani_content_3 = b'\x0A\x0A\x0B\x0B\x0C\x0C\x0D\x0D\x0E\x0E\x0F\x0F\x10\x10\x11\x11'

# Create the 'ani' files with additional data
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

ani_contents = [ani_content_1, ani_content_2, ani_content_3]

for i, content in enumerate(ani_contents):
    file_path = f'./tmp/ani_file_{i}.ani'
    with open(file_path, 'wb') as file:
        file.write(content)

print("Generated 'ani' files with more complex file structures successfully.")