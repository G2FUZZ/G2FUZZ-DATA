from PIL import Image, ImageDraw

def create_image_with_text(size, text, bg_color):
    # Create an image with the given background color
    img = Image.new('RGB', size, color=bg_color)
    # Initialize the drawing context
    draw = ImageDraw.Draw(img)
    # Set the text position
    text_position = (10, 10)
    # Set the text color
    text_color = (255, 255, 255)  # White
    # Draw the text on the image
    draw.text(text_position, text, fill=text_color)
    return img

def save_multi_page_tiff(path, images):
    # Save the first image
    images[0].save(
        path,
        save_all=True,
        append_images=images[1:],
        compression="tiff_deflate",
    )

def main():
    # Directory to save the TIFF file
    output_dir = './tmp/'
    # TIFF file name
    tiff_filename = 'multi_page.tiff'
    # Full path for the TIFF file
    tiff_path = output_dir + tiff_filename
    
    # Create a list of images
    images = [
        create_image_with_text((200, 200), f"Page {i+1}", bg_color)
        for i, bg_color in enumerate(['red', 'green', 'blue', 'yellow'])
    ]
    
    # Save the list of images as a multi-page TIFF
    save_multi_page_tiff(tiff_path, images)
    
    print(f"Multi-page TIFF saved at: {tiff_path}")

if __name__ == "__main__":
    main()