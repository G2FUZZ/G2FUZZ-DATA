import os

content = "P3\n# Portable: PNM files are platform-independent and can be easily exchanged between different systems.\n1 1\n255\n255 255 255\n"
file_path = "./tmp/portable.pnm"

os.makedirs("./tmp", exist_ok=True)

with open(file_path, "w") as file:
    file.write(content)

print(f"File saved at: {file_path}")