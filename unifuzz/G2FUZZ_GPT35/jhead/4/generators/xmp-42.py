import os

# Create a directory to store the xmp files
os.makedirs('./tmp/', exist_ok=True)

# Generate xmp file with additional complex features
xmp_content = """
<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/'>
    <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
        <rdf:Description rdf:about='' xmlns:xmpRights='http://ns.adobe.com/xap/1.0/rights/'>
            <xmpRights:UsageTerms>XMP can include rights-related information like usage terms and licensing details.</xmpRights:UsageTerms>
        </rdf:Description>
        <rdf:Description rdf:about='' xmlns:dc='http://purl.org/dc/elements/1.1/'>
            <dc:title>Sample Title</dc:title>
            <dc:creator>John Doe</dc:creator>
            <dc:description>This is a sample description.</dc:description>
            <dc:publisher>Publisher Name</dc:publisher>
        </rdf:Description>
        <rdf:Description rdf:about='' xmlns:custom='http://example.com/custom/'>
            <custom:customField1>Custom Value 1</custom:customField1>
            <custom:customField2>Custom Value 2</custom:customField2>
            <custom:nestedArray>
                <rdf:Bag>
                    <rdf:li>Array Item 1</rdf:li>
                    <rdf:li>Array Item 2</rdf:li>
                    <rdf:li>Array Item 3</rdf:li>
                </rdf:Bag>
            </custom:nestedArray>
        </rdf:Description>
        <rdf:Description rdf:about='' xmlns:exif='http://ns.adobe.com/exif/1.0/'>
            <exif:DateTimeOriginal>2022-01-01T12:00:00</exif:DateTimeOriginal>
            <exif:ExposureTime>1/60</exif:ExposureTime>
        </rdf:Description>
        <rdf:Description rdf:about='' xmlns:custom2='http://example.com/custom2/'>
            <custom2:complexField>
                <custom2:subField1>Subfield Value 1</custom2:subField1>
                <custom2:subField2>Subfield Value 2</custom2:subField2>
            </custom2:complexField>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>
"""

# Save the generated xmp file
with open('./tmp/extended_xmp_file_more_complex.xmp', 'w') as file:
    file.write(xmp_content)

print("Extended XMP file with even more complex features generated and saved successfully.")