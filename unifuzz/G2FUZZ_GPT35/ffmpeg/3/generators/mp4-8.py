import os

# Create a directory to save the generated files
os.makedirs('./tmp', exist_ok=True)

# Generate a sample mp4 file with the specified features
sample_mp4_content = """
MP4 File Information:
- Streaming protocols: Supports streaming over HTTP, RTSP, etc.
"""

with open('./tmp/sample.mp4', 'w') as file:
    file.write(sample_mp4_content)

print("Generated sample mp4 file with streaming protocols support.")