import os

def create_pnm_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

# Create P1 PNM file
p1_content = "P1\n# This is a P1 PNM file\n2 2\n1 0\n0 1"
p1_file_path = './tmp/p1_file.pnm'
create_pnm_file(p1_file_path, p1_content)

# Create P2 PNM file
p2_content = "P2\n# This is a P2 PNM file\n2 2\n255\n0 128\n64 192"
p2_file_path = './tmp/p2_file.pnm'
create_pnm_file(p2_file_path, p2_content)

# Create P3 PNM file
p3_content = "P3\n# This is a P3 PNM file\n2 2\n255\n255 0 0\n0 255 0\n0 0 255"
p3_file_path = './tmp/p3_file.pnm'
create_pnm_file(p3_file_path, p3_content)

print("PNM files created and saved in ./tmp/ directory.")