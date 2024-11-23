from PIL import Image

# Create a new image with RGB color mode and size 100x100
img = Image.new('RGB', (100, 100))

# Add JFIF format feature to the image
img.info["jfif"] = 1

# Add custom APP markers for application-specific information
app_marker_data = b'My Custom APP Marker Data'
app_marker = b'\xff\xe1' + (len(app_marker_data) + 2).to_bytes(2, 'big') + app_marker_data
img.info["APP"] = app_marker

# Add Color management feature
color_management_data = b'Color management information'
color_management_marker = b'\xff\xed' + (len(color_management_data) + 2).to_bytes(2, 'big') + color_management_data
img.info["Color management"] = color_management_marker

# Add Quantization matrices feature
quantization_matrices_data = b'Custom Quantization matrices'
quantization_matrices_marker = b'\xff\xdb' + (len(quantization_matrices_data) + 2).to_bytes(2, 'big') + quantization_matrices_data
img.info["Quantization matrices"] = quantization_matrices_marker

# Save the image with JPEG format and color depth of 8 bits per channel
img.save('./tmp/color_depth_example_with_JFIF_and_APP_and_color_management_and_quantization_matrices.jpg', quality=95)