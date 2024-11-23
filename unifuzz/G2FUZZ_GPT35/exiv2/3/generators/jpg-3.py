from PIL import Image

# Function to generate and save an image with specified color space
def generate_image(color_space, filename):
    if color_space.lower() == 'rgb':
        image = Image.new('RGB', (100, 100), color='red')
    elif color_space.lower() == 'cmyk':
        image = Image.new('CMYK', (100, 100), color='cyan')
    elif color_space.lower() == 'grayscale':
        image = Image.new('L', (100, 100), color='gray')
    else:
        print("Invalid color space")
        return
    
    image.save(f'./tmp/{filename}.jpg')
    print(f"Image with color space '{color_space}' saved as {filename}.jpg")

# Generate images with different color spaces
generate_image('rgb', 'image_rgb')
generate_image('cmyk', 'image_cmyk')
generate_image('grayscale', 'image_grayscale')