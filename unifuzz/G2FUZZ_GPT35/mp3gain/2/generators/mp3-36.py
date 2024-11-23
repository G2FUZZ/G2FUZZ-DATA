import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate dummy mp3 file with VBR encoding, DRM protection, and custom metadata
mp3_data = b'\xFF\xFA\x80\x00\x40'  # Dummy mp3 data with VBR encoding
drm_protection_data = b'DRM protection data'  # Dummy DRM protection data
metadata = b'Custom metadata'  # Dummy custom metadata

mp3_filename = './tmp/extended_example_with_more_complex_features.mp3'

with open(mp3_filename, 'wb') as file:
    file.write(mp3_data)
    file.write(drm_protection_data)
    file.write(metadata)

print(f"'{mp3_filename}' file with VBR encoding, DRM protection, and custom metadata has been generated.")