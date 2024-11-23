import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a random file size
file_size = 1024 * 1024  # 1MB file size

# Save the generated file with the specified features
with open('./tmp/image.ras', 'w') as f:
    f.write(f"File Size: {file_size} bytes\n")