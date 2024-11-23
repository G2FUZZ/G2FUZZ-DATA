import matplotlib.pyplot as plt

fig = plt.figure()
plt.text(0.5, 0.5, "Compatibility: Widely supported by various devices and software.", ha='center', va='center', fontsize=12)
plt.axis('off')
fig.savefig('./tmp/compatibility.jpg')
plt.close(fig)