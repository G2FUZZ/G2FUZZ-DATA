import numpy as np
import matplotlib.pyplot as plt
import os

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def generate_pattern(pattern_type, freq, size=(256, 256)):
    x, y = np.meshgrid(np.linspace(0, freq*np.pi, size[0]), np.linspace(0, freq*np.pi, size[1]))
    if pattern_type == "sin":
        z = np.sin(x) + np.sin(y)
    elif pattern_type == "cos":
        z = np.cos(x) + np.cos(y)
    elif pattern_type == "mixed":
        z = np.sin(x) + np.cos(y)
    else:
        raise ValueError("Unsupported pattern type")
    return z

def save_pattern_image(pattern_image, output_dir, pattern_type, freq):
    plt.figure(figsize=(6, 6))
    plt.imshow(pattern_image, cmap='viridis', interpolation='nearest')
    plt.axis('off')
    filename = f"{pattern_type}_freq_{freq}.png"
    plt.savefig(os.path.join(output_dir, pattern_type, filename), format='png', bbox_inches='tight', pad_inches=0)
    plt.close()

def create_complex_file_structure(output_dir, image_size, frequencies, pattern_types):
    ensure_dir(output_dir)
    for pattern_type in pattern_types:
        ensure_dir(os.path.join(output_dir, pattern_type))
        for freq in frequencies:
            pattern_image = generate_pattern(pattern_type, freq, size=image_size)
            save_pattern_image(pattern_image, output_dir, pattern_type, freq)

def combine_images_into_grid(output_dir, pattern_types, grid_dims=(2, 2)):
    fig, axs = plt.subplots(grid_dims[0], grid_dims[1], figsize=(12, 12))
    for ax, pattern_type in zip(axs.flatten(), pattern_types):
        pattern_images = os.listdir(os.path.join(output_dir, pattern_type))
        if pattern_images:
            img_path = os.path.join(output_dir, pattern_type, pattern_images[0])
            img = plt.imread(img_path)
            ax.imshow(img)
            ax.axis('off')
            ax.set_title(pattern_type)
        else:
            ax.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "master_image.png"), format='png', bbox_inches='tight', pad_inches=0)
    plt.close()

output_dir = "./tmp/complex_patterns"
image_size = (256, 256)
frequencies = [4, 8, 12]  # Example frequencies
pattern_types = ["sin", "cos", "mixed"]

create_complex_file_structure(output_dir, image_size, frequencies, pattern_types)
combine_images_into_grid(output_dir, pattern_types)