import os

# Define the directory for saving the XMP files
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# XMP content with multilingual support
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/">
   <dc:title>
    <rdf:Alt>
     <rdf:li xml:lang="en">Example Title in English</rdf:li>
     <rdf:li xml:lang="fr">Exemple de Titre en Français</rdf:li>
    </rdf:Alt>
   </dc:title>
   <dc:description>
    <rdf:Alt>
     <rdf:li xml:lang="en">This is an example description in English, showcasing multilingual support in XMP files.</rdf:li>
     <rdf:li xml:lang="fr">Ceci est un exemple de description en français, illustrant le support multilingue dans les fichiers XMP.</rdf:li>
    </rdf:Alt>
   </dc:description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# File path for the new XMP file
xmp_file_path = os.path.join(output_dir, 'example_multilingual.xmp')

# Write the XMP content to the file
with open(xmp_file_path, 'w', encoding='utf-8') as file:
    file.write(xmp_content)

print(f'XMP file with multilingual support created at: {xmp_file_path}')