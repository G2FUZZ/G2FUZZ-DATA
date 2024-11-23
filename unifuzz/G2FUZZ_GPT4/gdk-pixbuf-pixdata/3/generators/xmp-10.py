import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP content with Accessibility Features
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/">
   <dc:description>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">Image of a sunset over the mountains, providing a serene and colorful view. This image aims to be accessible to users with visual impairments by offering descriptive text.</rdf:li>
    </rdf:Alt>
   </dc:description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Define the file path
file_path = './tmp/accessibility_features.xmp'

# Write the XMP content to the file
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f'XMP file with accessibility features created at: {file_path}')