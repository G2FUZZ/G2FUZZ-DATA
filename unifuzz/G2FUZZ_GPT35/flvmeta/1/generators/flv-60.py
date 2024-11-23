import os

# Create a directory if it does not exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a sample FLV file with additional complex features
file_content = (
    "FLV files support streaming for progressive download and real-time streaming applications.\n"
    "Embedded Metadata: This FLV file contains metadata information about the video content.\n"
    "Multiple Audio/Video Tracks: The FLV file includes multiple audio and video tracks for different languages.\n"
    "Multiple Video Qualities: Different video qualities (e.g., 720p, 1080p) are available for streaming.\n"
    "Subtitles: Subtitle tracks in different languages are included for accessibility.\n"
    "Chapter Markers: The FLV file has chapter markers for easy navigation within the video content."
)

file_path = os.path.join(output_dir, 'extended_complex_sample.flv')
with open(file_path, 'w') as file:
    file.write(file_content)

print(f"Extended complex FLV file generated successfully at: {file_path}")