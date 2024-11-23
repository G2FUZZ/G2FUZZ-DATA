import os

# Create a directory to store the generated FLV files if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with small file sizes and multi-language support
file_sizes = [100, 200, 150, 180, 120]  # in KB
languages = ['English', 'Spanish', 'French', 'German', 'Chinese']

for idx, (size, language) in enumerate(zip(file_sizes, languages)):
    with open(f'./tmp/video_{idx}.flv', 'wb') as f:
        # Write dummy data to create a file with the specified size
        f.write(b'\0' * size * 1024)
        
        # Add multi-language support information to the FLV file
        metadata = f'Multi-language Support: {language}'
        f.write(metadata.encode())

print("FLV files with small file sizes and multi-language support have been generated and saved in the './tmp/' directory.")