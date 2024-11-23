import os

# Generate the XMP content
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
      <rdf:Description rdf:about=""
            xmlns:dc="http://purl.org/dc/elements/1.1/">
         <dc:title>Dublin Core Integration</dc:title>
         <dc:description>XMP incorporates elements from the Dublin Core Metadata Element Set, providing a standardized set of core metadata properties for describing resources.</dc:description>
      </rdf:Description>
   </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create the directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Save the XMP content to a file
with open('./tmp/dublin_core.xmp', 'w') as file:
    file.write(xmp_content)

print("XMP file 'dublin_core.xmp' has been generated and saved in the './tmp/' directory.")