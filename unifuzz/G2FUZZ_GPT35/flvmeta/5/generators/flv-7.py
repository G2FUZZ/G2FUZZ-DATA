import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a simple FLV file with a comment indicating compatibility
with open('./tmp/compatibility.flv', 'wb') as file:
    comment = b'FLV files are widely supported by media players and web browsers.'
    file.write(comment)

print('FLV file with compatibility feature generated successfully.')