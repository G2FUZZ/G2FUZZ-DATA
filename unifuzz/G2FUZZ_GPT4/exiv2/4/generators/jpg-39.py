import numpy as np
import cv2
import os

def generate_dct_image_with_advanced_features(width, height, filename, watermark_text, watermark_position, focal_point, focal_radius, high_quality_factor, low_quality_factor, gradient_compression=False):
    if not os.path.exists('./tmp/'):
        os.makedirs('./tmp/')

    img = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    img_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    y, cr, cb = cv2.split(img_ycrcb)

    def apply_selective_dct(channel, quality_map):
        channel_float = channel.astype(np.float32)
        dct = cv2.dct(channel_float)
        dct_quanted = np.round(dct / quality_map)
        channel_recovered = cv2.idct(dct_quanted * quality_map)  # Changed to apply quality map in reverse
        channel_recovered = np.clip(channel_recovered, 0, 255).astype(np.uint8)
        return channel_recovered

    # Create a quality map for selective or gradient compression
    if gradient_compression:
        x = np.linspace(-1, 1, width)
        y = np.linspace(-1, 1, height)
        xv, yv = np.meshgrid(x, y)
        dist = np.sqrt(xv**2 + yv**2)
        max_dist = np.sqrt(2)
        quality_map = ((dist / max_dist) * (low_quality_factor - high_quality_factor)) + high_quality_factor
    else:
        quality_map = np.full((height, width), low_quality_factor, dtype=np.float32)
        cv2.circle(quality_map, focal_point, focal_radius, high_quality_factor, -1)

    y_dct = apply_selective_dct(y, quality_map)
    cr_dct = apply_selective_dct(cr, quality_map)
    cb_dct = apply_selective_dct(cb, quality_map)

    img_dct = cv2.merge([y_dct, cr_dct, cb_dct])
    img_dct_bgr = cv2.cvtColor(img_dct, cv2.COLOR_YCrCb2BGR)

    # Dynamic watermark color based on the image background
    watermark_color = (255 - img_dct_bgr[watermark_position[1], watermark_position[0]]).tolist()

    cv2.putText(img_dct_bgr, watermark_text, watermark_position, cv2.FONT_HERSHEY_SIMPLEX, 1, watermark_color, 2, cv2.LINE_AA)
    
    cv2.imwrite(f'./tmp/{filename}', img_dct_bgr)

# Example usage
generate_dct_image_with_advanced_features(
    256,
    256,
    'dct_compressed_advanced_features.jpg',
    '©2023 My Watermark',
    watermark_position=(10, 30),
    focal_point=(128, 128),
    focal_radius=50,
    high_quality_factor=8,  # Higher quality (less compression) in focal area
    low_quality_factor=32,  # Lower quality (more compression) in other areas
    gradient_compression=True
)