from PIL import Image, ImageDraw
import os

def create_large_image(width, height):
    """Create a large image with some pattern or content."""
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)
    
    # Drawing a simple pattern
    for i in range(0, width, 100):
        for j in range(0, height, 100):
            draw.line((i, 0, i, height), fill=(255, 0, 0))
            draw.line((0, j, width, j), fill=(0, 255, 0))
    return img

def split_into_tiles(img, tile_width, tile_height):
    """Split the image into tiles."""
    img_width, img_height = img.size
    for x in range(0, img_width, tile_width):
        for y in range(0, img_height, tile_height):
            box = (x, y, x + tile_width, y + tile_height)
            yield img.crop(box)

def save_tiles(tiles, directory, base_filename):
    """Save tiles to the specified directory."""
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for i, tile in enumerate(tiles):
        filename = os.path.join(directory, f"{base_filename}_{i}.png")
        tile.save(filename)

def main():
    img_width, img_height = 2000, 2000  # Size of the large image
    tile_width, tile_width = 500, 500  # Size of the tiles
    
    # Create a large image
    large_image = create_large_image(img_width, img_height)
    
    # Split the large image into tiles
    tiles = split_into_tiles(large_image, tile_width, tile_width)
    
    # Save the tiles
    save_tiles(tiles, './tmp/', 'tile')

if __name__ == "__main__":
    main()