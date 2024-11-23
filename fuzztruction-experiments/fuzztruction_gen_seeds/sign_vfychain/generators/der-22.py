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

# Our original feature data
original_feature_data = {
    'id': 9,
    'description': "Direct Hardware Support: Some hardware devices, such as smart cards and hardware security modules (HSMs), may directly work with DER-encoded data, leveraging the format's efficiency and compactness for storage and processing constraints."
}

# New feature data for Efficient Parsing
efficient_parsing_feature_data = {
    'id': 7,
    'description': "**Efficient Parsing**: The deterministic nature of DER encoding facilitates efficient parsing and decoding of the binary data. Since there is only one way to encode a given structure, parsers can operate faster and with less complexity than if multiple encoding options were available."
}

# New feature data for Compression Support
compression_support_feature_data = {
    'id': 10,
    'description': "**Compression Support**: While DER itself does not inherently compress data, the binary nature of DER-encoded files means they can be efficiently compressed with external tools or algorithms, potentially reducing storage and transmission costs in data-intensive applications."
}

# Ensure the output directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to save feature data to a DER file
def save_feature_to_der_file(feature_data, file_name):
    # Encode the data to DER format
    encoded_data = compiled_schema.encode('Feature', feature_data)

    # Save the encoded data to a DER file
    output_file_path = os.path.join(output_dir, file_name)
    with open(output_file_path, 'wb') as file:
        file.write(encoded_data)

    print(f"DER file saved to {output_file_path}")

# Save the original feature to a DER file
save_feature_to_der_file(original_feature_data, 'original_feature_description.der')

# Save the new Efficient Parsing feature to a DER file
save_feature_to_der_file(efficient_parsing_feature_data, 'efficient_parsing_feature_description.der')

# Save the new Compression Support feature to a DER file
save_feature_to_der_file(compression_support_feature_data, 'compression_support_feature_description.der')