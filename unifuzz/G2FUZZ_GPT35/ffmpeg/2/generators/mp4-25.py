import os
import ffmpeg

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample MP4 file with Closed captioning and High frame rate (HFR) video support features
file_path = './tmp/sample_with_closed_caption_and_hfr.mp4'

input_file = ffmpeg.input('input_video.mp4')
output_file = ffmpeg.output(input_file, './tmp/output_video.mp4', vf='subtitles=your_subtitle_file.srt', r=60)

try:
    ffmpeg.run(output_file, capture_stderr=True)
    print(f"MP4 file '{file_path}' with Closed captioning and High frame rate (HFR) video support features has been generated successfully.")
except ffmpeg.Error as e:
    print(f"An error occurred: {e.stderr}")