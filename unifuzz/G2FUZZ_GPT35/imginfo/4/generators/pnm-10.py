# Generate PNM file content
pnm_content = """P3
# Example PNM file
3 2
255
255 0 0
0 255 0
0 0 255
255 255 0
255 255 255
0 0 0
"""

# Save PNM file to ./tmp/example.pnm
file_path = "./tmp/example.pnm"
with open(file_path, "w") as file:
    file.write(pnm_content)