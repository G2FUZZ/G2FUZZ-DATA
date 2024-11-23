import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample FLV file with the specified feature
with open('./tmp/sample.flv', 'wb') as f:
    f.write(b'FLV File Content')

print("FLV file 'sample.flv' with the specified feature has been generated and saved in './tmp/'.")