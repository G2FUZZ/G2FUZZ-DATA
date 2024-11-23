import os

# Define the content for the XMP file with additional features
xmp_content_extended = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:dc="http://purl.org/dc/elements/1.1/">
            <dc:description>Accessibility: XMP files can store accessibility information to improve the usability and availability of content for users with disabilities.</dc:description>
        </rdf:Description>
        <rdf:Description rdf:about=""
            xmlns:custom="http://example.com/custom/namespace">
            <custom:feature1>Custom feature 1</custom:feature1>
            <custom:feature2>Custom feature 2</custom:feature2>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Write the content to the extended XMP file
with open('./tmp/accessibility_info_extended.xmp', 'w') as file:
    file.write(xmp_content_extended)

print("Extended XMP file with additional features created at ./tmp/accessibility_info_extended.xmp")