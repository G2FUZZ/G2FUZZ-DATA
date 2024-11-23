import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots()

# Add text to the plot
ax.text(0.5, 0.5, "Wide compatibility: PNG files are widely supported across different platforms and software applications, making them a versatile choice for storing images.",
        horizontalalignment='center',
        verticalalignment='center',
        wrap=True)

# Remove axes
ax.axis('off')

# Save the plot as a PNG file
plt.savefig('./tmp/wide_compatibility.png', format='png', bbox_inches='tight', dpi=300)

# Show the plot
plt.show()