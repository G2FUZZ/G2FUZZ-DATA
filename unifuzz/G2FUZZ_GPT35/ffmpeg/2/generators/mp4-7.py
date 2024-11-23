import imageio

# Create a dummy image for the video
image = imageio.imread("imageio:chelsea.png")

# Create a video writer object
writer = imageio.get_writer("./tmp/fast_start.mp4", fps=30)

# Write frames to the video
for _ in range(100):
    writer.append_data(image)

writer.close()