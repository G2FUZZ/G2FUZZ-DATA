import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots()

# Add text with the desired features
ax.text(0.5, 0.5, "Platform-independent: PNG files are platform-independent and can be displayed on various operating systems and devices.", 
        horizontalalignment='center', verticalalignment='center', fontsize=12, color='black')

# Hide axes
ax.axis('off')

# Save the figure as a PNG file
plt.savefig('./tmp/platform_independent.png', format='png')

# Show the figure
plt.show()