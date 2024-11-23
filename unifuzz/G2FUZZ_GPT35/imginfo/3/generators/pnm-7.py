import os

def generate_pnm_files():
    # Create directory if it doesn't exist
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')
    
    # Generate PNM file with specific content
    content = "P3\n3 2\n255\n255 0 0 0 255 0 0 0 255\n"
    with open('./tmp/image.pnm', 'w') as f:
        f.write(content)

generate_pnm_files()