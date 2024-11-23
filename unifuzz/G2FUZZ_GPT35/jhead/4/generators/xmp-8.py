import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate xmp files with the given feature
feature = "Versioning: XMP allows for versioning of metadata to track changes and updates over time."
for i in range(3):
    with open(f'./tmp/file_{i + 1}.xmp', 'w') as file:
        file.write(f'<x:xmpmeta><rdf:RDF><rdf:Description>{feature}</rdf:Description></rdf:RDF></x:xmpmeta>')