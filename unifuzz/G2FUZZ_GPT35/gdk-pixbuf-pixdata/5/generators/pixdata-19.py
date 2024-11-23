import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate pixdata files containing the specified features
features = ['19. Custom extensions: Additional features or fields added by specific applications or developers.']

for i in range(5):
    with open(f'./tmp/pixdata_{i}.txt', 'w') as file:
        for feature in features:
            file.write(feature + '\n')

print("Generated pixdata files saved in ./tmp/ directory.")