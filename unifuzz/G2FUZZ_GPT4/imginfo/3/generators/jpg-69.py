import numpy as np
import cv2
import os
from datetime import datetime

def apply_circular_mask(image):
    center = (image.shape[1] // 2, image.shape[0] // 2)
    radius = min(center[0], center[1], 100)
    Y, X = np.ogrid[:image.shape[0], :image.shape[1]]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y - center[1])**2)
    mask = dist_from_center <= radius
    circular_image = np.zeros_like(image)
    circular_image[mask] = image[mask]
    return circular_image

def add_text_overlay(image, text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10, image.shape[0] - 10)
    fontScale = 1
    fontColor = (255, 255, 255)
    lineType = 2
    cv2.putText(image, text, bottomLeftCornerOfText, font, fontScale, fontColor, lineType)
    return image

def create_complex_gradient_image():
    base_dir = './tmp/'
    os.makedirs(base_dir, exist_ok=True)
    
    now = datetime.now()
    dir_path = now.strftime(base_dir + "%Y/%m/%d/%H/")
    os.makedirs(dir_path, exist_ok=True)
    
    width, height = 512, 512
    image = np.zeros((height, width, 3), dtype=np.uint8)
    
    for y in range(height):
        for x in range(width):
            image[y, x] = [(x + y) % 256, (256 - abs(x - y)) % 256, (x * y) % 256]
    
    for y in range(height):
        for x in range(width):
            if x % 2 == 0 and y % 2 == 0:
                temp = image[y, x].astype(np.int16) + np.array([(y) % 256, (width - x) % 256, (height - y) % 256], dtype=np.int16)
                image[y, x] = np.mod(temp, 256).astype(np.uint8)
    
    image = apply_circular_mask(image)
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    image = add_text_overlay(image, timestamp)
    
    filename = now.strftime("%Y%m%d_%H%M%S") + '_complex_gradient_image.jpg'
    cv2.imwrite(os.path.join(dir_path, filename), image)
    print(f"Image saved as {os.path.join(dir_path, filename)}")

create_complex_gradient_image()