import os
from datetime import datetime

# Ensuring the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to generate XMP content with advanced features
def generate_xmp_content(creator_list, title, description, copyright, license_url):
    creator_elements = ''.join([f'    <dc:creator><rdf:Seq><rdf:li>{creator}</rdf:li></rdf:Seq></dc:creator>\n' for creator in creator_list])
    xmp_content = f'''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
          xmlns:dc="http://purl.org/dc/elements/1.1/"
          xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/">
  <rdf:Description rdf:about=""
    xmlns:xmp="http://ns.adobe.com/xap/1.0/"
    xmlns:myNS="http://example.com/ns/">
   <xmp:CreatorTool>Advanced Example Tool</xmp:CreatorTool>
   <xmp:CreateDate>{datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}</xmp:CreateDate>
   <xmp:ModifyDate>{datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}</xmp:ModifyDate>
   <xmp:MetadataDate>{datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}</xmp:MetadataDate>
{creator_elements}
   <dc:title>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">{title}</rdf:li>
    </rdf:Alt>
   </dc:title>
   <dc:description>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">{description}</rdf:li>
    </rdf:Alt>
   </dc:description>
   <xmpRights:UsageTerms>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">{copyright}</rdf:li>
    </rdf:Alt>
   </xmpRights:UsageTerms>
   <xmpRights:WebStatement>{license_url}</xmpRights:WebStatement>
   <myNS:CustomFeature>Custom Value</myNS:CustomFeature>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''
    return xmp_content

# Example usage of the function
creator_list = ['Creator One', 'Creator Two']
title = "Advanced XMP Example"
description = "This is an example of a more complex XMP file with advanced features."
copyright = "© 2023 Creator One and Creator Two. All rights reserved."
license_url = "http://creativecommons.org/licenses/by-nc/4.0/"

xmp_content = generate_xmp_content(creator_list, title, description, copyright, license_url)

# File path for the XMP file
file_path = os.path.join(output_dir, 'advanced_feature.xmp')

# Writing the XMP content to the file
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f'XMP file created at {file_path}')