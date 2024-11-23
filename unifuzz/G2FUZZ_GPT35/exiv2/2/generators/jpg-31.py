from PIL import Image

# Create a new image with RGBA color mode and size 200x200
img = Image.new('RGBA', (200, 200))

# Add custom comment to the image
comment_data = b'My Custom Comment Data'
comment_marker = b'\xff\xfe' + (len(comment_data) + 2).to_bytes(2, 'big') + comment_data
img.info["Comment"] = comment_marker

# Add ICC profile for color management
icc_profile_data = b'ICC Profile Information'
icc_profile_marker = b'\xff\xdb' + (len(icc_profile_data) + 2).to_bytes(2, 'big') + icc_profile_data
img.info["ICC Profile"] = icc_profile_marker

# Add progressive scan feature
progressive_scan_data = b'Progressive Scan Information'
progressive_scan_marker = b'\xff\xda' + (len(progressive_scan_data) + 2).to_bytes(2, 'big') + progressive_scan_data
img.info["Progressive Scan"] = progressive_scan_marker

# Add custom marker for application-specific data
custom_marker_data = b'My Custom Marker Data'
custom_marker = b'\xff\xfe' + (len(custom_marker_data) + 2).to_bytes(2, 'big') + custom_marker_data
img.info["Custom Marker"] = custom_marker

# Convert RGBA image to RGB mode
img_rgb = img.convert('RGB')

# Save the image with JPEG format and color depth of 8 bits per channel
img_rgb.save('./tmp/complex_file_structure_example.jpg', quality=95)