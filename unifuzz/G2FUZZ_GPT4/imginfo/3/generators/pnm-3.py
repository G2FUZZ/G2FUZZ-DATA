import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the width and height for our images
width, height = 5, 5

# PBM data (P1) - simple checkerboard pattern
pbm_data = "\n".join(
    " ".join(str((x + y) % 2) for x in range(width))
    for y in range(height)
)

# PGM data (P2) - gradient from black to white
pgm_data = "\n".join(
    " ".join(str((y * 255) // (height - 1)) for x in range(width))
    for y in range(height)
)

# PPM data (P3) - simple RGB gradient
ppm_data = "\n".join(
    " ".join(f"{255 * x // (width - 1)} {255 * y // (height - 1)} {255 * (x + y) // (width + height - 2)}" 
             for x in range(width)) 
    for y in range(height)
)

# Save PBM file
with open('./tmp/sample.pbm', 'w') as f:
    f.write("P1\n")
    f.write(f"{width} {height}\n")
    f.write(pbm_data)

# Save PGM file
with open('./tmp/sample.pgm', 'w') as f:
    f.write("P2\n")
    f.write(f"{width} {height}\n")
    f.write("255\n")  # Max gray value
    f.write(pgm_data)

# Save PPM file
with open('./tmp/sample.ppm', 'w') as f:
    f.write("P3\n")
    f.write(f"{width} {height}\n")
    f.write("255\n")  # Max color value
    f.write(ppm_data)