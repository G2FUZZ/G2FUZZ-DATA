import os

# Define the XMP content
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:custom="http://ns.example.com/custom/">
   <custom:feature>
    Extensibility: XMP is designed to be extended and customized. It allows additional namespaces to be added for 
    specific needs beyond the standard set of metadata properties. This means organizations or industries can 
    define their own schemas to suit their metadata requirements.
   </custom:feature>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Ensure the target directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the output file path
output_file_path = os.path.join(output_dir, 'feature.xmp')

# Write the XMP content to the file
with open(output_file_path, 'w') as file:
    file.write(xmp_content)

print(f'XMP file has been successfully created at {output_file_path}')