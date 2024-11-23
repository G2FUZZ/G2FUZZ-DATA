import cv2
import numpy as np
import os

# Define the path for saving the video
save_path = './tmp/'
if not os.path.exists(save_path):
    os.makedirs(save_path)

# Video configuration
fps = 24
duration_sec = 10
total_frames = duration_sec * fps
frame_size = (640, 480)

# Initialize the Video Writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(f'{save_path}video_with_chapters.mp4', fourcc, fps, frame_size)

# Create a dummy video with text for different chapters
chapters = {
    1: 'Introduction',
    int(total_frames * 0.25): 'Chapter 1',
    int(total_frames * 0.5): 'Chapter 2',
    int(total_frames * 0.75): 'Chapter 3',
    total_frames - 1: 'Conclusion'
}

for frame_number in range(total_frames):
    # Create a black image
    img = np.zeros((frame_size[1], frame_size[0], 3), np.uint8)
    
    # Determine chapter marker
    text = 'Video Content'
    for chapter_frame, chapter_title in chapters.items():
        if frame_number >= chapter_frame:
            text = chapter_title
    
    # Put chapter title on the frame
    cv2.putText(img, text, (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
    # Write the frame into the file
    out.write(img)

# Release the VideoWriter
out.release()

# FFmpeg is required to insert chapter markers and add lossless audio
# This part of the code assumes FFmpeg is installed and available in the system path
chapter_file_content = ";FFMETADATA1\n"
for frame_number, chapter_title in chapters.items():
    start_time = frame_number / fps
    chapter_file_content += f"[CHAPTER]\nTIMEBASE=1/1\nSTART={int(start_time)}\nEND={int(start_time + duration_sec / len(chapters))}\ntitle={chapter_title}\n"

metadata_file_path = f'{save_path}metadata.txt'
with open(metadata_file_path, 'w') as f:
    f.write(chapter_file_content)

# Generating a silent lossless audio track of the same duration as the video
# Using FLAC as an example of a lossless codec
audio_file_path = f'{save_path}silent_audio.flac'
os.system(f'ffmpeg -f lavfi -i anullsrc=r=44100:cl=stereo -t {duration_sec} -acodec flac {audio_file_path}')

# Use FFmpeg to add chapters and the lossless audio to the video file
input_video_path = f'{save_path}video_with_chapters.mp4'
output_video_path = f'{save_path}final_video_with_chapters_and_lossless_audio.mp4'
os.system(f'ffmpeg -i {input_video_path} -i {audio_file_path} -i {metadata_file_path} -map_metadata 2 -map 0:v -map 1:a -c:v copy -c:a copy {output_video_path}')

# Clean up by removing the temporary files
os.remove(input_video_path)
os.remove(metadata_file_path)
os.remove(audio_file_path)