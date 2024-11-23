import os

def generate_pnm_file(metadata):
    file_name = os.path.join('./tmp/', 'generated_image.pnm')
    with open(file_name, 'w') as file:
        file.write(f'P3\n#{metadata}\n5 5\n255\n')
        for _ in range(5):
            for _ in range(5):
                file.write('255 0 0 ')
            file.write('\n')
    
metadata = 'Metadata: PNM files may contain optional metadata such as image dimensions and comments.'
generate_pnm_file(metadata)