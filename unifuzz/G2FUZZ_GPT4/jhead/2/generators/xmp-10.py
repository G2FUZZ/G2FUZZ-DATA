import os
from datetime import datetime

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the XMP content with placeholders for timestamps and version
xmp_content_template = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP toolkit">
   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
      <rdf:Description rdf:about=""
            xmlns:dc="http://purl.org/dc/elements/1.1/"
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            dc:format="application/pdf"
            dc:title="Sample XMP File"
            xmp:CreateDate="{creation_date}"
            xmp:ModifyDate="{modification_date}"
            xmp:Version="{version}">
      </rdf:Description>
   </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Set the creation, modification dates, and version
creation_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
modification_date = creation_date  # Corrected from creation_data to creation_date
version = "1.0"

# Format the XMP content with actual data
xmp_content = xmp_content_template.format(creation_date=creation_date, modification_date=modification_date, version=version)

# Define the file path
file_path = os.path.join(output_dir, 'example.xmp')

# Write the XMP content to a file
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file saved to {file_path}")