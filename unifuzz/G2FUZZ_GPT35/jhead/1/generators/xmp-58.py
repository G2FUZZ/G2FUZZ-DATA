import os

# Define the XML structure for metadata information
xml_template = '''<?xml version="1.0" encoding="UTF-8"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c132 79.159624, 2019/11/13-01:06:43">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
    <rdf:Description rdf:about=""
        xmlns:dc="http://purl.org/dc/elements/1.1/"
        xmlns:xmp="http://ns.adobe.com/xap/1.0/"
        xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/">
      <dc:title><rdf:Alt><rdf:li xml:lang="x-default">Sample Title</rdf:li></rdf:Alt></dc:title>
      <dc:description><rdf:Alt><rdf:li xml:lang="x-default">Sample Description</rdf:li></rdf:Alt></dc:description>
      <dc:creator><rdf:Seq><rdf:li>John Doe</rdf:li></rdf:Seq></dc:creator>
      <dc:date>2022-01-01</dc:date>
    </rdf:Description>
  </rdf:RDF>
</x:xmpmeta>'''

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate xmp files with the given XML template
num_files = 5

for i in range(num_files):
    with open(f'./tmp/file_{i}.xmp', 'w') as file:
        file.write(xml_template)

print(f'{num_files} xmp files generated and saved in ./tmp/')