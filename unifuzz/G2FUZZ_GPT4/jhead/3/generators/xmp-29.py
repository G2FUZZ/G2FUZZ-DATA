import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP content with a more complex structure
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"
    xmlns:xmp="http://ns.adobe.com/xap/1.0/"
    xmlns:exif="http://ns.adobe.com/exif/1.0/"
    xmlns:customNS="http://www.example.com/ns/">
   
   <dc:description>
    Complex XMP Example with Multiple Descriptions and Namespaces.
   </dc:description>
   <dc:creator>
    <rdf:Seq>
     <rdf:li>Creator Name</rdf:li>
    </rdf:Seq>
   </dc:creator>
   <photoshop:Headline>A Headline for the Image</photoshop:Headline>
   <xmp:CreateDate>2023-01-01T12:00:00</xmp:CreateDate>
   <exif:ExposureTime>1/60</exif:ExposureTime>
   <exif:FNumber>11.0</exif:FNumber>
   <exif:ISO>100</exif:ISO>
   <customNS:CustomField>Custom Value</customNS:CustomField>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Path to the XMP file to be created
xmp_file_path = './tmp/complex_feature_description.xmp'

# Write the XMP content to the file
with open(xmp_file_path, 'w') as xmp_file:
    xmp_file.write(xmp_content)

print(f"XMP file created at {xmp_file_path}")