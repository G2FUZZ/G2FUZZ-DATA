import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Content to be written to the XMP file
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c014 79.159824, 2016/09/14-01:09:01        ">
   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
      <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/">
         <xmp:CreatorTool>Python Script</xmp:CreatorTool>
         <xmp:CreateDate>2023-01-01T12:00:00</xmp:CreateDate>
         <xmp:MetadataDate>2023-01-01T12:00:00</xmp:MetadataDate>
         <xmp:ModifyDate>2023-01-01T12:00:00</xmp:ModifyDate>
         <!-- Custom metadata field representing RDF-based feature -->
         <xmp:CustomField>RDF-based: XMP is based on the Resource Description Framework (RDF), a standard model for data interchange on the web. RDF provides a consistent way to represent metadata about resources in a way that can be easily parsed and understood by software.</xmp:CustomField>
      </rdf:Description>
   </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# File path for the XMP file to be saved
xmp_file_path = os.path.join(output_dir, "example.xmp")

# Writing the content to the XMP file
with open(xmp_file_path, "w") as file:
    file.write(xmp_content)

print(f"XMP file has been saved to {xmp_file_path}")