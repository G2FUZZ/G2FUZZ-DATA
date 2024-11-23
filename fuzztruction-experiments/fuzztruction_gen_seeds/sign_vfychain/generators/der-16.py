from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.x509.oid import NameOID
import datetime
import os
from cryptography.hazmat.primitives import serialization
from cryptography.x509.oid import ExtensionOID

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Create a builder for the certificate
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Organization"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"mydomain.com"),
])
certificate_builder = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    private_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    # Certificate valid for 1 year
    datetime.datetime.utcnow() + datetime.timedelta(days=365)
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName(u"mydomain.com")]),
    critical=False,
)

# Assuming we want to add a custom extension to encode structured data
# Here we're using a dummy OID for demonstration. In a real scenario, you'll need to use or define an appropriate OID.
structured_data_oid = x509.ObjectIdentifier("1.3.6.1.4.1.99999.1")
structured_data = b"\x30\x0c\x02\x01\x01\x02\x01\x02\x02\x01\x03"  # ASN.1 Encoding of some structured data
certificate_builder = certificate_builder.add_extension(
    x509.UnrecognizedExtension(structured_data_oid, structured_data),
    critical=False,
)

# Sign the certificate with the private key
certificate = certificate_builder.sign(
    private_key=private_key, algorithm=hashes.SHA256(),
)

# Save the certificate as a DER file
with open('./tmp/certificate_with_structured_data.der', 'wb') as f:
    f.write(certificate.public_bytes(Encoding.DER))

print("DER file with Encoding of Structured Data generated and saved to ./tmp/certificate_with_structured_data.der")