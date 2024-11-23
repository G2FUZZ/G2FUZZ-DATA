from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding
from datetime import datetime, timedelta
import os

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Create a name builder
name = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Organization"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"mydomain.com"),
])

# Build certificate
certificate = (
    x509.CertificateBuilder()
    .subject_name(name)
    .issuer_name(name)  # Self-signed, so issuer is the same as subject
    .public_key(private_key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365))  # The certificate is valid for 1 year
    .add_extension(
        x509.SubjectAlternativeName([x509.DNSName(u"mydomain.com")]),
        critical=False,
    )
    .sign(private_key, hashes.SHA256())
)

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Save the certificate as a DER file
with open('./tmp/certificate.der', 'wb') as der_file:
    der_file.write(certificate.public_bytes(Encoding.DER))

print("Certificate generated and saved as './tmp/certificate.der'")