import subprocess
import os

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the filename of the output FLV file and the HLS directory
output_file = os.path.join(output_dir, 'enhanced_alpha_support_vp6_with_scaling_with_script_data_and_frame_skipping.flv')
hls_output_dir = os.path.join(output_dir, 'hls/')

# Sample command to generate a video with VP6 codec, alpha channel, On2 VP6 Scaling, Support for Script Data Objects, and Frame Skipping for Improved Performance, plus Adaptive Bitrate Streaming Compatibility.
ffmpeg_command = [
    'ffmpeg',
    '-i', 'input_with_alpha.mov',  # Input file
    '-vcodec', 'vp6a',  # VP6 codec with Alpha
    '-ar', '44100',  # Audio sample rate
    '-ab', '128k',  # Audio bit rate
    '-vf', 'scale=1280:720',  # On2 VP6 Scaling: scale the video to 1280x720 resolution
    '-r', '24',  # Frame rate adjustment for frame skipping effect (Optional, adjust based on source video frame rate)
    '-metadata', 'title="Enhanced Example Title"',  # Adding script data object - title
    '-metadata', 'comment="Enhanced Example Description"',  # Adding another script data object - description
    '-f', 'flv',  # Output format
    output_file  # Output file
]

# Execute the FFmpeg command to create the FLV file
try:
    subprocess.run(ffmpeg_command, check=True)
    print(f"File '{output_file}' has been created successfully with On2 VP6 Scaling, Support for Script Data Objects, and Frame Skipping for Improved Performance.")
except subprocess.CalledProcessError as e:
    print(f"Failed to create enhanced FLV file: {e}")

# Now, for Adaptive Bitrate Streaming Compatibility, we will convert the FLV file into an HLS (HTTP Live Streaming) format.
# This part of the code assumes you want to create multiple bitrate streams for adaptive streaming.
hls_command = [
    'ffmpeg',
    '-i', output_file,  # Input is the FLV file we just created
    '-profile:v', 'baseline',  # Baseline profile for compatibility
    '-level', '3.0',
    '-start_number', '0',  # HLS start number
    '-hls_time', '10',  # Segment length
    '-hls_list_size', '0',  # Maximum number of playlist entries (0 means no limit)
    '-f', 'hls',  # Output format HLS
    os.path.join(hls_output_dir, 'index.m3u8')  # HLS output directory and playlist file
]

# Ensure the HLS output directory exists
os.makedirs(hls_output_dir, exist_ok=True)

# Execute the FFmpeg command to create the HLS stream
try:
    subprocess.run(hls_command, check=True)
    print(f"HLS content has been created successfully in '{hls_output_dir}' for Adaptive Bitrate Streaming Compatibility.")
except subprocess.CalledProcessError as e:
    print(f"Failed to create HLS content for Adaptive Bitrate Streaming: {e}")