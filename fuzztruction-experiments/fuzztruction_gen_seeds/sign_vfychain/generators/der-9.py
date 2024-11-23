import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes  # Import hashes module
from cryptography import x509
from cryptography.x509.oid import NameOID
from datetime import datetime, timedelta

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a private key for use in certificates and private key files
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Generate a self-signed certificate for demonstration purposes
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"mycompany.com"),
])
certificate = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    private_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.utcnow()
).not_valid_after(
    # Our certificate will be valid for 10 days
    datetime.utcnow() + timedelta(days=10)
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),
    critical=False,
).sign(private_key, hashes.SHA256())  # Now 'hashes' is defined

# Save the private key to a .key file in DER format
with open("./tmp/private_key.key", "wb") as key_file:
    key_file.write(private_key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

# Save the certificate to a .cer file in DER format
with open("./tmp/certificate.cer", "wb") as cert_file:
    cert_file.write(certificate.public_bytes(
        encoding=serialization.Encoding.DER
    ))

# Save the certificate to a .crt file in DER format (same content as .cer, different extension for demonstration)
with open("./tmp/certificate.crt", "wb") as crt_file:
    crt_file.write(certificate.public_bytes(
        encoding=serialization.Encoding.DER
    ))