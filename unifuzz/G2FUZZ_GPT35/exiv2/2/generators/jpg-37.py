from PIL import Image

# Create a new image with RGB color mode and size 200x200
img = Image.new('RGB', (200, 200))

# Add ICC profile to the image
icc_profile_data = b'Fake ICC Profile Data'
icc_profile = b'\xff\xed' + (len(icc_profile_data) + 2).to_bytes(2, 'big') + icc_profile_data
img.info["icc_profile"] = icc_profile

# Add progressive mode to the image
img.info["progressive"] = 1

# Add custom comments to the image
comment_data = b'Custom Comment: This is a sample comment'
comment_marker = b'\xff\xfe' + (len(comment_data) + 2).to_bytes(2, 'big') + comment_data
img.info["comment"] = comment_marker

# Save the image with JPEG format and color depth of 8 bits per channel
img.save('./tmp/complex_jpg_file.jpg', quality=95)