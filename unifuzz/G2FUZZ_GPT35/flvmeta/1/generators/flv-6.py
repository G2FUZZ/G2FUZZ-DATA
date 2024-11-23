import os

# Create a directory if it does not exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a sample FLV file with the specified feature
file_content = "FLV files support streaming for progressive download and real-time streaming applications."
file_path = os.path.join(output_dir, 'sample.flv')
with open(file_path, 'w') as file:
    file.write(file_content)

print(f"FLV file generated successfully at: {file_path}")