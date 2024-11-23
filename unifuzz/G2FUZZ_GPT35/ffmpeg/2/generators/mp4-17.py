import os
import ffmpeg

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample MP4 file with Closed captioning feature
file_path = './tmp/sample_with_closed_caption.mp4'

input_file = ffmpeg.input('input_video.mp4')
output_file = ffmpeg.output(input_file, './tmp/output_video.mp4', vf='subtitles=your_subtitle_file.srt')

try:
    ffmpeg.run(output_file, capture_stderr=True)
    print(f"MP4 file '{file_path}' with Closed captioning feature has been generated successfully.")
except ffmpeg.Error as e:
    print(f"An error occurred: {e.stderr}")