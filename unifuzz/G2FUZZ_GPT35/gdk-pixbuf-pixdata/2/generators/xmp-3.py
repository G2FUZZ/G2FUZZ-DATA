import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate xmp files with the specified feature
for i in range(5):  # Generate 5 xmp files
    file_content = """<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/'>
    <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
        <rdf:Description rdf:about=''>
            <xmp:Standardization>{}</xmp:Standardization>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>""".format("XMP files adhere to standardized schemas and namespaces, ensuring consistency and interoperability across different applications and platforms.")

    file_path = os.path.join(directory, 'file_{}.xmp'.format(i))
    with open(file_path, 'w') as file:
        file.write(file_content)

print("XMP files generated successfully in the './tmp/' directory.")