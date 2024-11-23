import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Complex XMP content with multiple feature descriptions and namespaces
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  
    <!-- First Description Block -->
    <rdf:Description rdf:about=""
        xmlns:xmp="http://ns.adobe.com/xap/1.0/"
        xmlns:dc="http://purl.org/dc/elements/1.1/"
        xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">
        <xmp:CreatorTool>Adobe Photoshop 23.1.0</xmp:CreatorTool>
        <dc:format>image/jpeg</dc:format>
        <photoshop:Credit>Photographer Name</photoshop:Credit>
    </rdf:Description>
    
    <!-- Second Description Block -->
    <rdf:Description rdf:about=""
        xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/"
        xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/">
        <xmpRights:UsageTerms>
            This work is licensed under a Creative Commons Attribution 4.0 International License.
        </xmpRights:UsageTerms>
        <xmpMM:DocumentID>uuid:12345678-1234-1234-1234-123456789012</xmpMM:DocumentID>
    </rdf:Description>
    
    <!-- Third Description Block -->
    <rdf:Description rdf:about=""
        xmlns:exif="http://ns.adobe.com/exif/1.0/">
        <exif:ExposureTime>1/200</exif:ExposureTime>
        <exif:FNumber>8.0</exif:FNumber>
        <exif:ISO>100</exif:ISO>
        <exif:FocalLength>50.0 mm</exif:FocalLength>
    </rdf:Description>
    
  </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Path to the complex XMP file
file_path = './tmp/complex_feature_description.xmp'

# Write the complex XMP content to the file
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f'Complex XMP file "{file_path}" has been created successfully.')