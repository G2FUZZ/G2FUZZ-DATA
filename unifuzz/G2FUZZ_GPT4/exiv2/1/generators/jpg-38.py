from PIL import Image, ImageDraw, ImageFont
import os
import piexif
import textwrap

def create_complex_image(size, text, bgcolor=(255, 255, 255), fgcolor=(0, 0, 0), color_space="RGB", font_path=None):
    """Create an image with complex structures including shapes and text."""
    # Create base image
    if color_space == "CMYK":
        image = Image.new("CMYK", size, color=bgcolor)
    else:
        image = Image.new("RGB", size, color=bgcolor)
    draw = ImageDraw.Draw(image)

    # Add shapes
    rectangle_color = (255, 0, 0)  # Red
    draw.rectangle([10, size[1] / 2, size[0] - 10, size[1] - 10], outline=rectangle_color, fill=None)
    circle_color = (0, 255, 0)  # Green
    draw.ellipse([size[0] / 4, size[1] / 4, 3 * size[0] / 4, 3 * size[1] / 4], fill=circle_color, outline=None)

    # Determine font size and style
    if font_path:
        try:
            font_size = int(size[1] / 10)
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            print(f"Font file not found at {font_path}. Falling back to default font.")
            font = ImageFont.load_default()
    else:
        font = ImageFont.load_default()

    # Adjust text to fit the image
    wrapped_text = textwrap.fill(text, width=20)
    draw.multiline_text((10, 10), wrapped_text, fill=fgcolor, font=font)

    # Create a second layer
    overlay = Image.new("RGBA", size, (255, 255, 255, 0))  # Fully transparent
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_text_color = (0, 0, 255, 128)  # Semi-transparent blue text
    overlay_draw.text((10, size[1] - 40), "Overlay Text", fill=overlay_text_color, font=font)

    # Merge base image and overlay
    combined = Image.alpha_composite(image.convert("RGBA"), overlay)

    return combined

def save_image_with_compression_and_exif(image, path, exif_data, quality=75):
    """Save an image with specified JPEG quality and EXIF data."""
    image.save(path, 'JPEG', quality=quality, exif=exif_data)

def get_exif_data():
    """Generate fake EXIF data as an example."""
    # EXIF data generation code remains the same
    zeroth_ifd = {piexif.ImageIFD.Make: u"Fake Camera Make",
                  piexif.ImageIFD.Model: u"Fake Camera Model",
                  piexif.ImageIFD.Software: u"Piexif"}
    exif_ifd = {piexif.ExifIFD.DateTimeOriginal: u"2023:01:01 00:00:00",
                piexif.ExifIFD.LensMake: u"Fake Lens Make",
                piexif.ExifIFD.Sharpness: 65535,
                piexif.ExifIFD.LensSpecification: ((1, 1), (1, 1), (1, 1), (1, 1))}
    gps_ifd = {piexif.GPSIFD.GPSLatitudeRef: u"N",
               piexif.GPSIFD.GPSLatitude: ((30, 1), (15, 1), (0, 1)),
               piexif.GPSIFD.GPSLongitudeRef: u"E",
               piexif.GPSIFD.GPSLongitude: ((115, 1), (30, 1), (0, 1))}
    first_ifd = {piexif.ImageIFD.Make: u"Fake Camera Make",
                 piexif.ImageIFD.Model: u"Fake Camera Model"}

    exif_dict = {"0th": zeroth_ifd, "Exif": exif_ifd, "GPS": gps_ifd, "1st": first_ifd}
    exif_bytes = piexif.dump(exif_dict)
    return exif_bytes

def generate_complex_images(base_name, qualities=[10, 50, 90], color_spaces=["RGB", "CMYK"], font_path=None):
    """Generate and save images with complex structures."""
    os.makedirs('./tmp/', exist_ok=True)
    exif_data = get_exif_data()  # Generate EXIF data
    
    for color_space in color_spaces:
        for quality in qualities:
            image = create_complex_image((400, 200), f"Quality: {quality}, {color_space}. Complex structures included.", color_space=color_space, font_path=font_path)
            filename = f'{base_name}_complex_{quality}_{color_space}.jpg'
            filepath = os.path.join('./tmp/', filename)
            save_image_with_compression_and_exif(image.convert("RGB"), filepath, exif_data, quality=quality)

generate_complex_images('complex_test_image', font_path="path/to/your/font.ttf")