import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample MP4 file with Extended file compatibility feature
file_path = './tmp/sample_extended.mp4'
with open(file_path, 'wb') as f:
    f.write(b'Extended file compatibility: MP4 files are widely supported across various platforms, devices, and media players, making them a versatile choice for multimedia content distribution.')

print(f"MP4 file '{file_path}' with Extended file compatibility feature has been generated successfully.")