import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate XMP file with the specified feature
xmp_content = """
<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:dc="http://purl.org/dc/elements/1.1/">
            <dc:description>
                <rdf:Alt>
                    <rdf:li xml:lang="en">XMP supports multiple languages and character encodings, allowing for the representation of metadata in different languages.</rdf:li>
                    <rdf:li xml:lang="fr">XMP prend en charge plusieurs langues et codages de caractères, permettant la représentation de métadonnées dans différentes langues.</rdf:li>
                </rdf:Alt>
            </dc:description>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

with open('./tmp/feature_xmp.xmp', 'w') as file:
    file.write(xmp_content)

print("XMP file generated successfully.")