from PIL import Image, ImageDraw
import os

def create_icon_with_hotspot(output_path, hotspot_x, hotspot_y, size=(64, 64), color=(0, 0, 255, 0)):
    # Create a new image with RGBA (Red, Green, Blue, Alpha) color mode
    img = Image.new("RGBA", size, color)

    # Optionally, draw something on the image
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, size[0]-10, size[1]-10], outline="white", width=2)

    # Ensure the output directory exists
    os.makedirs(output_path, exist_ok=True)

    # Define the icon filename
    icon_filename = "icon_with_hotspot.ico"
    # Save the image as an ICO file
    img.save(os.path.join(output_path, icon_filename))

    # Since ICO format doesn't support hotspots directly, we'll document the hotspot coordinates
    # by creating a separate text file or embedding it in the filename.
    # Here we're creating a text file approach.
    hotspot_info_filename = "icon_hotspot_info.txt"
    with open(os.path.join(output_path, hotspot_info_filename), 'w') as f:
        f.write(f"Hotspot X: {hotspot_x}\nHotspot Y: {hotspot_y}\n")
    print(f"Icon and hotspot info saved to {output_path}")

# Example usage
create_icon_with_hotspot("./tmp/", 32, 32, size=(64, 64), color=(255, 0, 0, 0))