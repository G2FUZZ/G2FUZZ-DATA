import os
from xml.dom import minidom

# Create a function to generate XMP files
def generate_xmp_file(metadata):
    xmp_file = minidom.Document()
    
    # Create root node
    rdf = xmp_file.createElement('rdf:RDF')
    rdf.setAttribute('xmlns:rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
    xmp_file.appendChild(rdf)
    
    # Create Description node
    desc = xmp_file.createElement('rdf:Description')
    rdf.appendChild(desc)
    
    # Add metadata properties
    for key, value in metadata.items():
        desc.setAttribute(key, value)
    
    return xmp_file.toprettyxml()

# Define metadata for XMP file
metadata = {
    'Author': 'John Doe',
    'Title': 'Sample Document',
    'Keywords': 'Python, XMP, Metadata',
    'Copyright': '2022, John Doe'
}

# Generate XMP file content
xmp_content = generate_xmp_file(metadata)

# Save XMP file to './tmp/sample.xmp'
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

file_path = os.path.join(output_dir, 'sample.xmp')
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f'XMP file generated and saved at: {file_path}')