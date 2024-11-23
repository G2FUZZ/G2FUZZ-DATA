import os

# Create a directory for storing generated xmp files
os.makedirs('./tmp/', exist_ok=True)

# Define the content for the xmp file with additional complex features
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:custom="http://example.com/custom/">
            <custom:extensibility>XMP allows for custom schemas and properties to be defined and stored within the file.</custom:extensibility>
            <custom:complex_property>
                <custom:nested_property>A nested property value</custom:nested_property>
                <custom:array_property>
                    <custom:item>Item 1</custom:item>
                    <custom:item>Item 2</custom:item>
                </custom:array_property>
            </custom:complex_property>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Save the extended xmp file
with open('./tmp/extended_custom_xmp_file.xmp', 'w') as file:
    file.write(xmp_content)