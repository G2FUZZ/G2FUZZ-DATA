import os
import moviepy.editor as mp

# Create a sample video clip with a red background color for 10 seconds
clip = mp.ColorClip(size=(1920, 1080), color=(255, 0, 0), duration=10)  
clip.fps = 24  # Set the frames per second

# Define the output file path
output_dir = './tmp/'
output_file = os.path.join(output_dir, 'sample_video.mp4')

# Write the video clip to a file with H.264 codec
clip.write_videofile(output_file, codec='libx264')

print(f"Video file saved at: {output_file}")