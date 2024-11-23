import numpy as np
import matplotlib.pyplot as plt
import os

def ensure_dir(directory):
    """Ensures the given directory exists."""
    os.makedirs(directory, exist_ok=True)

def generate_gamma_corrected_images(output_dir, base_image):
    gamma_values = [0.5, 1.0, 1.5, 2.0]
    for gamma in gamma_values:
        gamma_corrected = np.power(base_image, gamma)
        plt.figure(figsize=(6, 6))
        plt.imshow(gamma_corrected, cmap='gray', vmin=0, vmax=1)
        plt.axis('off')
        plt.savefig(f'{output_dir}gamma_{gamma}.png', bbox_inches='tight', pad_inches=0)
        plt.close()

def generate_sine_modulated_images(output_dir, base_image):
    frequencies = [2, 4, 8, 16]
    for freq in frequencies:
        sine_wave = np.sin(2 * np.pi * freq * np.linspace(0, 1, base_image.shape[0]))
        sine_modulated = base_image * sine_wave[:, np.newaxis]
        plt.figure(figsize=(6, 6))
        plt.imshow(sine_modulated, cmap='gray', vmin=0, vmax=1)
        plt.axis('off')
        plt.savefig(f'{output_dir}sine_{freq}.png', bbox_inches='tight', pad_inches=0)
        plt.close()

def generate_combined_images(output_dir, base_image):
    gamma = 1.5
    freq = 8
    gamma_corrected = np.power(base_image, gamma)
    sine_wave = np.sin(2 * np.pi * freq * np.linspace(0, 1, base_image.shape[0]))
    combined = gamma_corrected * sine_wave[:, np.newaxis]
    plt.figure(figsize=(6, 6))
    plt.imshow(combined, cmap='gray', vmin=0, vmax=1)
    plt.axis('off')
    plt.savefig(f'{output_dir}combined_gamma_{gamma}_freq_{freq}.png', bbox_inches='tight', pad_inches=0)
    plt.close()

def main():
    base_output_dir = './tmp/complex_structures/'
    ensure_dir(base_output_dir)
    
    width, height = 256, 256
    base_image = np.tile(np.arange(width, dtype=np.float32) / width, (height, 1))

    # Generate gamma corrected images
    gamma_dir = os.path.join(base_output_dir, 'gamma/')
    ensure_dir(gamma_dir)
    generate_gamma_corrected_images(gamma_dir, base_image)

    # Generate sine modulated images
    sine_dir = os.path.join(base_output_dir, 'sine/')
    ensure_dir(sine_dir)
    generate_sine_modulated_images(sine_dir, base_image)

    # Generate combined images
    combined_dir = os.path.join(base_output_dir, 'combined/')
    ensure_dir(combined_dir)
    generate_combined_images(combined_dir, base_image)

if __name__ == '__main__':
    main()