import cv2
import numpy as np

# Define the resolutions to create video versions for
resolutions = [
    (1280, 720),  # HD
]

# Directory to save generated MP4 files
output_dir = "./tmp/"

def generate_complex_video(resolution):
    width, height = resolution
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 codec
    output_path = f"{output_dir}complex_video_{width}x{height}.mp4"
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (width, height))
    
    scenes = [
        {"duration": 60, "background": (0, 0, 255), "text": "Scene 1", "font_size": 1, "color": (255, 255, 0)},
        {"duration": 60, "background": (0, 255, 0), "text": "Scene 2", "font_size": 2, "color": (0, 0, 255)},
        {"duration": 60, "background": (255, 0, 0), "text": "Scene 3", "font_size": 3, "color": (0, 255, 255)}
    ]

    font = cv2.FONT_HERSHEY_SIMPLEX

    for scene in scenes:
        # Create frames for each scene
        for i in range(scene["duration"]):
            img = np.zeros((height, width, 3), np.uint8)
            img[:] = scene["background"]
            
            # Calculate text size, to position it in the center
            text_size = cv2.getTextSize(scene["text"], font, scene["font_size"], 2)[0]
            text_x = (width - text_size[0]) // 2
            text_y = (height + text_size[1]) // 2
            
            # Put the text on the image
            cv2.putText(img, scene["text"], (text_x, text_y), font, scene["font_size"], scene["color"], 2)
            
            # Apply a simple fade-in effect for the first frame of each scene
            if i == 0:
                for alpha in np.arange(0, 1.1, 0.1):
                    faded_img = cv2.addWeighted(img, alpha, np.zeros((height, width, 3), np.uint8), 1 - alpha, 0)
                    out.write(faded_img)
            else:
                out.write(img)
    
    out.release()  # Release the VideoWriter object

# Generate complex videos with different resolutions
for resolution in resolutions:
    generate_complex_video(resolution)  # Corrected variable name here

print("Complex Videos generated successfully.")