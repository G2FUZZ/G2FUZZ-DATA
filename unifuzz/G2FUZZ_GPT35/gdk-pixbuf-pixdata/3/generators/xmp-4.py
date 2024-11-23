import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate xmp files with the specified feature
xmp_content = """<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/'>
    <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
        <rdf:Description rdf:about=''>
            <xmp:Standardization>XMP is an ISO standard (ISO 16684-1), ensuring compatibility and interoperability across different software applications and platforms.</xmp:Standardization>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>"""

# Save the generated xmp file
file_path = './tmp/standardization.xmp'
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file saved at: {file_path}")