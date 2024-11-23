import numpy as np
import cv2
import json  # Import the json module

# Generate a random video frame
frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'FLV1')  # H.263 codec
out = cv2.VideoWriter('./tmp/generated_video_with_cue_points.flv', fourcc, 30, (640, 480))

# Write frame to the video
for _ in range(100):
    out.write(frame)

# Release the VideoWriter
out.release()

# Add Cue Points to the FLV file
cue_points = {
    "cuePoint1": {
        "time": 5,  # Cue point at 5 seconds
        "frameLabel": "Event1"
    },
    "cuePoint2": {
        "time": 15,  # Cue point at 15 seconds
        "frameLabel": "Event2"
    }
}

# Save the cue points information to a file
with open('./tmp/cue_points.json', 'w') as f:
    json.dump(cue_points, f)