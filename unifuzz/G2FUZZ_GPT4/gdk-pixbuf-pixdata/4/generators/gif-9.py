from PIL import Image

# Define the output directory and filename
output_dir = './tmp/'
output_filename = 'aspect_ratio_info.gif'

# Create a new image with RGB mode
img = Image.new('RGB', (320, 240), color=(73, 109, 137))

# Ensure the output directory exists
import os
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the image as a GIF
img.save(output_dir + output_filename)

# Now, manually append an application-specific extension for aspect ratio
aspect_ratio_code = b"\x01"  # Example byte for aspect ratio; actual calculation might be needed
application_id = b"NETSCAPE2.0"  # Common application block ID for demonstration
application_auth_code = b"ASPECT"  # Custom authentication code for demonstration purposes

# Construct the application extension block manually
# Format: Extension Introducer (0x21), Application Extension Label (0xFF), Block Size (0x0B),
# Application Identifier (8 bytes), Application Authentication Code (3 bytes),
# Data Sub-blocks (variable size), Block Terminator (0x00)
app_extension = bytes([0x21, 0xFF, 0x0B]) + application_id + application_auth_code + bytes([0x01, len(aspect_ratio_code)]) + aspect_ratio_code + bytes([0x00])

# Open the saved GIF to append the application-specific extension
with open(output_dir + output_filename, 'ab') as f:  # 'ab' mode to append binary data
    f.write(app_extension)

print(f"GIF with aspect ratio information created at {output_dir + output_filename}")