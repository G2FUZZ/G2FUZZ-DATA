import os

# Generate pixel data for image 1
image1_data = "RGB: 255, 0, 0\n" * 10  # Sample RGB data
image1_filename = "./tmp/image1_pixdata.txt"
with open(image1_filename, "w") as file1:
    file1.write(image1_data)

# Generate pixel data for image 2
image2_data = "Grayscale: 128\n" * 10  # Sample grayscale data
image2_filename = "./tmp/image2_pixdata.txt"
with open(image2_filename, "w") as file2:
    file2.write(image2_data)

print("Pixel data files generated successfully.")