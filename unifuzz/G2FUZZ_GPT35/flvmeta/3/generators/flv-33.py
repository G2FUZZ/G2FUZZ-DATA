import os

# Define the content of the complex FLV file
flv_content = """
FLV File Format:
- Streaming Capabilities: FLV files support streaming, enabling users to watch videos as they download without waiting for the entire file to be downloaded.
- Video Segments:
    Segment 1: Introduction
    Segment 2: Main Content
    Segment 3: Conclusion
- Metadata:
    Title: Sample FLV File
    Author: John Doe
    Description: This is a sample FLV file with complex file structure.
"""

# Create a directory to store the FLV files
os.makedirs('./tmp/', exist_ok=True)

# Save the content to a complex FLV file
with open('./tmp/complex_flv_file.flv', 'w') as file:
    file.write(flv_content)

print("Complex FLV file generated successfully.")