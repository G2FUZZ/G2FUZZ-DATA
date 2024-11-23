from PIL import Image, ImageDraw, ImageFilter, ImageFont

# Function to generate and save an image with specified color space, resolution, color depth, text overlay, and filter
def generate_complex_image(color_space, resolution, color_depth, filename, text_overlay=None, filter_type=None):
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
        
    if text_overlay:
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()  # Using a built-in font
        draw.text((10, 10), text_overlay, fill='black', font=font)
    
    if filter_type == 'blur':
        image = image.filter(ImageFilter.BLUR)
    elif filter_type == 'detail':
        image = image.filter(ImageFilter.DETAIL)
    
    if image.mode == 'P':
        image = image.convert('RGB')  # Convert paletted image to RGB before saving as JPEG
    
    image.save(f'./tmp/{filename}.jpg')
    print(f"Image with color space '{color_space}', resolution '{resolution}', color depth '{color_depth}', text overlay '{text_overlay}', and filter '{filter_type}' saved as {filename}.jpg")

# Generate more complex images with text overlays and filters
generate_complex_image('rgb', 'standard', '24bit', 'image_rgb_standard_24bit_complex', text_overlay='Hello, World!', filter_type='blur')
generate_complex_image('cmyk', 'high', '8bit', 'image_cmyk_high_8bit_complex', text_overlay='CMYK Image', filter_type='detail')