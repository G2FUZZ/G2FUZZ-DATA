from PIL import Image, ImageDraw
import os
import piexif

def create_image_with_text(size, text, bgcolor=(255, 255, 255), fgcolor=(0, 0, 0), color_space="RGB"):
    """Create an image with some text."""
    if color_space == "CMYK":
        image = Image.new("CMYK", size, color=bgcolor)
    else:
        image = Image.new("RGB", size, color=bgcolor)
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), text, fill=fgcolor)
    return image

def save_image_with_compression_and_exif(image, path, exif_data, quality=75):
    """Save an image with specified JPEG quality and EXIF data."""
    image.save(path, 'JPEG', quality=quality, exif=exif_data)

def get_exif_data():
    """Generate fake EXIF data as an example."""
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
    first_ifd = {piexif.ImageIFD.Make: u"Fake Camera Make",  # It's okay to duplicate data across IFDs
                 piexif.ImageIFD.Model: u"Fake Camera Model"}

    # Assemble the EXIF data
    exif_dict = {"0th": zeroth_ifd, "Exif": exif_ifd, "GPS": gps_ifd, "1st": first_ifd}
    exif_bytes = piexif.dump(exif_dict)
    return exif_bytes

def generate_images_with_various_compressions_and_color_spaces_and_exif(base_name, qualities=[10, 50, 90], color_spaces=["RGB", "CMYK"]):
    """Generate and save images with various levels of compression, color spaces, and EXIF data."""
    os.makedirs('./tmp/', exist_ok=True)
    exif_data = get_exif_data()  # Generate EXIF data
    
    for color_space in color_spaces:
        for quality in qualities:
            image = create_image_with_text((200, 100), f'Quality: {quality}, {color_space}', color_space=color_space)
            filename = f'{base_name}_quality_{quality}_{color_space}.jpg'
            filepath = os.path.join('./tmp/', filename)
            save_image_with_compression_and_exif(image, filepath, exif_data, quality=quality)

generate_images_with_various_compressions_and_color_spaces_and_exif('test_image')