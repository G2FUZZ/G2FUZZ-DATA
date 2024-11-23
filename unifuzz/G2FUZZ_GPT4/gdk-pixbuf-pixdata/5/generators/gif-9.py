from PIL import Image, GifImagePlugin
import os

# Create the ./tmp/ directory if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the path for the new GIF file
output_path = os.path.join(output_dir, 'example_with_comment.gif')

# Create a simple GIF
# Here, we're creating a list of images (frames for the GIF)
frames = [Image.new('RGBA', (100, 100), (255, 0, 0, i)) for i in range(0, 255, 64)]

# Save the frames as a GIF
frames[0].save(
    output_path,
    save_all=True,
    append_images=frames[1:],
    duration=100,
    loop=0,
    comment=b'This is a comment block within the GIF.'
)

print(f"GIF saved to {output_path} with a comment block.")