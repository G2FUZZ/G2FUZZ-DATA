import os

def generate_pnm_file():
    file_content = "6. Platform Independence: PNM files are platform-independent and can be easily transferred between different systems."
    file_path = './tmp/platform_independence.pnm'
    
    with open(file_path, 'w') as file:
        file.write(file_content)
    
    print(f"PNM file generated and saved at: {file_path}")

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

generate_pnm_file()