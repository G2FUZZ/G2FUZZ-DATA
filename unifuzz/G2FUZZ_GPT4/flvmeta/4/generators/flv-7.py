import ffmpeg
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the output file path
output_file = os.path.join(output_dir, 'example.flv')

# Generate a simple FLV file
# This command generates a 5-second video file with a resolution of 640x360.
# The video will be blank (color black) as it's generated from an artificial color input.
try:
    (
        ffmpeg
        .input('color=c=black:s=640x360:d=5', f='lavfi')
        .output(output_file, vcodec='flv', format='flv')
        .run()
    )
    print(f"FLV file created at: {output_file}")
except ffmpeg.Error as e:
    print(f"An error occurred: {e.stderr}")