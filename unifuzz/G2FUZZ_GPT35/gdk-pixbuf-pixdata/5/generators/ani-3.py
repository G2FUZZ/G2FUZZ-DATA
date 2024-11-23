import os

# Define the content of the 'ani' file with the specified feature
ani_content = """
Resolution Independence: Yes
Allow Various Screen Sizes: Yes
Quality Loss: None
"""

# Create a directory to save the 'ani' files if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Save the generated 'ani' file with the specified content
file_path = './tmp/ani_file.ani'
with open(file_path, 'w') as f:
    f.write(ani_content)

print(f"Generated 'ani' file saved at: {file_path}")