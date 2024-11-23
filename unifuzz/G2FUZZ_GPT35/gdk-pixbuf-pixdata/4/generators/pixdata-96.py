import os
import random
import time

# Create a directory to store the generated files
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

def generate_pixdata_files():
    features = {
        'Data encoding': ['raw', 'compressed', 'encrypted'],
        'File size': [1024, 2048, 4096],
        'Timestamp': time.strftime("%Y-%m-%d %H:%M:%S")
    }

    for feature, values in features.items():
        for value in values:
            if isinstance(value, int):
                value_str = f'{value} KB'
            else:
                value_str = value

            filename = f'{feature.lower().replace(" ", "_")}_{str(value).lower()}.txt'
            with open(os.path.join(output_dir, filename), 'w') as f:
                f.write(f'{feature}: {value_str}')

generate_pixdata_files()