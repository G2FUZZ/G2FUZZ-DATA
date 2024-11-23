from PIL import Image
import os

# Function to generate and save an image with specified color space and save in subfolders
def generate_image(color_space, filename):
    if color_space.lower() == 'rgb':
        image = Image.new('RGB', (100, 100), color='red')
        folder = 'rgb_images'
    elif color_space.lower() == 'cmyk':
        image = Image.new('CMYK', (100, 100), color='cyan')
        folder = 'cmyk_images'
    elif color_space.lower() == 'grayscale':
        image = Image.new('L', (100, 100), color='gray')
        folder = 'grayscale_images'
    else:
        print("Invalid color space")
        return
    
    if not os.path.exists(f'./tmp/{folder}'):
        os.makedirs(f'./tmp/{folder}')
    
    image.save(f'./tmp/{folder}/{filename}.jpg')
    print(f"Image with color space '{color_space}' saved in '{folder}' as {filename}.jpg")

# Generate images with different color spaces and save in respective subfolders
generate_image('rgb', 'image_rgb')
generate_image('cmyk', 'image_cmyk')
generate_image('grayscale', 'image_grayscale')