from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
from datetime import datetime, timedelta
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Details for the certificate
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Organization"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"mydomain.com"),
])

# Validity period
valid_from = datetime.utcnow()
valid_to = valid_from + timedelta(days=365)

# Build the certificate
certificate = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    private_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    valid_from
).not_valid_after(
    valid_to
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName(u"mydomain.com")]),
    critical=False,
).sign(private_key, hashes.SHA256())

# Save the certificate as a DER file
cert_file_path = os.path.join(output_dir, 'certificate.der')
with open(cert_file_path, 'wb') as cert_file:
    cert_file.write(certificate.public_bytes(serialization.Encoding.DER))

# Now, let's generate a dummy CRL (Certificate Revocation List)
crl_builder = x509.CertificateRevocationListBuilder().issuer_name(
    issuer
).last_update(
    datetime.utcnow()
).next_update(
    datetime.utcnow() + timedelta(days=30)
)

# Sign the CRL with our private key
crl = crl_builder.sign(private_key, hashes.SHA256())

# Save the CRL as a DER file
crl_file_path = os.path.join(output_dir, 'crl.der')
with open(crl_file_path, 'wb') as crl_file:
    crl_file.write(crl.public_bytes(serialization.Encoding.DER))

print(f"Certificate saved to {cert_file_path}")
print(f"CRL saved to {crl_file_path}")