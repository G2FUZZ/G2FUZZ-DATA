from PIL import Image

# Create a new image with RGB mode
img = Image.new('RGB', (100, 100))

# Progressive encoding with DCT compression and Progressive scan scripts
scan_scripts = b'\x00\x01\x02\x03\x04\x05\x06\x07'  # Example scan scripts data

img.save('./tmp/progressive_encoded_with_dct_and_scan_scripts.jpg', 'JPEG', quality=95, optimize=True, progressive=True, dct_mode='1', exif=scan_scripts, thumbnail=img.resize((64, 64)))