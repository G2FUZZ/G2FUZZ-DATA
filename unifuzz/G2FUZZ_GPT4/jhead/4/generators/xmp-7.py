import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# XMP content with the feature description
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
    <rdf:Description rdf:about=""
        xmlns:xmp="http://ns.adobe.com/xap/1.0/">
        <xmp:FeatureDescription>
            7. **Synchronization**: XMP allows for the synchronization of metadata across different file versions and derivatives. If a file is edited or transformed, the XMP metadata can be updated to reflect these changes, ensuring that metadata remains accurate and relevant.
        </xmp:FeatureDescription>
    </rdf:Description>
  </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Path to the XMP file
file_path = './tmp/feature_description.xmp'

# Write the XMP content to the file
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f'XMP file "{file_path}" has been created successfully.')