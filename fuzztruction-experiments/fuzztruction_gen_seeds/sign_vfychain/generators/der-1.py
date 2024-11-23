import asn1tools
import os

# Define the ASN.1 schema
schema = """
Module DEFINITIONS ::= BEGIN

    MyData ::= SEQUENCE {
        id INTEGER,
        description UTF8String
    }

END
"""

# Compile the schema
compiled_schema = asn1tools.compile_string(schema, codec='der')

# Create a directory for the DER files if it doesn't already exist
os.makedirs('./tmp/', exist_ok=True)

# Define the data to be encoded
data_to_encode = {'id': 123, 'description': 'This is a test'}

# Encode the data using the compiled schema
encoded_data = compiled_schema.encode('MyData', data_to_encode)

# Save the encoded data to a DER file
with open('./tmp/example.der', 'wb') as file:
    file.write(encoded_data)

print("DER file has been generated and saved to ./tmp/example.der")