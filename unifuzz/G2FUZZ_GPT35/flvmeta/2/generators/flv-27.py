import numpy as np
import cv2
import json  # Import the json module

# Generate a random video frame
frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'FLV1')  # H.263 codec
out = cv2.VideoWriter('./tmp/generated_video_with_error_handling.flv', fourcc, 30, (640, 480))

# Write frame to the video
try:
    for _ in range(100):
        out.write(frame)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    out.release()

# Add Cue Points and Chapter Markers to the FLV file
metadata = {
    "cuePoints": {
        "cuePoint1": {
            "time": 5,  # Cue point at 5 seconds
            "frameLabel": "Event1"
        },
        "cuePoint2": {
            "time": 15,  # Cue point at 15 seconds
            "frameLabel": "Event2"
        }
    },
    "chapterMarkers": {
        "chapterMarker1": {
            "time": 10,  # Chapter marker at 10 seconds
            "title": "Chapter 1"
        },
        "chapterMarker2": {
            "time": 20,  # Chapter marker at 20 seconds
            "title": "Chapter 2"
        }
    }
}

# Save the metadata information to a file
with open('./tmp/metadata.json', 'w') as f:
    json.dump(metadata, f)