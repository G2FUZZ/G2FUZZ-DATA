import numpy as np
import matplotlib.pyplot as plt

# Create a platform-independent PNG file with the given feature
fig, ax = plt.subplots()
ax.text(0.5, 0.5, "PNG files are platform-independent", ha='center', va='center', fontsize=12, color='black')
ax.axis('off')

plt.savefig('./tmp/platform_independent.png')
plt.close()