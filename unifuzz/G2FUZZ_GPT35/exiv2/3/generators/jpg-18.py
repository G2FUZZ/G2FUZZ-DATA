from PIL import Image

# Function to generate and save an image with specified color space and resolution
def generate_image(color_space, resolution, filename):
    if color_space.lower() == 'rgb':
        image = Image.new('RGB', (100, 100), color='red')
    elif color_space.lower() == 'cmyk':
        image = Image.new('CMYK', (100, 100), color='cyan')
    elif color_space.lower() == 'grayscale':
        image = Image.new('L', (100, 100), color='gray')
    else:
        print("Invalid color space")
        return
    
    if resolution.lower() == 'high':
        image = image.resize((800, 800))
    
    image.save(f'./tmp/{filename}.jpg')
    print(f"Image with color space '{color_space}' and resolution '{resolution}' saved as {filename}.jpg")

# Generate images with different color spaces and resolutions
generate_image('rgb', 'standard', 'image_rgb_standard')
generate_image('cmyk', 'high', 'image_cmyk_high')
generate_image('grayscale', 'high', 'image_grayscale_high')