import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Create a sample XMP file with multiple RDF Descriptions
xmp_content = """
<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
 <x:xmpmeta xmlns:x="adobe:ns:meta/">
   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
     <rdf:Description rdf:about=""
           xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/">
       <xmpRights:Marked>True</xmpRights:Marked>
     </rdf:Description>
     <rdf:Description rdf:about=""
           xmlns:dc="http://purl.org/dc/elements/1.1/">
       <dc:title>Sample Title</dc:title>
       <dc:creator>John Doe</dc:creator>
     </rdf:Description>
     <rdf:Description rdf:about=""
           xmlns:custom="http://example.com/custom/">
       <custom:customField1>Value 1</custom:customField1>
       <custom:customField2>Value 2</custom:customField2>
     </rdf:Description>
   </rdf:RDF>
 </x:xmpmeta>
<?xpacket end="w"?>
"""

# Save the extended XMP file
with open('./tmp/sample_extended.xmp', 'w') as file:
    file.write(xmp_content)