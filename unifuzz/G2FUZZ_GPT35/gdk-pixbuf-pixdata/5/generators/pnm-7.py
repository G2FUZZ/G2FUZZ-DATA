import os

# Create a directory to store the generated PNM files
os.makedirs('./tmp/', exist_ok=True)

# Generate a PNM file with the provided feature
pnm_content = """P3
# Simple Structure
2 2
255
255 0 0 0 255 0
0 0 255 255 255 255
"""
with open('./tmp/simple_structure.pnm', 'w') as f:
    f.write(pnm_content)

print("PNM file with simple structure generated and saved as './tmp/simple_structure.pnm'")