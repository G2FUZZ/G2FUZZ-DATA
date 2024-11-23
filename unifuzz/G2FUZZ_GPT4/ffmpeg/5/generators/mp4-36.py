import os
from moviepy.editor import ColorClip, concatenate_videoclips
from moviepy.video.fx.all import fadein, fadeout

# Ensure the tmp directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a simple video clip
clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=10)  # A red video of 10 seconds

# Apply fade-in and fade-out effects
clip = fadein(clip, 1)  # 1-second fade-in
clip = fadeout(clip, 1)  # 1-second fade-out

# Loop the clip
num_loops = 3  # Number of times to loop
looped_clip = concatenate_videoclips([clip] * num_loops)

# Metadata
metadata = {
    'title': 'Sample Video',
    'artist': 'Pythonista',
    'album': 'Python Generated',
    'comments': 'This is a sample video clip with metadata, generated using MoviePy.'
}

# Set metadata (MoviePy does not directly support setting arbitrary metadata, workaround by saving as a temporary file and using ffmpeg)
temp_video_path = os.path.join(output_dir, 'temp_video.mp4')
final_video_path = os.path.join(output_dir, 'final_video_with_metadata.mp4')  # Corrected the final_video_path

# Specify the fps directly in the write_videofile function
looped_clip.write_videofile(temp_video_path, fps=24)  # Assuming 24 fps for this example

# Use ffmpeg to add metadata and specify a different codec for demonstration of codec independence
# Here, using libx265 as an example for video codec to demonstrate codec independence
cmd = f"ffmpeg -i {temp_video_path} -metadata title=\"{metadata['title']}\" -metadata artist=\"{metadata['artist']}\" -metadata album=\"{metadata['album']}\" -metadata comment=\"{metadata['comments']}\" -c:v libx265 -crf 28 -c:a aac -b:a 128k {final_video_path}"

os.system(cmd)

# Cleanup the temporary file
os.remove(temp_video_path)