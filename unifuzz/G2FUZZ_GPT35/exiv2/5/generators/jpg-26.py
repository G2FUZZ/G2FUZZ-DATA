from PIL import Image, ImageDraw

# Create a black image with white text
image = Image.new('RGB', (100, 50), color='black')
text = "Lossless Rotation"
draw = ImageDraw.Draw(image)
draw.text((10, 10), text, fill='white')

# Add a comment marker to the image
comment = b'Hello, this is a comment marker in a JPEG file.'
image.info["comment"] = comment

# Save the image with the comment marker
image.save('./tmp/lossless_rotation_with_comment.jpg')