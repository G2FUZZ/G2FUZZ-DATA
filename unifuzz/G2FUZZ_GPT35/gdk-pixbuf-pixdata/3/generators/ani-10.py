import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate 'ani' file with platform compatibility feature
file_content = "Platform Compatibility: 'ani' files can be designed for specific platforms or have cross-platform support."

# Save the generated file
file_path = './tmp/ani_file.ani'
with open(file_path, 'w') as file:
    file.write(file_content)

print(f"File saved at: {file_path}")