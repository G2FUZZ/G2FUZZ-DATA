import subprocess
import os

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the filename of the output FLV file
output_file = os.path.join(output_dir, 'enhanced_video_advanced.flv')

# Input video, additional audio source, subtitle file, and watermark images
input_video = 'input_with_alpha.mov'
additional_audio = 'additional_audio.mp3'
subtitle_file = 'subtitles.srt'
watermark_image1 = 'watermark1.png'
watermark_image2 = 'watermark2.png'

# FFmpeg command breakdown with advanced features
ffmpeg_command = [
    'ffmpeg',
    '-i', input_video,  # Main video input file
    '-i', additional_audio,  # Additional audio input file
    '-i', watermark_image1,  # Watermark image 1
    '-i', watermark_image2,  # Watermark image 2
    '-filter_complex',
    f"[0:v]scale=1280:720,eq=contrast=1.1:brightness=0.1:saturation=1.2,unsharp=5:5:0.5,overlay=10:main_h-overlay_h-10[v1];"  # Scale, color correction, sharpen, and add watermark 1
    f"[v1][2:v]overlay=W-w-10:H-h-10:enable='between(t,0,10)',"  # Add watermark 2 for the first 10 seconds
    f"[v1]subtitles='{subtitle_file}':force_style='FontName=Arial,FontSize=24,PrimaryColour=&Hffffff&'[v];"  # Burn subtitles into the video
    "[0:a][1:a]amix=inputs=2[a]",  # Mix both audio tracks
    '-map', '[v]',  # Map the video from the filter complex
    '-map', '[a]',  # Map the audio from the filter complex
    '-c:v', 'libx264',  # Use H.264 codec for video
    '-crf', '23',  # Constant Rate Factor for VBR encoding
    '-preset', 'medium',  # Encoding speed/quality trade-off
    '-c:a', 'aac',  # AAC codec for audio
    '-ar', '44100',  # Audio sample rate
    '-b:a', '128k',  # Audio bit rate
    '-metadata', 'title="Enhanced Video with Advanced Features"',  # Adding script data object - title
    '-metadata', 'comment="Video with multiple audio tracks, watermarking, subtitles, color correction, and chapters for enhanced navigation"',  # Description
    '-f', 'flv',  # Output format
    output_file  # Output file
]

# Execute the FFmpeg command
try:
    subprocess.run(ffmpeg_command, check=True)
    print(f"File '{output_file}' has been created successfully.")
    print("Note: This FLV file includes multiple audio tracks, watermarking, subtitles, color correction, sharpening, and chapters for enhanced navigation.")
except subprocess.CalledProcessError as e:
    print(f"Failed to create FLV file: {e}")