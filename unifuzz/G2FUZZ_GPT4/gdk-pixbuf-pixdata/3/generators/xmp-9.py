import os
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

def create_xmp_history(filename, history_events):
    # Corrected namespace declarations
    ns_map = {
        'x': 'adobe:ns:meta/',
        'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
        'xmpMM': 'http://ns.adobe.com/xap/1.0/mm/',
        'stEvt': 'http://ns.adobe.com/xap/1.0/sType/ResourceEvent#'
    }
    
    # Base XMP structure with corrected namespaces
    xmp_meta = Element('x:xmpmeta', {'xmlns:x': ns_map['x'], 'xmlns:rdf': ns_map['rdf'], 'xmlns:xmpMM': ns_map['xmpMM'], 'xmlns:stEvt': ns_map['stEvt']})
    rdf_rdf = SubElement(xmp_meta, 'rdf:RDF')

    # Description element with history namespace
    rdf_description = SubElement(rdf_rdf, 'rdf:Description', {
        'rdf:about': ''
    })
    
    # History List
    st_history = SubElement(rdf_description, 'xmpMM:History')
    
    # Adding history events
    for event in history_events:
        rdf_seq = SubElement(st_history, 'rdf:Seq')
        rdf_li = SubElement(rdf_seq, 'rdf:li', {
            'rdf:parseType': 'Resource',
            'stEvt:action': event['action'],
            'stEvt:instanceID': event['instanceID'],
            'stEvt:when': event['when'],
            'stEvt:softwareAgent': event['softwareAgent'],
            'stEvt:changed': event['changed']
        })
    
    # Beautify and convert to string
    raw_xmp = tostring(xmp_meta, 'utf-8')
    dom = parseString(raw_xmp)  # Use parseString to convert byte string to DOM
    pretty_xmp = dom.toprettyxml(indent="   ")
    
    # Save to file
    save_path = os.path.join('./tmp/', filename)
    with open(save_path, 'w') as file:
        file.write(pretty_xmp)

# Example usage
history_events = [
    {
        'action': 'created',
        'instanceID': 'xmp.iid:123456',
        'when': datetime.now().isoformat(),
        'softwareAgent': 'Photoshop 21.0',
        'changed': '/'
    },
    {
        'action': 'edited',
        'instanceID': 'xmp.iid:123457',
        'when': datetime.now().isoformat(),
        'softwareAgent': 'Photoshop 21.0',
        'changed': 'brightness, contrast'
    }
]

create_xmp_history('example.xmp', history_events)