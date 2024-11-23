from PIL import Image, ImageDraw

def create_tga_image():
    # Image dimensions
    width, height = 800, 600

    # Create a new image with RGBA (Red, Green, Blue, Alpha) mode 
    image = Image.new("RGBA", (width, height))
    
    # Initialize the draw context
    draw = ImageDraw.Draw(image)
    
    # Draw a gradient that could symbolize "Versatility"
    # This is a simple representation and can be adapted to your specific needs
    for i in range(width):
        # Define colors for the gradient
        red = int(255 * (i / width))
        green = int(255 * (1 - (i / width)))
        blue = 127  # A constant value for simplicity
        
        # Set the color with varying alpha to demonstrate the support for alpha channels
        color = (red, green, blue, 127)
        
        # Draw a vertical line with the specified color
        draw.line([(i, 0), (i, height)], fill=color)
    
    # Save the image as TGA file
    image.save("./tmp/versatility.tga")

create_tga_image()