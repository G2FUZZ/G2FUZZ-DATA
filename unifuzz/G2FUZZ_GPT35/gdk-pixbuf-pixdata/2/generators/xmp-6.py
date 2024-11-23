import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate xmp files with localization feature
for language in ['en', 'fr', 'es', 'de']:
    filename = f'./tmp/metadata_{language}.xmp'
    with open(filename, 'w') as file:
        file.write(f'<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.4-c005 1.1.0">\n')
        file.write(f'    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n')
        file.write(f'        <rdf:Description rdf:about="" xmlns:dc="http://purl.org/dc/elements/1.1/">\n')
        file.write(f'            <dc:title>\n')
        file.write(f'                <rdf:Alt>\n')
        file.write(f'                    <rdf:li xml:lang="{language}">Localization: XMP metadata can be localized to support multiple languages and regions for global content distribution.</rdf:li>\n')
        file.write(f'                </rdf:Alt>\n')
        file.write(f'            </dc:title>\n')
        file.write(f'        </rdf:Description>\n')
        file.write(f'    </rdf:RDF>\n')
        file.write(f'</x:xmpmeta>\n')

    print(f'Generated {filename}')