from PIL import Image, ImageDraw, ImageFont
import os

def generate_complex_chroma_subsampling_image():
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)

    # Create an image with a colorful pattern
    base_image_size = (400, 400)
    base_image = Image.new('RGB', base_image_size, 'white')
    draw = ImageDraw.Draw(base_image)
    
    for i in range(0, 400, 20):
        for j in range(0, 400, 20):
            color = (i % 256, j % 256, (i+j) % 256)
            draw.rectangle([i, j, i+10, j+10], fill=color)
    
    # Define subsampling settings and their labels
    subsampling_settings = [(0, "4:4:4"), (1, "4:2:2"), (2, "4:2:0")]
    thumbnails = []
    
    # Create thumbnails with different subsampling settings
    for setting, label in subsampling_settings:
        thumbnail = base_image.copy()
        thumbnail.save(f'./tmp/tmp_subsampling_{label}.jpg', 'JPEG', quality=95, subsampling=setting)
        thumbnail = Image.open(f'./tmp/tmp_subsampling_{label}.jpg')
        draw = ImageDraw.Draw(thumbnail)
        thumbnails.append(thumbnail)
    
    # Create a new image to hold the grid
    grid_image_size = (base_image_size[0] * len(subsampling_settings), base_image_size[1])
    grid_image = Image.new('RGB', grid_image_size, 'white')
    
    # Paste thumbnails into the grid image
    for i, thumbnail in enumerate(thumbnails):
        grid_image.paste(thumbnail, (i * base_image_size[0], 0))
    
    # Optionally, add labels to the thumbnails
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except IOError:
        font = ImageFont.load_default()
        
    draw = ImageDraw.Draw(grid_image)
    for i, (_, label) in enumerate(subsampling_settings):
        draw.text((i * base_image_size[0] + 10, base_image_size[1] - 30), label, (255, 255, 255), font=font)
    
    # Save the grid image
    grid_image.save('./tmp/complex_subsampling_grid.jpg', 'JPEG', quality=95)

generate_complex_chroma_subsampling_image()