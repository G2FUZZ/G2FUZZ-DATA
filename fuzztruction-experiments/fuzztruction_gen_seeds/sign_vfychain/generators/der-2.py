from pyasn1.type import univ
from pyasn1.codec.der import encoder
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define a simple ASN.1 structure (e.g., an integer)
asn1_integer = univ.Integer(12345)

# Encode the ASN.1 structure into DER format
encoded_data = encoder.encode(asn1_integer)

# Write the DER-encoded data to a file
with open('./tmp/integer.der', 'wb') as f:
    f.write(encoded_data)