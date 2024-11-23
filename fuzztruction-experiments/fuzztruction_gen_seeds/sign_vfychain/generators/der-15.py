from cryptography.hazmat.primitives import serialization
from cryptography import x509
from cryptography.x509.oid import NameOID, ExtensionOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
import datetime

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Create a self-signed certificate
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"mycompany.com"),
])

# Creating the certificate builder
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
    # Certificate is valid for 1 day
    datetime.datetime.utcnow() + datetime.timedelta(days=1)
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName(u"www.mycompany.com")]),
    critical=False,
)

# Adding the KeyUsage extension for non-repudiation
certificate_builder = certificate_builder.add_extension(
    x509.KeyUsage(
        digital_signature=True,  # This enables non-repudiation
        content_commitment=True,  # This is another term for non-repudiation
        key_encipherment=True,
        data_encipherment=False,
        key_agreement=False,
        key_cert_sign=False,
        crl_sign=False,
        encipher_only=False,
        decipher_only=False,
    ),
    critical=True,
)

certificate = certificate_builder.sign(private_key, hashes.SHA256())

# Save the private key and certificate
with open("./tmp/private_key.der", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open("./tmp/certificate.der", "wb") as f:
    f.write(certificate.public_bytes(
        encoding=serialization.Encoding.DER
    ))