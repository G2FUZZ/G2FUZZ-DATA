import numpy as np
import cv2
import os

def generate_dct_image_with_advanced_features(width, height, filename, watermark_text, focal_point, focal_radius, high_quality_factor, low_quality_factor, edge_effect=False):
    if not os.path.exists('./tmp/'):
        os.makedirs('./tmp/')

    # Generate a random image
    img = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    img_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    y, cr, cb = cv2.split(img_ycrcb)

    def apply_selective_dct(channel, quality_map):
        channel_float = channel.astype(np.float32)
        dct = cv2.dct(channel_float)
        dct_quanted = np.round(dct / quality_map)
        channel_recovered = cv2.idct(dct_quanted)
        channel_recovered = np.clip(channel_recovered, 0, 255).astype(np.uint8)
        return channel_recovered

    # Create a gradient quality map for selective compression
    x = np.arange(width)
    y_grid = np.arange(height)  # Renamed to avoid confusion with the 'y' channel
    xv, yv = np.meshgrid(x, y_grid)
    distance_from_center = np.sqrt((xv - focal_point[0])**2 + (yv - focal_point[1])**2)
    normalized_distance = distance_from_center / np.max(distance_from_center)
    quality_map = low_quality_factor + (high_quality_factor - low_quality_factor) * (1 - normalized_distance)
    quality_map = np.clip(quality_map, high_quality_factor, low_quality_factor).astype(np.float32)
    
    y_dct = apply_selective_dct(y, quality_map)
    cr_dct = apply_selective_dct(cr, quality_map)
    cb_dct = apply_selective_dct(cb, quality_map)

    if edge_effect:
        # Apply edge detection on the focal region
        mask = np.zeros_like(y_dct, dtype=np.uint8)
        cv2.circle(mask, focal_point, focal_radius, 255, -1)
        y_for_canny = np.clip(y, 0, 255).astype(np.uint8)  # Ensure y is suitable for Canny
        edges = cv2.Canny(y_for_canny, 100, 200)
        y_dct = np.where((mask != 0) & (edges != 0), 255, y_dct)

    img_dct = cv2.merge([y_dct, cr_dct, cb_dct])
    img_dct_bgr = cv2.cvtColor(img_dct, cv2.COLOR_YCrCb2BGR)

    # Add semi-transparent watermark
    watermark = np.zeros_like(img_dct_bgr)
    cv2.putText(watermark, watermark_text, (10, height - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255, 128), 2, cv2.LINE_AA)
    cv2.addWeighted(img_dct_bgr, 1, watermark, 0.5, 0, img_dct_bgr)
    
    # Save the generated image into './tmp/'
    cv2.imwrite(f'./tmp/{filename}', img_dct_bgr)

# Example usage
generate_dct_image_with_advanced_features(
    256,
    256,
    'dct_advanced_features.jpg',
    '©2023 My Watermark',
    focal_point=(128, 128),
    focal_radius=50,
    high_quality_factor=8,  # Higher quality closer to the focal point
    low_quality_factor=32,  # Lower quality farther from the focal point
    edge_effect=True        # Apply edge effect in the focal area
)