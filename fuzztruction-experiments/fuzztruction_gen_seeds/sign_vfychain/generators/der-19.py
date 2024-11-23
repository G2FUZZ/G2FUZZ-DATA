from cryptography.hazmat.primitives import serialization
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, ec
import datetime

def generate_rsa_key_and_certificate():
    # Generate a private RSA key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    return generate_certificate(private_key)

def generate_ec_key_and_certificate():
    # Generate a private EC key
    private_key = ec.generate_private_key(
        curve=ec.SECP256R1()
    )
    return generate_certificate(private_key)

def generate_certificate(private_key):
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
    return private_key, certificate

# Generate RSA key and certificate
private_key_rsa, certificate_rsa = generate_rsa_key_and_certificate()
# Generate EC key and certificate
private_key_ec, certificate_ec = generate_ec_key_and_certificate()

# Save the RSA private key and certificate
with open("./tmp/private_key_rsa.der", "wb") as f:
    f.write(private_key_rsa.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open("./tmp/certificate_rsa.der", "wb") as f:
    f.write(certificate_rsa.public_bytes(
        encoding=serialization.Encoding.DER
    ))

# Save the EC private key and certificate
with open("./tmp/private_key_ec.der", "wb") as f:
    f.write(private_key_ec.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open("./tmp/certificate_ec.der", "wb") as f:
    f.write(certificate_ec.public_bytes(
        encoding=serialization.Encoding.DER
    ))