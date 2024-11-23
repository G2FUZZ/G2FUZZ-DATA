from PIL import Image, ImageDraw
import os

def create_transparent_frame(size, color, transparency, filename):
    """
    Create a single frame with transparency and save it as PNG.
    """
    image = Image.new("RGBA", size, color=(0, 0, 0, 0))  # Create transparent image
    draw = ImageDraw.Draw(image)
    draw.ellipse((0, 0, size[0]-1, size[1]-1), fill=color + (transparency,))
    image.save(filename, "PNG")

def convert_png_to_ico(png_file, ico_file):
    """
    Convert PNG to ICO format.
    """
    image = Image.open(png_file)
    image.save(ico_file, format='ICO', sizes=[(256, 256)])

def create_ani_file(frames, ani_file_path):
    """
    Assemble the ANI file. This is a placeholder function to demonstrate the concept.
    Actual implementation would require writing the RIFF structure for ANI files.
    """
    print(f"Creating ANI file with {len(frames)} frames: {ani_file_path}")
    # Here you would implement the logic to create an ANI file using the frames.
    # This example does not implement the full ANI file creation due to its complexity and scope.

def main():
    tmp_dir = "./tmp/"
    os.makedirs(tmp_dir, exist_ok=True)
    
    # Parameters for the frame
    size = (64, 64)
    color = (255, 0, 0)  # Red
    transparency = 128  # Semi-transparent
    
    frame_filenames = []
    for i in range(4):  # Create 4 frames
        png_filename = os.path.join(tmp_dir, f"frame_{i}.png")
        ico_filename = os.path.join(tmp_dir, f"frame_{i}.ico")
        create_transparent_frame(size, color, transparency, png_filename)
        convert_png_to_ico(png_filename, ico_filename)
        frame_filenames.append(ico_filename)
    
    ani_file_path = os.path.join(tmp_dir, "animated_cursor.ani")
    create_ani_file(frame_filenames, ani_file_path)

if __name__ == "__main__":
    main()