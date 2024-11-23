import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the XMP file
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c015 91.163494, 2019/02/06-16:13:26        ">
   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
      <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/">
         <xmp:CreatorTool>Python Script</xmp:CreatorTool>
         <xmp:CreateDate>2023-01-01T12:00:00</xmp:CreateDate>
         <xmp:ModifyDate>2023-01-01T12:00:00</xmp:ModifyDate>
         <xmp:MetadataDate>2023-01-01T12:00:00</xmp:MetadataDate>
         <xmp:Description>3. **Extensibility**: XMP is designed to be extensible, allowing users and organizations to define additional metadata fields beyond the standard set. This feature enables the customization of metadata to meet specific needs or industry standards.</xmp:Description>
      </rdf:Description>
   </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
'''

# Define the path to the XMP file
xmp_file_path = './tmp/feature_description.xmp'

# Write the content to the XMP file
with open(xmp_file_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file saved at: {xmp_file_path}")