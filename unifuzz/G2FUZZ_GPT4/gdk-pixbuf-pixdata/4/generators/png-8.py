import numpy as np
import matplotlib.pyplot as plt
import os

# Create the tmp directory if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define image size and the number of images for demonstration
image_size = (256, 256, 3)  # 256x256 RGB image

# Generate images demonstrating the concept of filtering
num_images = 5
filters = ['None', 'Sub', 'Up', 'Average', 'Paeth']
for i, filter_name in enumerate(filters):
    # Generate a random image
    img_data = np.random.rand(*image_size)
    
    # Apply a simple filter effect for demonstration purposes
    if filter_name == 'Sub':
        img_data = np.cumsum(img_data, axis=1)  # Cumulative sum to simulate 'Sub' filter effect
    elif filter_name == 'Up':
        img_data = np.cumsum(img_data, axis=0)  # Cumulative sum to simulate 'Up' filter effect
    elif filter_name == 'Average':
        img_data = (np.cumsum(img_data, axis=1) + np.cumsum(img_data, axis=0)) / 2  # Average of 'Sub' and 'Up'
    elif filter_name == 'Paeth':
        img_data = np.abs(np.diff(img_data, axis=0, prepend=0))  # Difference to simulate 'Paeth' predictor
    
    # Normalize the image data to be in the range [0, 1]
    img_data -= img_data.min()
    img_data /= img_data.max()

    # Plot the image
    plt.imshow(img_data)
    plt.title(f'Filter: {filter_name}')
    plt.axis('off')
    
    # Save the plot to a PNG file
    file_path = os.path.join(output_dir, f'filter_demo_{i}.png')
    plt.savefig(file_path, bbox_inches='tight')
    plt.close()

print(f'Generated {num_images} images demonstrating filter effects, saved in {output_dir}')