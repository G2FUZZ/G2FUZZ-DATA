from PIL import Image, ImageDraw, ImageCms
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to create a simple image for demonstration purposes
def create_image(width, height, color, color_space="RGB"):
    if color_space == "RGB":
        image = Image.new("RGB", (width, height), color)
    elif color_space == "CMYK":
        image = Image.new("CMYK", (width, height), color)
    elif color_space == "Lab":
        # Creating an L*a*b* image directly is not supported; convert from RGB
        image = Image.new("RGB", (width, height), color)
        rgb2lab = ImageCms.createProfile(colorSpace="sRGB")
        labProfile = ImageCms.createProfile("LAB")
        image = ImageCms.profileToProfile(image, rgb2lab, labProfile, outputMode='LAB')
    else:
        # Default back to RGB if an unsupported color space is requested
        image = Image.new("RGB", (width, height), color)
    
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), "Sample", fill="black" if color_space != "CMYK" else "white")
    return image

# Create images in different color spaces
image1 = create_image(100, 100, "red", "RGB")
image2 = create_image(100, 100, "green", "CMYK")
image3 = create_image(100, 100, "blue", "Lab")

# Save images as a multi-page TIFF, note that keeping different color spaces in one TIFF might not be properly supported by all viewers
tiff_path = os.path.join(output_dir, 'multi_color_space.tiff')
image1.save(tiff_path, save_all=True, append_images=[image2, image3], compression="tiff_deflate")