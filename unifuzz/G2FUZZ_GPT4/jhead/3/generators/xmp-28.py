import os
from datetime import datetime

def create_xmp_file(file_path, metadata, history_events, custom_namespaces={}, localized_titles=[], localized_descriptions=[], rights_management={}, file_format='image/jpeg'):
    """
    Creates an XMP file with customizable metadata, multiple history events, support for multiple file formats,
    custom namespaces, localized titles and descriptions, and rights management information.
    
    :param file_path: Path to save the XMP file.
    :param metadata: Dictionary of metadata fields (key: field name, value: field value).
    :param history_events: List of dictionaries for each history event (keys: action, instanceID, when, softwareAgent).
    :param custom_namespaces: Dictionary of custom namespaces (key: prefix, value: URI).
    :param localized_titles: List of dictionaries for localized titles (keys: lang, title).
    :param localized_descriptions: List of dictionaries for localized descriptions (keys: lang, description).
    :param rights_management: Dictionary of rights management information (keys: certificate, marked, owner, usageTerms, webStatement).
    :param file_format: The format of the file (default is 'image/jpeg').
    """
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # XMP template with placeholders
    xmp_template = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/"{custom_namespaces_attr}>
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
       xmlns:xmp="http://ns.adobe.com/xap/1.0/"
       xmlns:dc="http://purl.org/dc/elements/1.1/"
       xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/"
       xmlns:stEvt="http://ns.adobe.com/xap/1.0/sType/ResourceEvent#"
       {custom_namespaces_attr_in_desc}>
   <dc:format>{file_format}</dc:format>
   {metadata_fields}
   {localized_titles_str}
   {localized_descriptions_str}
   <xmpMM:History>
    <rdf:Seq>
     {history_items}
    </rdf:Seq>
   </xmpMM:History>
   {rights_management_str}
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

    # Prepare custom namespaces
    custom_namespaces_attr = ' '.join([f'xmlns:{prefix}="{uri}"' for prefix, uri in custom_namespaces.items()])
    custom_namespaces_attr_in_desc = ' '.join([f'xmlns:{prefix}="{uri}"' for prefix, uri in custom_namespaces.items() if prefix not in ['xmp', 'dc', 'xmpMM', 'stEvt']])

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
    
    # Localized Titles
    localized_titles_str = '\n   '.join(
        [f'<dc:title><rdf:Alt><rdf:li xml:lang="{item["lang"]}">{item["title"]}</rdf:li></rdf:Alt></dc:title>' for item in localized_titles])

    # Localized Descriptions
    localized_descriptions_str = '\n   '.join(
        [f'<dc:description><rdf:Alt><rdf:li xml:lang="{item["lang"]}">{item["description"]}</rdf:li></rdf:Alt></dc:description>' for item in localized_descriptions])

    # Rights Management
    rights_management_str = '\n   '.join(
        [f'<xmpRights:{key}>{value}</xmpRights:{key}>' for key, value in rights_management.items()])

    # Fill in the template
    xmp_content = xmp_template.format(file_format=file_format, metadata_fields=metadata_fields, history_items=history_items, custom_namespaces_attr=custom_namespaces_attr, custom_namespaces_attr_in_desc=custom_namespaces_attr_in_desc, localized_titles_str=localized_titles_str, localized_descriptions_str=localized_descriptions_str, rights_management_str=rights_management_str)

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

custom_namespaces = {
    'myNS': 'http://example.com/ns/'
}

localized_titles = [
    {'lang': 'en-US', 'title': 'Example Title in English'},
    {'lang': 'fr-FR', 'title': 'Exemple de Titre en Français'}
]

localized_descriptions = [
    {'lang': 'en-US', 'description': 'An example description in English.'},
    {'lang': 'fr-FR', 'description': 'Un exemple de description en français.'}
]

rights_management = {
    'certificate': 'http://example.com/certificates/cert123',
    'marked': 'true',
    'owner': 'John Doe',
    'usageTerms': 'All rights reserved.',
    'webStatement': 'http://example.com/rights/'
}

file_path = './tmp/advanced_example_with_more_features.xmp'
create_xmp_file(file_path, metadata, history_events, custom_namespaces, localized_titles, localized_descriptions, rights_management)