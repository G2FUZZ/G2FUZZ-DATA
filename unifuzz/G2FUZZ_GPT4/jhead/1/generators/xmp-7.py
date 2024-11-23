import os
from datetime import datetime

# Ensure ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the XMP content with placeholders for version control
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
        xmlns:dc="http://purl.org/dc/elements/1.1/"
        xmlns:xmp="http://ns.adobe.com/xap/1.0/">
   <dc:format>image/jpeg</dc:format>
   <xmp:ModifyDate>{modify_date}</xmp:ModifyDate>
   <xmp:CreatorTool>Python Script</xmp:CreatorTool>
   <xmp:MetadataDate>{metadata_date}</xmp:MetadataDate>
   <xmp:VersionControl>
    <rdf:Seq>
     <rdf:li>
      <rdf:Description>
       <xmp:version>1.0</xmp:version>
       <xmp:modifier>Author Name</xmp:modifier>
       <xmp:modified>{modified}</xmp:modified>
       <xmp:changeDescription>Initial creation</xmp:changeDescription>
      </rdf:Description>
     </rdf:li>
    </rdf:Seq>
   </xmp:VersionControl>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Set current date and time
current_datetime = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

# Format the XMP content with the current date and time
formatted_xmp_content = xmp_content.format(modify_date=current_datetime, metadata_date=current_datetime, modified=current_datetime)

# Define the file path
file_path = os.path.join(output_dir, 'version_control_metadata.xmp')

# Write the XMP content to a file
with open(file_path, 'w') as file:
    file.write(formatted_xmp_content)

print(f'XMP file created at {file_path}')