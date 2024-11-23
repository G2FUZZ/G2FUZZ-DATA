import os
from datetime import datetime

def ensure_directory_exists(directory_path):
    """
    Ensures the specified directory exists.
    """
    os.makedirs(directory_path, exist_ok=True)

def generate_xmp_content(creator_tool, metadata_dict, custom_fields):
    """
    Generates XMP content with dynamic dates and custom fields.
    """
    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    xmp_template = f"""<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="{creator_tool}">
   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
      <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:dc="http://purl.org/dc/elements/1.1/"
            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"
            xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/">
         <xmp:CreateDate>{metadata_dict.get('CreateDate', current_time)}</xmp:CreateDate>
         <xmp:ModifyDate>{metadata_dict.get('ModifyDate', current_time)}</xmp:ModifyDate>
         <xmp:MetadataDate>{metadata_dict.get('MetadataDate', current_time)}</xmp:MetadataDate>
         <dc:creator>{metadata_dict.get('Creator', 'Unknown')}</dc:creator>
         <photoshop:Headline>{metadata_dict.get('Headline', 'Generated by Python')}</photoshop:Headline>
         <xmpRights:UsageTerms>{metadata_dict.get('UsageTerms', 'Copyrighted work')}</xmpRights:UsageTerms>
         <dc:description>{metadata_dict.get('Description', 'No description available')}</dc:description>
"""
    for field_name, field_value in custom_fields.items():
        xmp_template += f'         <xmp:{field_name}>{field_value}</xmp:{field_name}>\n'
    
    xmp_template += """      </rdf:Description>
   </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""
    return xmp_template

def save_xmp_file(file_path, content):
    """
    Saves the content to an XMP file specified by file_path.
    """
    with open(file_path, "w") as file:
        file.write(content)

def main():
    output_dir = "./tmp/"
    ensure_directory_exists(output_dir)
    
    xmp_content = generate_xmp_content(
        creator_tool="Advanced Python Script",
        metadata_dict={
            'CreateDate': '2023-01-01T12:00:00',
            'Creator': 'Python Developer',
            'Headline': 'Sample XMP File',
            'UsageTerms': 'Free for personal and educational use',
            'Description': 'This is a sample XMP file generated by a Python script for demonstration purposes.'
        },
        custom_fields={
            'CustomField1': 'This is a test custom field',
            'CustomField2': 'Another custom field with important information'
        }
    )
    
    xmp_file_path = os.path.join(output_dir, "advanced_example.xmp")
    save_xmp_file(xmp_file_path, xmp_content)
    
    print(f"XMP file has been saved to {xmp_file_path}")

if __name__ == "__main__":
    main()