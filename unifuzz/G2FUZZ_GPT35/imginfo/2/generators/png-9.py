import numpy as np
import matplotlib.pyplot as plt

# Create a simple PNG image with text
text = "PNG is an open standard file format, promoting interoperability and accessibility"
plt.text(0.5, 0.5, text, ha='center', va='center', fontsize=12)
plt.axis('off')

# Save the image as a PNG file
plt.savefig('./tmp/open_standard.png', format='png')