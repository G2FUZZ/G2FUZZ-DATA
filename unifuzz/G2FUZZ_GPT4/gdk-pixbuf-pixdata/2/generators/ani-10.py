from PIL import Image, ImageDraw
import os

def create_frame(index, size=(32, 32), color="black"):
    """
    Create an individual frame for the animation.
    """
    image = Image.new("RGBA", size, "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle([index, index, index + 10, index + 10], fill=color)
    return image

def save_ani_frames(frames, directory="./tmp/", basename="frame"):
    """
    Save frames to the specified directory.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    frame_filenames = []
    for i, frame in enumerate(frames):
        frame_filename = f"{basename}_{i}.ico"
        frame_path = os.path.join(directory, frame_filename)
        frame.save(frame_path, format="ICO", sizes=[(32, 32)])
        frame_filenames.append(frame_filename)
    return frame_filenames

def create_ani_file(frame_filenames, ani_filename="animation.ani", rate=100):
    """
    Create a basic .ani file with the given frames and rate.
    This function simplifies the .ani file structure for demonstration.
    """
    header = "RIFFxxxxACONanih36\x00\x00\x00\x24\x00\x00\x00\x02\x00\x00\x00"
    header += f"{rate}\x00\x00\x00{len(frame_filenames)}\x00\x00\x00{len(frame_filenames)}\x00\x00\x00"
    
    list_section = "LISTxxxxfram"
    for filename in frame_filenames:
        with open(f"./tmp/{filename}", "rb") as f:
            content = f.read()
            list_section += f"icon{content}"
    
    # Simplified example; real .ani files would need more accurate headers and data
    with open(f"./tmp/{ani_filename}", "wb") as f:
        f.write(header.encode("latin-1") + list_section.encode("latin-1"))

def main():
    # Create frames of a simple moving square
    frames = [create_frame(i) for i in range(10)]
    
    # Save frames as .ico files
    frame_filenames = save_ani_frames(frames)
    
    # Create a basic .ani file from these frames
    create_ani_file(frame_filenames)

if __name__ == "__main__":
    main()