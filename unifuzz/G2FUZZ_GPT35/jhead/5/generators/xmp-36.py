import os

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate XMP file with more complex file structures
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:dc="http://purl.org/dc/elements/1.1/"
            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"
            xmp:CreatorTool="Python"
            xmp:CreateDate="2022-01-01T12:00:00"
            dc:title="Sample Title"
            dc:subject="Sample Subject"
            photoshop:Credit="John Doe"
            photoshop:Country="USA">
            <dc:creator>
                <rdf:Seq>
                    <rdf:li>Author 1</rdf:li>
                    <rdf:li>Author 2</rdf:li>
                </rdf:Seq>
            </dc:creator>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

file_name = 'extended_file.xmp'
file_path = os.path.join(directory, file_name)

with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file '{file_name}' with more complex file structures generated and saved in '{directory}'")