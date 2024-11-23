import os

def generate_pnm_file():
    header = "P3\n800 600\n255\n"  # P3 format with resolution 800x600 and max color value 255

    # Generating pixel values with a gradient effect
    pixels = ""
    for y in range(600):
        for x in range(800):
            r = int((x / 800) * 255)
            g = int((y / 600) * 255)
            b = int((x*y / (800*600)) * 255)
            pixels += f"{r} {g} {b} "

    content = header + pixels

    # Adding comment lines to the PNM file
    comments = "# Example PNM file\n# Generated using Python\n"
    content = comments + content

    with open("./tmp/example_extended.pnm", "w") as file:
        file.write(content)

if not os.path.exists("./tmp"):
    os.makedirs("./tmp")

generate_pnm_file()