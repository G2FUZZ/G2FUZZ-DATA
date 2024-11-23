from PIL import Image, ImageCms, PngImagePlugin
import os
from PIL.ExifTags import TAGS

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a simple image using RGB mode
image = Image.new("RGB", (100, 100), (255, 0, 0))

# Path to the sRGB profile (Adjust this path to the actual location of your sRGB profile)
srgb_profile_path = 'path_to_your_srgb_profile.icc'

# Load the sRGB color profile
try:
    srgb_profile = ImageCms.ImageCmsProfile(srgb_profile_path)
except OSError as e:
    print(f"Error opening sRGB profile: {e}")
    # Optionally, handle the error (e.g., use a default profile, exit the program, etc.)
else:
    # Convert the image to have the sRGB profile
    output = ImageCms.profileToProfile(image, srgb_profile, srgb_profile)

    # Prepare metadata for the image
    # Create an info dictionary to hold metadata
    info = PngImagePlugin.PngInfo()

    # Add metadata editing feature description
    metadata_editing_description = "Metadata Editing: Beyond simply containing metadata, JPEG files allow for the editing of this information without affecting the image data, enabling photographers and archivists to update or correct information such as tags, geolocation, and camera settings."

    # Add custom metadata
    info.add_text("Description", metadata_editing_description)

    # Alternatively, you can edit EXIF data if needed
    # For demonstration, setting a fake camera make and model
    exif_data = output.getexif()
    exif_data[271] = "CameraBrand"  # Camera Make
    exif_data[272] = "CameraModel"  # Camera Model

    # Convert the modified EXIF data back to bytes and attach it to the image
    output.putexif(exif_data)

    # Apply the sRGB color profile and save the image with metadata
    output.save('./tmp/colored_image_with_profile_and_metadata.jpg', 'JPEG', icc_profile=srgb_profile.tobytes(), pnginfo=info)

    print("Image saved with metadata editing feature.")