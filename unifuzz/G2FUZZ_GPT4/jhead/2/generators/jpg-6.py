from PIL import Image, ImageCms
import os

# Print the current working directory (for debugging purposes)
print("Current Working Directory:", os.getcwd())

# Create an image
width, height = 800, 600
image = Image.new("RGB", (width, height), "blue")

# Load an ICC profile
# Ensure this path is correct relative to the current working directory
icc_profile_path = "sRGB_v4_ICC_preference.icc"
if not os.path.exists(icc_profile_path):
    print(f"Error: The file {icc_profile_path} does not exist.")
else:
    with open(icc_profile_path, "rb") as f:
        icc_profile = f.read()

    # Ensure the target directory exists
    os.makedirs("./tmp/", exist_ok=True)

    # Save the image with the ICC profile embedded
    output_path = "./tmp/icc_profiled_image.jpg"
    image.save(output_path, "JPEG", icc_profile=icc_profile)

    print(f"Image saved to {output_path} with an embedded ICC profile.")