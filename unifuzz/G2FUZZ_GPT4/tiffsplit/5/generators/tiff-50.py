from PIL import Image, ImageDraw, ImageCms
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to create a layered image for demonstration purposes
def create_layered_image(width, height, base_color, layers, color_space="RGB"):
    base_image = Image.new("RGB", (width, height), base_color)
    rgb2profile = None
    output_profile = None
    if color_space == "CMYK":
        base_image = base_image.convert("CMYK")
    elif color_space == "Lab":
        rgb2profile = ImageCms.createProfile(colorSpace="sRGB")
        output_profile = ImageCms.createProfile("LAB")
        base_image = ImageCms.profileToProfile(base_image, rgb2profile, output_profile, outputMode='LAB')

    # Create layers with varying opacity
    images = [base_image]
    for i, (color, opacity) in enumerate(layers):
        layer = Image.new("RGBA", (width, height), color=color)
        layer.putalpha(int(opacity * 255))  # Convert opacity to a scale of 0-255
        
        # Composite the layer onto the base image if not the first layer
        if i > 0 or color_space != "RGB":
            composite = Image.alpha_composite(images[0].convert("RGBA"), layer)
            if color_space == "CMYK":
                composite = composite.convert("CMYK")
            elif color_space == "Lab" and rgb2profile and output_profile:
                composite = ImageCms.profileToProfile(composite.convert("RGB"), rgb2profile, output_profile, outputMode='LAB')
            images.append(composite)
        else:
            images.append(layer)

    return images

# Define colors and opacities for layers
layers = [("red", 0.5), ("green", 0.5), ("blue", 0.5)]

# Create layered images in different color spaces
images_rgb = create_layered_image(100, 100, "white", layers, "RGB")
images_cmyk = create_layered_image(100, 100, "white", layers, "CMYK")
images_lab = create_layered_image(100, 100, "white", layers, "Lab")

# Save images as a multi-page TIFF with multiple layers per page
tiff_path = os.path.join(output_dir, 'complex_multi_color_space.tiff')
images_rgb[0].save(tiff_path, save_all=True, append_images=images_rgb[1:] + images_cmyk + images_lab, compression="tiff_deflate")

print(f"TIFF file saved at: {tiff_path}")