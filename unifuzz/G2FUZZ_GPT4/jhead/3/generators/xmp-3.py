import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the content of the XMP file
xmp_content = """
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:xmp="http://ns.adobe.com/xap/1.0/">
    <xmp:Interoperability>XMP enables the exchange of metadata across different applications, devices, and platforms without loss of information, facilitating a seamless workflow between different systems and software.</xmp:Interoperability>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
"""

# Define the filename
file_name = 'feature_description.xmp'

# Full path for the file
file_path = os.path.join(output_dir, file_name)

# Writing the XMP content to the file
with open(file_path, 'w') as file:
    file.write(xmp_content.strip())

print(f"XMP file '{file_name}' has been created in '{output_dir}'.")