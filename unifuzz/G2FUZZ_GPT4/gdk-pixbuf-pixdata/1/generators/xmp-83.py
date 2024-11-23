import os
from xml.sax.saxutils import escape

# Define a function to generate XMP content
def generate_xmp_content(metadata):
    """
    Generates XMP content with multiple descriptions, creator, rights, and custom fields.
    
    :param metadata: A dictionary containing different pieces of metadata.
    :return: A string of XMP content.
    """
    xmp_template = """
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP toolkit">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
          xmlns:dc="http://purl.org/dc/elements/1.1/"
          xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/"
          xmlns:cc="http://creativecommons.org/ns#"
          xmlns:my_ns="http://example.com/ns/">
  <rdf:Description rdf:about=""
    dc:description="{description}"
    dc:creator="{creator}"
    dc:title="{title}"
    xmpRights:UsageTerms="{usage_terms}"
    cc:license="{license}"
    my_ns:customField="{custom_field}">
    <dc:subject>
      <rdf:Bag>
        {subjects}
      </rdf:Bag>
    </dc:subject>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
""".format(
        description=escape(metadata.get("description", "")),
        creator=escape(metadata.get("creator", "")),
        title=escape(metadata.get("title", "")),
        usage_terms=escape(metadata.get("usage_terms", "")),
        license=escape(metadata.get("license", "")),
        custom_field=escape(metadata.get("custom_field", "")),
        subjects="\n        ".join([f'<rdf:li>{escape(subject)}</rdf:li>' for subject in metadata.get("subjects", [])])
    )
    
    return xmp_template.strip()

# Metadata to be included in the XMP file
metadata = {
    "description": "This is an extended XMP example with multiple fields.",
    "creator": "John Doe",
    "title": "Extended XMP Example",
    "usage_terms": "Free for personal use.",
    "license": "https://creativecommons.org/licenses/by-nc/4.0/",
    "custom_field": "Custom data relevant to the file.",
    "subjects": ["XMP", "Metadata", "Digital Asset Management"]
}

# Generate the XMP content
xmp_content = generate_xmp_content(metadata)

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the path for the new XMP file
xmp_file_path = './tmp/complex_features.xmp'

# Write the XMP content to the file
with open(xmp_file_path, 'w') as file:
    file.write(xmp_content)

print(f'XMP file saved at {xmp_file_path}')