import os

def create_ascii_pnm(filepath):
    # P2 denotes a grayscale image in ASCII format
    header = "P2\n"
    width, height = 5, 5
    maxval = 255
    data = "\n".join(" ".join(str((x*y) % maxval) for x in range(width)) for y in range(height))
    
    content = f"{header}{width} {height}\n{maxval}\n{data}"
    
    with open(filepath, "w") as file:
        file.write(content)

def create_binary_pnm(filepath):
    # P5 denotes a grayscale image in Binary format
    header = b"P5\n"
    width, height = 5, 5
    maxval = 255
    data = bytearray((x*y) % maxval for y in range(height) for x in range(width))
    
    content = header + f"{width} {height}\n{maxval}\n".encode() + data
    
    with open(filepath, "wb") as file:
        file.write(content)

if __name__ == "__main__":
    os.makedirs("./tmp/", exist_ok=True)
    create_ascii_pnm("./tmp/ascii_pnm.pnm")
    create_binary_pnm("./tmp/binary_pnm.pnm")