import os

# Create the directory if it doesn't exist
directory = './tmp'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate XMP files with custom schemas, complex features, embedded images, and geospatial metadata
xmp_content = """
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:custom="http://example.com/custom/">
            <custom:customProperties>
                <rdf:Bag>
                    <rdf:li>
                        <custom:propertyName>Property 1</custom:propertyName>
                        <custom:propertyValue>Value 1</custom:propertyValue>
                    </rdf:li>
                    <rdf:li>
                        <custom:propertyName>Property 2</custom:propertyName>
                        <custom:propertyValue>Value 2</custom:propertyValue>
                    </rdf:li>
                </rdf:Bag>
            </custom:customProperties>
            <custom:nestedProperties>
                <rdf:Description>
                    <custom:nestedProperty1>Nested Value 1</custom:nestedProperty1>
                    <custom:nestedProperty2>Nested Value 2</custom:nestedProperty2>
                </rdf:Description>
            </custom:nestedProperties>
            <custom:embeddedImage>
                <rdf:Description>
                    <custom:imageWidth>800</custom:imageWidth>
                    <custom:imageHeight>600</custom:imageHeight>
                    <custom:imageFormat>JPEG</custom:imageFormat>
                    <custom:imageData>Base64EncodedImageDataHere</custom:imageData>
                </rdf:Description>
            </custom:embeddedImage>
            <custom:geospatialMetadata>
                <rdf:Description>
                    <custom:latitude>37.7749</custom:latitude>
                    <custom:longitude>-122.4194</custom:longitude>
                    <custom:altitude>10</custom:altitude>
                </rdf:Description>
            </custom:geospatialMetadata>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
"""

for i in range(3):  # Generate 3 XMP files with custom schemas, complex features, embedded images, and geospatial metadata
    filename = f'{directory}/custom_metadata_{i + 1}.xmp'
    with open(filename, 'w') as file:
        file.write(xmp_content)

print("XMP files with custom schemas, complex features, embedded images, and geospatial metadata generated successfully in the ./tmp/ directory.")