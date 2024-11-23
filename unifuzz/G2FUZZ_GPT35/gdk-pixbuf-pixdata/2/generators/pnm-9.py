def generate_pnm_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

pnm_content = '''P3
# Compatibility: PNM files are widely supported across different platforms and software applications.
2 2
255
255 0 0
0 255 0
0 0 255
255 255 0
'''

file_path = './tmp/sample.pnm'
generate_pnm_file(file_path, pnm_content)