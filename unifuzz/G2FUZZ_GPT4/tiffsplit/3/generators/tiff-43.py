from PIL import Image, ImageDraw
import os

# Create the tmp directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

def create_image_with_shape(color, shape, size=(100, 100)):
    image = Image.new("RGBA", size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    
    if shape == "circle":
        radius = min(size) // 3
        left_up_point = (size[0]//2 - radius, size[1]//2 - radius)
        right_down_point = (size[0]//2 + radius, size[1]//2 + radius)
        draw.ellipse([left_up_point, right_down_point], fill=color)
    elif shape == "square":
        edge_length = min(size) // 2
        left_up_point = (size[0]//2 - edge_length//2, size[1]//2 - edge_length//2)
        right_down_point = (size[0]//2 + edge_length//2, size[1]//2 + edge_length//2)
        draw.rectangle([left_up_point, right_down_point], fill=color)

    return image

layer1 = create_image_with_shape("red", "circle", size=(200, 200))
layer2 = create_image_with_shape("blue", "square", size=(150, 150))

additional_layers = []

layer1.save('./tmp/complex_multi_layer.tiff', save_all=True, append_images=[layer2] + additional_layers, transparency=0)

print("Complex TIFF with layers created at ./tmp/complex_multi_layer.tiff")