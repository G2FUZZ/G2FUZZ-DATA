import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Define the content of the 'ras' file
content = """6. Platform Independence: 'ras' files are platform-independent and can be viewed on different operating systems."""

# Save the content to the 'ras' file
filename = os.path.join(directory, 'platform_independence.ras')
with open(filename, 'w') as file:
    file.write(content)

print(f"File '{filename}' has been generated successfully.")