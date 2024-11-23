import os

def generate_pnm_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

features = "8. Simple Structure: 'pnm' files have a simple structure, making them easy to parse and manipulate programmatically."

file_name = './tmp/generated_file.pnm'
generate_pnm_file(file_name, features)

print(f"Generated 'pnm' file saved at: {file_name}")