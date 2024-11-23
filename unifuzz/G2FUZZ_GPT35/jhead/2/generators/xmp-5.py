import os

# Define the content of the XMP file
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
	<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
		<rdf:Description rdf:about=""
			xmlns:xmp="http://ns.adobe.com/xap/1.0/"
			xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/"
			xmlns:dc="http://purl.org/dc/elements/1.1/">
			<xmp:ModifyDate>2021-12-01T12:00:00</xmp:ModifyDate>
			<dc:format>image/jpeg</dc:format>
			<xmpRights:Marked>True</xmpRights:Marked>
			<xmpRights:WebStatement>https://www.example.com/rights</xmpRights:WebStatement>
			<xmpRights:UsageTerms>Embeddable: XMP metadata can be embedded within the associated file, such as images, videos, and documents, allowing for easy access and sharing of metadata along with the content.</xmpRights:UsageTerms>
		</rdf:Description>
	</rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create the tmp directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Save the XMP file to ./tmp/
with open('./tmp/metadata.xmp', 'w') as file:
    file.write(xmp_content)

print("XMP file generated and saved successfully.")