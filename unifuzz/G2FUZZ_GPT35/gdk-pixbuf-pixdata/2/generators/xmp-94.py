import os

# Define the content for the XMP files with more complex structures
xmp_content_complex = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:custom="http://example.com/custom/">
            <custom:extensibility>XMP files allow for the addition of custom metadata properties to suit specific needs or requirements.</custom:extensibility>
            <custom:creator>
                <rdf:Seq>
                    <rdf:li>John Doe</rdf:li>
                    <rdf:li>Jane Smith</rdf:li>
                </rdf:Seq>
            </custom:creator>
            <custom:location>
                <custom:latitude>40.7128</custom:latitude>
                <custom:longitude>-74.0060</custom:longitude>
            </custom:location>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create a directory to save the XMP files if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the XMP files with the defined complex content
for i in range(3):  # Generating 3 XMP files
    file_name = f'{directory}file_complex_{i+1}.xmp'
    with open(file_name, 'w') as file:
        file.write(xmp_content_complex)

print("XMP files with more complex structures generated successfully.")