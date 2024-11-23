import numpy as np
import matplotlib.pyplot as plt

# Generating a more complex image
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.linspace(-2*np.pi, 2*np.pi, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

# Display the image with a title and customized color map
plt.imshow(Z, cmap='viridis')
plt.title('Sine and Cosine Pattern')
plt.colorbar()

# Save the image as a PNG file with higher quality
plt.savefig('./tmp/complex_image.png', format='png', dpi=300)

plt.show()