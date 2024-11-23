from PIL import Image
import os

def create_frame(color, size=(32, 32)):
    """
    Create a single frame with the specified color and size.
    """
    image = Image.new("RGBA", size, color)
    return image

def save_ani(frames, filename, frame_rate=60):
    """
    Save a sequence of frames as an .ani file.
    
    This function is a simplified representation. The .ani format is more complex and requires specific headers
    and structures. For a fully functional .ani file, additional RIFF headers and chunks need to be written.
    """
    # Ensure the tmp directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # ANI files require a specific header and structure. This example does not fully implement the .ani specification.
    # Instead, we'll save each frame as a separate file for demonstration purposes.
    for i, frame in enumerate(frames):
        frame_filename = f"{filename}_{i}.png"
        frame.save(frame_filename)

# Example usage
if __name__ == "__main__":
    # Generate a sequence of frames with different colors
    colors = [("red"), ("green"), ("blue"), ("yellow")]
    frames = [create_frame(color) for color in colors]

    # Save the sequence as an .ani file (demonstration purposes only)
    save_ani(frames, "./tmp/animation.ani")