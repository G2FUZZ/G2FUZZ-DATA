import os
from datetime import datetime

def create_xmp_file(file_path, metadata, history_events, file_format='image/jpeg'):
    """
    Creates an XMP file with customizable metadata, multiple history events, and support for multiple file formats.
    
    :param file_path: Path to save the XMP file.
    :param metadata: Dictionary of metadata fields (key: field name, value: field value).
    :param history_events: List of dictionaries for each history event (keys: action, instanceID, when, softwareAgent).
    :param file_format: The format of the file (default is 'image/jpeg').
    """
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # XMP template with placeholders for metadata and history
    xmp_template = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
       xmlns:xmp="http://ns.adobe.com/xap/1.0/"
       xmlns:dc="http://purl.org/dc/elements/1.1/"
       xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/"
       xmlns:stEvt="http://ns.adobe.com/xap/1.0/sType/ResourceEvent#">
   <dc:format>{file_format}</dc:format>
   {metadata_fields}
   <xmpMM:History>
    <rdf:Seq>
     {history_items}
    </rdf:Seq>
   </xmpMM:History>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''
    
    # Generate metadata fields string
    metadata_fields = '\n   '.join([f'<{key}>{value}</{key}>' for key, value in metadata.items()])
    
    # Generate history items string
    history_items = '\n     '.join([
        f'''<rdf:li rdf:parseType="Resource">
      <stEvt:action>{event["action"]}</stEvt:action>
      <stEvt:instanceID>{event["instanceID"]}</stEvt:instanceID>
      <stEvt:when>{event["when"]}</stEvt:when>
      <stEvt:softwareAgent>{event["softwareAgent"]}</stEvt:softwareAgent>
     </rdf:li>''' for event in history_events
    ])
    
    # Fill in the template
    xmp_content = xmp_template.format(file_format=file_format, metadata_fields=metadata_fields, history_items=history_items)

    # Write the XMP content to a file
    with open(file_path, 'w') as file:
        file.write(xmp_content)

    print(f'XMP file saved as {file_path}')

# Example usage
metadata = {
    'xmp:CreatorTool': 'Advanced Example Creator',
    'dc:creator': 'John Doe'
}

history_events = [
    {
        'action': 'created',
        'instanceID': 'xmp.iid:123456',
        'when': datetime.now().isoformat(),
        'softwareAgent': 'Advanced Example Creator'
    },
    {
        'action': 'modified',
        'instanceID': 'xmp.iid:7891011',
        'when': datetime.now().isoformat(),
        'softwareAgent': 'Advanced Example Modifier'
    }
]

file_path = './tmp/advanced_example.xmp'
create_xmp_file(file_path, metadata, history_events)