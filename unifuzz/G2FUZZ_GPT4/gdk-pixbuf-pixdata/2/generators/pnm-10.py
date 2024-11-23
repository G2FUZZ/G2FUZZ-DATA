import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple PBM image (10x10 pixels)
pbm_data = "P1\n10 10\n" + "\n".join(["0 1 " * 5] * 10)
with open('./tmp/example.pbm', 'w') as file:
    file.write(pbm_data)

# Create a simple PGM image (10x10 pixels), with a gradient
pgm_data = "P2\n10 10\n255\n"
pgm_data += "\n".join([" ".join([str((x+y*10)*25 % 256) for x in range(10)]) for y in range(10)])
with open('./tmp/example.pgm', 'w') as file:
    file.write(pgm_data)

# Create a simple PPM image (10x10 pixels), with a basic color pattern
ppm_data = "P3\n10 10\n255\n"
for y in range(10):
    for x in range(10):
        r = x * 25 % 256
        g = y * 25 % 256
        b = (x + y) * 12.5 % 256
        ppm_data += f"{r} {g} {b} "
    ppm_data += "\n"
with open('./tmp/example.ppm', 'w') as file:
    file.write(ppm_data)

print("PNM files created in ./tmp/")