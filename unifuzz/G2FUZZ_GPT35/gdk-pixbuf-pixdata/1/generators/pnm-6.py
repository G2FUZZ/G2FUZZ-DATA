import os

def generate_pnm_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

content = """P3
# Platform Independence: PNM files are platform-independent and can be easily viewed and manipulated across different operating systems and software applications.
2 2
255
255 255 255
0 0 0
"""
filename = './tmp/platform_independence.pnm'

generate_pnm_file(content, filename)