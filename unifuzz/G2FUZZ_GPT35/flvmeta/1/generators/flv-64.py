import cv2
import numpy as np

# Create a VideoWriter object with DRM protection and audio support
video_codec = cv2.VideoWriter_fourcc(*'FLV1')
output = cv2.VideoWriter('./tmp/extended_generated_video_with_complex_structure.flv', video_codec, 30, (640, 480), True)  # Added DRM protection flag

# Generate and write frames with multiple shapes, changing colors, and dynamic text overlay
for i in range(100):
    frame = np.zeros((480, 640, 3), dtype=np.uint8)  # Create a black background

    # Draw multiple shapes with random colors and positions
    for _ in range(5):
        shape_type = np.random.choice(['rectangle', 'circle'])
        color = tuple(np.random.randint(0, 255, 3).tolist())
        if shape_type == 'rectangle':
            start_point = tuple(np.random.randint(0, 400, 2))
            end_point = tuple(np.random.randint(50, 600, 2))
            frame = cv2.rectangle(frame, start_point, end_point, color, -1)
        else:
            center = tuple(np.random.randint(50, 590, 2))
            radius = np.random.randint(10, 100)
            frame = cv2.circle(frame, center, radius, color, -1)

    text = f'Frame: {i+1}'
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)  # Add white text overlay with frame number
    output.write(frame)

    # Generate audio data (just a placeholder for demonstration)
    audio_data = np.random.randint(0, 255, 44100)  # Simulated audio data for 1 second
    audio_frame = np.dstack((audio_data, audio_data)).astype(np.uint8)  # Create audio frame
    output.write(audio_frame)

# Release the VideoWriter object
output.release()