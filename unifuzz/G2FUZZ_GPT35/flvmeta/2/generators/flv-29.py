import numpy as np
import cv2
import json

# Generate a random video frame
frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'FLV1')
out = cv2.VideoWriter('./tmp/generated_video_with_thumbnails.flv', fourcc, 30, (640, 480))

# Write frame to the video
for _ in range(100):
    out.write(frame)

# Release the VideoWriter
out.release()

# Add Cue Points, Chapter Markers, and Thumbnail Generation metadata to the FLV file
metadata = {
    "cuePoints": {
        "cuePoint1": {
            "time": 5,
            "frameLabel": "Event1"
        },
        "cuePoint2": {
            "time": 15,
            "frameLabel": "Event2"
        }
    },
    "chapterMarkers": {
        "chapterMarker1": {
            "time": 10,
            "title": "Chapter 1"
        },
        "chapterMarker2": {
            "time": 20,
            "title": "Chapter 2"
        }
    },
    "thumbnails": {
        "thumbnail1": {
            "time": 3,  # Time in seconds for the thumbnail
            "imagePath": "./tmp/thumbnail_image.jpg"
        },
        "thumbnail2": {
            "time": 12,
            "imagePath": "./tmp/thumbnail_image.jpg"
        }
    }
}

# Save the metadata information to a file
with open('./tmp/metadata_with_thumbnails.json', 'w') as f:
    json.dump(metadata, f)