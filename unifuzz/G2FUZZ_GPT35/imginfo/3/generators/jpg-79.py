import os
import matplotlib.pyplot as plt

# Create a figure with multiple subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Add text with different styles to each subplot
for i in range(2):
    for j in range(2):
        axs[i, j].text(0.5, 0.5, f"Plot {i+1}-{j+1}", ha='center', va='center', fontsize=16, color='blue', style='italic')

# Customize the overall layout
plt.tight_layout()

# Create the directory if it does not exist
os.makedirs('./tmp/complex_plots/', exist_ok=True)

# Save the figure with a complex file structure
fig.savefig('./tmp/complex_plots/plot_collection.jpg')

# Close the figure
plt.close(fig)