import cv2

# Define the video codec mappings
codec_mappings = {
    'H264': cv2.VideoWriter_fourcc(*'H264'),
    'HEVC': cv2.VideoWriter_fourcc(*'HEVC'),
    'MPEG4': cv2.VideoWriter_fourcc(*'XVID')
}
fps = 30
frame_width = 640
frame_height = 480

for codec in codec_mappings:
    out = cv2.VideoWriter(f'./tmp/video_{codec}.mp4', codec_mappings[codec], fps, (frame_width, frame_height))

    # Generate a sample video
    for i in range(100):
        frame = cv2.randn((frame_height, frame_width, 3), 0, 255)
        frame = cv2.convertScaleAbs(frame)  # Convert frame to CV_8U depth
        out.write(frame)

    out.release()