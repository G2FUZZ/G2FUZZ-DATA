import asn1tools
import os

# ASN.1 specification
asn_spec = """
MyModule DEFINITIONS ::= BEGIN

-- Definition of a simple sequence with one element
Features ::= SEQUENCE {
    versatilityInApplications    VisibleString
}

END
"""

# Compile the ASN.1 specification
compiled_spec = asn1tools.compile_string(asn_spec, 'der')

# Data to be encoded
data = {
    'versatilityInApplications': 'Beyond cryptographic keys and certificates, DER files can be used to encode any data that can be described by ASN.1, including various protocols\' messages, making them versatile in network and security-related applications.'
}

# Encode the data
encoded_data = compiled_spec.encode('Features', data)

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Write the encoded data to a DER file
with open('./tmp/features.der', 'wb') as f:
    f.write(encoded_data)

print("DER file generated successfully.")