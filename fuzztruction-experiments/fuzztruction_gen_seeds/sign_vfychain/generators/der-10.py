import asn1tools
import os

# Define a simple ASN.1 schema to hold our feature description
schema = """
FeatureDescription DEFINITIONS ::= BEGIN
    Feature ::= SEQUENCE {
        id INTEGER,
        description UTF8String
    }
END
"""

# Compile the schema
compiled_schema = asn1tools.compile_string(schema, codec='der')

# Our feature data based on your description
feature_data = {
    'id': 9,  # Assuming an arbitrary ID for the feature
    'description': "Direct Hardware Support: Some hardware devices, such as smart cards and hardware security modules (HSMs), may directly work with DER-encoded data, leveraging the format's efficiency and compactness for storage and processing constraints."
}

# Encode the data to DER format
encoded_data = compiled_schema.encode('Feature', feature_data)

# Ensure the output directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the encoded data to a DER file
output_file_path = os.path.join(output_dir, 'feature_description.der')
with open(output_file_path, 'wb') as file:
    file.write(encoded_data)

print(f"DER file saved to {output_file_path}")