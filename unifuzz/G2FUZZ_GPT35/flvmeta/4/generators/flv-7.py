import os

# Function to generate FLV files
def generate_flv_file(file_path, feature):
    with open(file_path, 'w') as file:
        file.write(f"FLV File\nFeature: {feature}")

# Create tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV file with the specified feature
feature = "Compatibility: FLV files are widely supported across different platforms and media players."
file_path = './tmp/sample.flv'
generate_flv_file(file_path, feature)

print(f"FLV file generated with the feature: {feature}")