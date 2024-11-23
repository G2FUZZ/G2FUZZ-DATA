import numpy as np
import matplotlib.pyplot as plt

# Create a simple image with text
text = "Platform-independent: PNG files are\nviewable on different OS without\ncompatibility issues"
fig, ax = plt.subplots()
ax.text(0.5, 0.5, text, ha='center', va='center', fontsize=12, color='black')

# Save the image as a PNG file
plt.axis('off')
plt.savefig('./tmp/platform_independent.png', format='png', bbox_inches='tight', pad_inches=0.1)
plt.close()