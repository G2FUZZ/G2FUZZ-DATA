from PIL import Image, ImageDraw
import os

def create_cursor_with_hotspot(output_path, hotspot=(0, 0), size=(32, 32), color=(0, 0, 0, 0)):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Create a new image with RGBA (to support transparency)
    image = Image.new("RGBA", size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    
    # Draw a simple shape to represent the pointer/cursor
    # Here, it's a basic triangle pointing upwards
    draw.polygon([(size[0]//2, size[1]//4), 
                  (size[0]//4, 3*size[1]//4), 
                  (3*size[1]//4, 3*size[1]//4)], fill=color)
    
    # Convert the PIL image to .ico format, including hotspot coordinates for .cur
    # Since PIL does not natively support hotspot in .ico or .cur, this part will only save the icon image.
    # The hotspot information should be manually handled or supported by another library/tool that supports .cur files specifically.
    image.save(output_path, format='ICO', sizes=[size])
    
# Example usage
create_cursor_with_hotspot('./tmp/custom_cursor.ico', hotspot=(16, 16), size=(32, 32), color=(0, 0, 0, 255))