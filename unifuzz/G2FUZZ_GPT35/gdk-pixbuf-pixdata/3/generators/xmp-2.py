import os

# Define the content for the XMP file
xmp_content = """
<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:custom="http://www.example.com/custom/"
            custom:customField1="value1"
            custom:customField2="value2">
            <custom:customField3>value3</custom:customField3>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

# Create a directory if it doesn't exist
os.makedirs("./tmp/", exist_ok=True)

# Write the XMP content to a file in the tmp directory
with open("./tmp/custom_metadata.xmp", "w") as f:
    f.write(xmp_content)

print("XMP file with custom metadata fields generated successfully.")