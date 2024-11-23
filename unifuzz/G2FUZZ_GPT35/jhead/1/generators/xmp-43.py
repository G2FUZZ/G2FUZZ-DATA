import os

# Define the XMP file name and path
xmp_file = "./tmp/metadata.xmp"

# Define the metadata fields
metadata = {
    "Title": "Sample Title",
    "Author": "John Doe",
    "Description": "This is a sample XMP file with complex structures.",
    "Tags": ["tag1", "tag2", "tag3"],
    "CustomFields": {
        "Field1": "Value1",
        "Field2": "Value2"
    }
}

# Generate the XMP file with complex structures
with open(xmp_file, "w") as file:
    file.write("<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>\n")
    file.write("<rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>\n")
    
    for key, value in metadata.items():
        if isinstance(value, list):
            file.write(f"  <{key}>\n")
            for item in value:
                file.write(f"    <rdf:li>{item}</rdf:li>\n")
            file.write(f"  </{key}>\n")
        elif isinstance(value, dict):
            file.write(f"  <{key}>\n")
            for subkey, subvalue in value.items():
                file.write(f"    <{subkey}>{subvalue}</{subkey}>\n")
            file.write(f"  </{key}>\n")
        else:
            file.write(f"  <{key}>{value}</{key}>\n")
    
    file.write("</rdf:RDF>\n")
    file.write("<?xpacket end='w'?>\n")

print("XMP file with complex structures generated successfully.")