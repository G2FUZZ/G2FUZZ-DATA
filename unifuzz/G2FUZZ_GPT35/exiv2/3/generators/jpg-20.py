from PIL import Image

# Function to generate and save an image with specified color space, resolution, and color depth
def generate_image(color_space, resolution, color_depth, filename):
    if color_space.lower() == 'rgb':
        if color_depth == '8bit':
            image = Image.new('RGB', (100, 100), color='red')
        elif color_depth == '24bit':
            image = Image.new('RGB', (100, 100), color='red')
    elif color_space.lower() == 'cmyk':
        if color_depth == '8bit':
            image = Image.new('CMYK', (100, 100), color='cyan')
        elif color_depth == '24bit':
            image = Image.new('CMYK', (100, 100), color='cyan')
    elif color_space.lower() == 'grayscale':
        if color_depth == '8bit':
            image = Image.new('L', (100, 100), color='gray')
        elif color_depth == '24bit':
            image = Image.new('L', (100, 100), color='gray')
    else:
        print("Invalid color space")
        return
    
    if resolution.lower() == 'high':
        image = image.resize((800, 800))
    
    if image.mode == 'P':
        image = image.convert('RGB')  # Convert paletted image to RGB before saving as JPEG
    
    image.save(f'./tmp/{filename}.jpg')
    print(f"Image with color space '{color_space}', resolution '{resolution}', and color depth '{color_depth}' saved as {filename}.jpg")

# Generate images with different color spaces, resolutions, and color depths
generate_image('rgb', 'standard', '8bit', 'image_rgb_standard_8bit')
generate_image('rgb', 'standard', '24bit', 'image_rgb_standard_24bit')
generate_image('cmyk', 'high', '8bit', 'image_cmyk_high_8bit')
generate_image('cmyk', 'high', '24bit', 'image_cmyk_high_24bit')
generate_image('grayscale', 'high', '8bit', 'image_grayscale_high_8bit')
generate_image('grayscale', 'high', '24bit', 'image_grayscale_high_24bit')