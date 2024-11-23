from lxml import etree
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP template with more complex features
xmp_template = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c014 79.159824, 2016/09/14-01:09:01">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
             xmlns:dc="http://purl.org/dc/elements/1.1/"
             xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/"
             xmlns:cc="http://creativecommons.org/ns#"
             xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"
             xmlns:tiff="http://ns.adobe.com/tiff/1.0/"
             xmlns:exif="http://ns.adobe.com/exif/1.0/">
        <rdf:Description rdf:about=""
                         dc:creator="Jane Doe"
                         dc:title="Example Image"
                         dc:description="An example image with complex XMP metadata"
                         photoshop:Credit="Jane Doe Photography"
                         photoshop:Source="https://example.com"
                         tiff:Make="Example Camera Brand"
                         tiff:Model="Example Camera Model"
                         exif:ExposureTime="1/60"
                         exif:FNumber="8.0"
                         exif:ISOSpeedRatings="100">
            <dc:rights>
                <rdf:Alt>
                    <rdf:li xml:lang="x-default">Creative Commons Attribution 4.0 International License</rdf:li>
                    <rdf:li xml:lang="x-default">GNU General Public License</rdf:li>
                </rdf:Alt>
            </dc:rights>
            <xmpRights:UsageTerms>
                <rdf:Alt>
                    <rdf:li xml:lang="x-default">This work is licensed under a Creative Commons Attribution 4.0 International License.</rdf:li>
                    <rdf:li xml:lang="x-default">This work is also licensed under the GNU General Public License.</rdf:li>
                </rdf:Alt>
            </xmpRights:UsageTerms>
            <xmpRights:WebStatement>http://creativecommons.org/licenses/by/4.0/</xmpRights:WebStatement>
            <cc:license rdf:resource="http://creativecommons.org/licenses/by/4.0/" />
            <cc:license rdf:resource="http://www.gnu.org/licenses/gpl.html" />
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Parse the XMP template
xmp_data = etree.fromstring(xmp_template)

# Write the XMP data to a file
xmp_file_path = './tmp/complex_licensing_info.xmp'
with open(xmp_file_path, 'wb') as f:
    f.write(etree.tostring(xmp_data, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

print(f"XMP file with complex metadata saved to {xmp_file_path}")