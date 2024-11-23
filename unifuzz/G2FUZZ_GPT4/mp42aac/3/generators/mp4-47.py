import cv2
import numpy as np
import os
import subprocess

# Ensure the ./tmp/ directory exists
output_directory = './tmp/'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Define the filenames for intermediate and final output video files
output_filename_main_video = output_directory + 'main_video.mp4'
output_filename_pip_video = output_directory + 'pip_video.mp4'
output_filename_audio_original = output_directory + 'audio_original.m4a'
output_filename_audio_commentary = output_directory + 'audio_commentary.m4a'
output_filename_audio_music = output_directory + 'audio_music.m4a'
output_filename_subtitles = output_directory + 'subtitles.srt'
output_filename_final_complex = output_directory + 'final_complex_structure.mp4'

# Properties for the main video
frame_width_main = 1920
frame_height_main = 1080
fps_main = 24  # Frames per second

# Properties for the PiP video
frame_width_pip = 480
frame_height_pip = 270  # Smaller than the main video
fps_pip = 24

# Duration of the videos in seconds
duration_sec = 10

# Create the main video with changing colors
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4V codec
out_main = cv2.VideoWriter(output_filename_main_video, fourcc, fps_main, (frame_width_main, frame_height_main))

for i in range(fps_main * duration_sec):
    frame = np.zeros((frame_height_main, frame_width_main, 3), dtype=np.uint8)
    color_intensity = (i * 255 // (fps_main * duration_sec))
    frame[:, :] = [color_intensity % 255, color_intensity % 255, color_intensity % 255]
    out_main.write(frame)
out_main.release()

# Create the PiP video with a constant color
out_pip = cv2.VideoWriter(output_filename_pip_video, fourcc, fps_pip, (frame_width_pip, frame_height_pip))
pip_color = np.array([0, 255, 0], dtype=np.uint8)  # Green
pip_frame = np.zeros((frame_height_pip, frame_width_pip, 3), dtype=np.uint8)
pip_frame[:, :] = pip_color
for _ in range(fps_pip * duration_sec):
    out_pip.write(pip_frame)
out_pip.release()

# Generate silent lossless audio files for original, commentary, and music tracks
subprocess.run(['ffmpeg', '-y', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-c:a', 'alac', '-t', str(duration_sec), output_filename_audio_original])
subprocess.run(['ffmpeg', '-y', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-c:a', 'alac', '-t', str(duration_sec), output_filename_audio_commentary])
subprocess.run(['ffmpeg', '-y', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-c:a', 'alac', '-t', str(duration_sec), output_filename_audio_music])

# Create subtitles file
with open(output_filename_subtitles, "w") as f:
    f.write("1\n")
    f.write("00:00:01,000 --> 00:00:02,000\n")
    f.write("Example Subtitle 1\n\n")
    f.write("2\n")
    f.write("00:00:03,000 --> 00:00:04,000\n")
    f.write("Example Subtitle 2\n")

# Combine everything into the final complex file
subprocess.run([
    'ffmpeg', '-y',
    '-i', output_filename_main_video,
    '-i', output_filename_pip_video,
    '-i', output_filename_audio_original,
    '-i', output_filename_audio_commentary,
    '-i', output_filename_audio_music,
    '-filter_complex', f"[1]scale={frame_width_pip}:{frame_height_pip} [pip]; [0][pip] overlay=main_w-overlay_w-10:10",  # PiP overlay
    '-map', '0:v', '-map', '2:a', '-map', '3:a', '-map', '4:a',  # Select video and audio tracks
    '-c:v', 'copy',
    '-c:a', 'copy',
    '-metadata:s:a:0', 'language=eng',
    '-metadata:s:a:1', 'language=eng',
    '-metadata:s:a:2', 'language=eng',
    '-disposition:a:1', 'commentary',
    '-disposition:a:2', 'secondary',
    '-scodec', 'mov_text',
    '-metadata:s:s:0', 'language=eng',
    '-f', 'mp4',
    output_filename_final_complex
])

# Cleanup temporary files
os.remove(output_filename_main_video)
os.remove(output_filename_pip_video)
os.remove(output_filename_audio_original)
os.remove(output_filename_audio_commentary)
os.remove(output_filename_audio_music)

print(f'Complex MP4 file with multiple video tracks, audio tracks, and subtitles has been saved to {output_filename_final_complex}')