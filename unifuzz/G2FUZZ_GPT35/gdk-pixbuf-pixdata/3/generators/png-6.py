import matplotlib.pyplot as plt

text = "6. Portable: PNG is a portable format, widely supported across different platforms and software applications."

fig, ax = plt.subplots()
ax.text(0.5, 0.5, text, va='center', ha='center', wrap=True, fontsize=12)
ax.axis('off')

plt.savefig('./tmp/portable_png.png', format='png', dpi=300)
plt.close()