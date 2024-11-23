import numpy as np

def generate_pnm_file(file_name, message):
    with open(file_name, 'w') as file:
        file.write(message)

file_name = './tmp/platform_independence.pnm'
message = "Platform Independence: PNM files are platform-independent and can be easily transferred between different systems."

generate_pnm_file(file_name, message)