import os

# The content to be written to the XMP file
xmp_content = """
<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/">
   <dc:description>
    4. **Embeddability**: XMP can be embedded into the file it describes (such as JPEG, PDF, TIFF, and many others) or stored externally as sidecar files, providing flexibility in managing metadata.
   </dc:description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

# Directory to save the XMP file
output_dir = "./tmp/"
# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# The name of the XMP file
xmp_filename = "feature_description.xmp"

# Full path for the XMP file
xmp_file_path = os.path.join(output_dir, xmp_filename)

# Writing the content to the XMP file
with open(xmp_file_path, "w") as file:
    file.write(xmp_content)

print(f"XMP file saved to: {xmp_file_path}")