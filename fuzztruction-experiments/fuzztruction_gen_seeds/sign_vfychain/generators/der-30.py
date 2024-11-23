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

# New feature data for Tagging Mechanism
tagging_mechanism_feature_data = {
    'id': 9,
    'description': "**Tagging Mechanism**: DER uses a tagging mechanism for identifying the type of data elements (e.g., INTEGER, OCTET STRING), which aids in parsing and interpreting the content correctly without ambiguity."
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

# Save the new Tagging Mechanism feature to a DER file
save_feature_to_der_file(tagging_mechanism_feature_data, 'tagging_mechanism_feature_description.der')