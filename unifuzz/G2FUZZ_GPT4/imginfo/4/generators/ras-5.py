import os

# Create tmp directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Define the content for the RAS file
content = '''5. **Portability**: Designed on Sun Microsystems' workstations, the format is well-supported across different platforms, ensuring that the files can be opened and edited on various operating systems without significant compatibility issues.
'''

# Define the filename
filename = 'feature.ras'

# Full path for the file
full_path = os.path.join('./tmp', filename)

# Write the content to the RAS file
with open(full_path, 'w') as file:
    file.write(content)

print(f'File "{filename}" has been created in "./tmp/".')