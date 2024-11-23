import os

# Define the metadata content
metadata_content = """
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:xmp="http://ns.adobe.com/xap/1.0/">
    <xmp:Searchability>XMP metadata can enhance the searchability of files by providing additional information for indexing and retrieval.</xmp:Searchability>
  </rdf:Description>
</rdf:RDF>
"""

# Create a directory if it doesn't exist
directory = './tmp/'
os.makedirs(directory, exist_ok=True)

# Generate XMP files
for i in range(5):
    file_name = f'{directory}file_{i}.xmp'
    with open(file_name, 'w') as file:
        file.write(metadata_content)

print("XMP files generated successfully.")