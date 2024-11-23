import os

# Define the content for the XMP file with more complex file structures
xmp_content_complex = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
             xmlns:exif="http://ns.adobe.com/exif/1.0/"
             xmlns:xmp="http://ns.adobe.com/xap/1.0/"
             xmlns:tiff="http://ns.adobe.com/tiff/1.0/">
        <rdf:Description rdf:about=""
            xmlns:dc="http://purl.org/dc/elements/1.1/"
            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">
            <dc:title>Sample Image</dc:title>
            <dc:creator>John Doe</dc:creator>
            <dc:description>A sample image with complex metadata.</dc:description>
            <exif:PixelXDimension>800</exif:PixelXDimension>
            <exif:PixelYDimension>600</exif:PixelYDimension>
            <tiff:ImageWidth>800</tiff:ImageWidth>
            <tiff:ImageLength>600</tiff:ImageLength>
            <photoshop:CaptionWriter>Jane Smith</photoshop:CaptionWriter>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Write the content to the XMP file with complex file structures
with open('./tmp/complex_metadata.xmp', 'w') as file:
    file.write(xmp_content_complex)

print("XMP file with complex metadata information created at ./tmp/complex_metadata.xmp")