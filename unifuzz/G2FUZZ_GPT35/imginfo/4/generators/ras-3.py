import os

features = {
    'Color Depth': ['monochrome', 'grayscale', 'full color']
}

output_dir = './tmp/'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for feature, values in features.items():
    filename = f'{feature.replace(" ", "_").lower()}.ras'
    with open(os.path.join(output_dir, filename), 'w') as file:
        file.write(f'{feature}:\n')
        for value in values:
            file.write(f'- {value}\n')