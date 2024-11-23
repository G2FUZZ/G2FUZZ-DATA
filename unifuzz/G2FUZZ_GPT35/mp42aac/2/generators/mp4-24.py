import moviepy.editor as mp

# Create a color clip with a duration of 5 seconds and a resolution of 640x480 with green color
clip = mp.ColorClip(size=(640, 480), color=(0, 255, 0), duration=5)
clip.fps = 30  # Set the frames per second (fps) for the video clip

# Set the video codec to H.264
clip.write_videofile("./tmp/example_video_H264.mp4", codec="libx264")

# Set the video codec to H.265
clip.write_videofile("./tmp/example_video_H265.mp4", codec="libx265")

# Adding the Editable feature to the video clip
editable_feature = "Editable: can be edited using various video editing software"
with open("./tmp/example_video_with_editable_feature.txt", "w") as file:
    file.write(editable_feature)

# Adding the Timed text feature to the video clip
timed_text_feature = "Timed text: support for timed text tracks for closed captioning or subtitles"
with open("./tmp/example_video_with_timed_text_feature.txt", "w") as file:
    file.write(timed_text_feature)

# Adding the High dynamic range (HDR) support feature to the video clip
hdr_support_feature = "High dynamic range (HDR) support: ability to store HDR video content"
with open("./tmp/example_video_with_hdr_support_feature.txt", "w") as file:
    file.write(hdr_support_feature)