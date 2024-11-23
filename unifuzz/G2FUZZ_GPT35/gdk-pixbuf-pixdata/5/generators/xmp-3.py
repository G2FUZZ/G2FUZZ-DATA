import os

# Define the content of the xmp file
xmp_content = """
<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c132 79.159725, 2016/09/14-01:09:01        ">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/">
            <xmp:Standardization>XMP follows a standardized format for metadata storage and exchange.</xmp:Standardization>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Save the xmp content to a file
with open('./tmp/metadata.xmp', 'w') as file:
    file.write(xmp_content)

print("XMP file created successfully.")