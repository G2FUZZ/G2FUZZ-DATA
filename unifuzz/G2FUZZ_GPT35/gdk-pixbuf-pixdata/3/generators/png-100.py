import matplotlib.pyplot as plt

text = "7. High Quality: PNG supports high-quality images with lossless compression."

fig, ax = plt.subplots()
ax.set_facecolor('lightgray')
ax.text(0.5, 0.5, text, va='center', ha='center', wrap=True, fontsize=12, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=1'))
ax.axis('off')

plt.savefig('./tmp/high_quality_png.png', format='png', dpi=300)
plt.close()