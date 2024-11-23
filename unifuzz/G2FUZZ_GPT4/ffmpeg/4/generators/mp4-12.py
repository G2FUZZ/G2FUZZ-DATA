import cv2
import numpy as np

# Set parameters for the video
width, height = 640, 360
fps = 24
duration = 5  # seconds
background_color = (255, 255, 255)

# Text settings for compatibility feature
compatibility_text = "10. **Compatibility**: They are widely compatible with media players, web browsers, and devices, making them a universal format for distributing and accessing multimedia content."
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.5
font_color = (0, 0, 0)
font_thickness = 2

# Text settings for multi-track audio feature
multi_track_audio_text = "5. **Multi-track Audio**: They can include multiple audio tracks in different languages or with different audio qualities, giving users options for playback."
# Calculate text size to center the multi-track audio text
text_size_audio = cv2.getTextSize(multi_track_audio_text, font, font_scale, font_thickness)[0]
text_x_audio = (width - text_size_audio[0]) // 2
text_y_audio = height // 3  # Position the audio feature text in the upper third

# Calculate text size to center the compatibility text
text_size_compatibility = cv2.getTextSize(compatibility_text, font, font_scale, font_thickness)[0]
text_x_compatibility = (width - text_size_compatibility[0]) // 2
text_y_compatibility = (height * 2) // 3  # Position the compatibility feature text in the lower third

# Create a blank image/frame
frame = np.full((height, width, 3), background_color, np.uint8)

# Put the multi-track audio text onto the frame
cv2.putText(frame, multi_track_audio_text, (text_x_audio, text_y_audio), font, font_scale, font_color, font_thickness, cv2.LINE_AA)

# Put the compatibility text onto the frame
cv2.putText(frame, compatibility_text, (text_x_compatibility, text_y_compatibility), font, font_scale, font_color, font_thickness, cv2.LINE_AA)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec used to compress the frames
output_path = './tmp/features.mp4'
video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Write the same frame for the entire duration of the video
for _ in range(fps * duration):
    video.write(frame)

# Release everything when job is finished
video.release()
cv2.destroyAllWindows()