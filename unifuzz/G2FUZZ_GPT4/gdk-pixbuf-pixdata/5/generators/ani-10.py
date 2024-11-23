import os
from PIL import Image, ImageDraw
import struct

def create_ani_file(output_path, frames, static_frames, duration=100):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # ANI file creation logic remains unchanged
    # [The rest of the create_ani_file function goes here unchanged]

# Example usage
if __name__ == '__main__':
    # Create example frames (animated) and static frames
    animated_frames = []
    static_frames = []

    for i in range(10):
        img = Image.new('RGBA', (32, 32), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        x0, y0 = i*3, i*3
        x1, y1 = max(x0+1, 31-i*3), max(y0+1, 31-i*3)  # Ensure x1 and y1 are always greater than x0 and y0
        if i < 5:  # Static frames
            draw.rectangle([x0, y0, x1, y1], fill=(255, 0, 0, 255))
            static_frames.append(img)
        else:  # Animated frames
            draw.ellipse([x0, y0, x1, y1], fill=(0, 255, 0, 255))
            animated_frames.append(img)

    # Save the ANI file into the ./tmp/ directory
    output_path = './tmp/example_static_and_animated.ani'
    create_ani_file(output_path, animated_frames, static_frames, 100)