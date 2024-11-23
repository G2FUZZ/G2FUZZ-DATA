import os

# Define the content for the XMP files
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:custom="http://example.com/custom/">
            <custom:extensibility>XMP files allow for the addition of custom metadata properties to suit specific needs or requirements.</custom:extensibility>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create a directory to save the XMP files if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the XMP files with the defined content
for i in range(3):  # Generating 3 XMP files
    file_name = f'{directory}file_{i+1}.xmp'
    with open(file_name, 'w') as file:
        file.write(xmp_content)

print("XMP files generated successfully.")