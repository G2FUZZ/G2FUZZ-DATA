import os

# Create a directory to store the generated files
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

def generate_pixdata_files():
    features = {
        'Data encoding': 'raw'
    }

    for feature, value in features.items():
        filename = f'{feature.lower().replace(" ", "_")}.txt'
        with open(os.path.join(output_dir, filename), 'w') as f:
            f.write(f'{feature}: {value}')

generate_pixdata_files()