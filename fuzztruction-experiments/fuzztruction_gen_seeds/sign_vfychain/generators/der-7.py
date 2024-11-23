from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

# Generate a private key for demonstration purposes
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Define the feature information to be saved in a DER file
feature_info = """
6. **Interoperability**: Due to their standardized format, DER files are widely supported across different platforms and software, making them suitable for interoperability in systems that require secure data exchange.
"""

# Encode the feature information as a DER formatted file
# Since DER is typically used for binary encoding of data structures, this example will
# demonstrate saving a private key to show the process. Encoding arbitrary text isn't
# typical for DER files, as they are used for cryptographic, certificate management, etc.
der_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Save the DER file
der_file_path = './tmp/feature_info_private_key.der'
with open(der_file_path, 'wb') as file:
    file.write(der_private_key)

print(f"DER file saved at: {der_file_path}")