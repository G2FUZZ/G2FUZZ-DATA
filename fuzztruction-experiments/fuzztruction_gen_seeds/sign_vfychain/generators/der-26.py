import asn1tools
import os

# Updated ASN.1 schema to include multiple Features in a sequence
schema = """
FeatureDescriptions DEFINITIONS ::= BEGIN
    Feature ::= SEQUENCE {
        id INTEGER,
        description UTF8String
    }
    Features ::= SEQUENCE OF Feature
END
"""

# Compile the updated schema
compiled_schema = asn1tools.compile_string(schema, codec='der')

# Our original feature data and the new feature data, including the new "Length Encoding" feature
features_data = [
    {
        'id': 9,  # Assuming an arbitrary ID for the original feature
        'description': "Direct Hardware Support: Some hardware devices, such as smart cards and hardware security modules (HSMs), may directly work with DER-encoded data, leveraging the format's efficiency and compactness for storage and processing constraints."
    },
    {
        'id': 6,  # Arbitrary ID for the new feature "Constraint Validation"
        'description': "**Constraint Validation**: The strict encoding rules of DER ensure that all constraints specified in the ASN.1 definition are met. This includes size constraints, range values, and mandatory elements, which are critical for the integrity and validation of the encoded data."
    },
    {
        'id': 5,  # Adding new ID for "Length Encoding"
        'description': "**Length Encoding**: DER files use a specific scheme for encoding the length of data elements, which can handle both fixed-size and variable-size data. This flexibility supports a wide range of applications, from simple data fields to complex structures with dynamic sizes."
    }
]

# Encode the data to DER format
encoded_data = compiled_schema.encode('Features', features_data)

# Ensure the output directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the encoded data to a new DER file
output_file_path = os.path.join(output_dir, 'features_description_with_length_encoding.der')
with open(output_file_path, 'wb') as file:
    file.write(encoded_data)

print(f"DER file saved to {output_file_path}")