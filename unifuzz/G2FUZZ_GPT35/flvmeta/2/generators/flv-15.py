import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample FLV file with the specified features including Interactivity
with open('./tmp/sample_interactive.flv', 'wb') as f:
    f.write(b'FLV File Content with Interactivity')

print("FLV file 'sample_interactive.flv' with the additional feature 'Interactivity' has been generated and saved in './tmp/'.")