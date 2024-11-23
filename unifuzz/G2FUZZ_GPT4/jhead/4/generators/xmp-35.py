import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# More complex XMP content with nested structures and custom namespaces
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  
    <!-- Complex Description Block with nested Seq and Bag -->
    <rdf:Description rdf:about=""
        xmlns:xmp="http://ns.adobe.com/xap/1.0/"
        xmlns:dc="http://purl.org/dc/elements/1.1/"
        xmlns:myNS="http://example.com/ns/">
        
        <!-- Standard properties -->
        <xmp:CreatorTool>Adobe Photoshop 23.1.0</xmp:CreatorTool>
        <dc:format>image/jpeg</dc:format>
        
        <!-- Custom Ordered List (Seq) -->
        <myNS:ColorProfiles>
            <rdf:Seq>
                <rdf:li>sRGB</rdf:li>
                <rdf:li>AdobeRGB</rdf:li>
                <rdf:li>ProPhoto RGB</rdf:li>
            </rdf:Seq>
        </myNS:ColorProfiles>
        
        <!-- Custom Unordered List (Bag) -->
        <myNS:Keywords>
            <rdf:Bag>
                <rdf:li>landscape</rdf:li>
                <rdf:li>photography</rdf:li>
                <rdf:li>vacation</rdf:li>
            </rdf:Bag>
        </myNS:Keywords>
        
        <!-- Custom Complex Structure -->
        <myNS:CameraSettings>
            <rdf:Alt>
                <rdf:li xml:lang="x-default">ExposureTime=1/200, FNumber=8.0, ISO=100, FocalLength=50.0mm</rdf:li>
            </rdf:Alt>
        </myNS:CameraSettings>
        
    </rdf:Description>
    
    <!-- Additional Description Blocks can be added here -->
    
  </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Path to the more complex XMP file
file_path = './tmp/more_complex_structure.xmp'

# Write the more complex XMP content to the file
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f'More complex XMP file "{file_path}" has been created successfully.')