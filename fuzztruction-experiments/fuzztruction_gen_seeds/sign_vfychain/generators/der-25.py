from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.x509.oid import NameOID, ExtendedKeyUsageOID
import datetime
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a private key for the CA
ca_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Generate a private key for the server
server_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# CA's subject and issuer are the same
ca_subject = ca_issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My CA Organization"),
    x509.NameAttribute(NameOID.COMMON_NAME, "myca.com"),
])

ca_certificate_builder = x509.CertificateBuilder().subject_name(
    ca_subject
).issuer_name(
    ca_issuer
).public_key(
    ca_private_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    datetime.datetime.utcnow() + datetime.timedelta(days=365)  # CA certificate valid for 1 year
).add_extension(
    x509.BasicConstraints(ca=True, path_length=None), critical=True,
)

# Sign the CA certificate with its own private key
ca_certificate = ca_certificate_builder.sign(
    private_key=ca_private_key, algorithm=hashes.SHA256(),
)

# Server's subject and issuer
server_subject = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Server Organization"),
    x509.NameAttribute(NameOID.COMMON_NAME, "myserver.com"),
])

# Adding a custom extension for embedded information, such as policies
policy_information = x509.CertificatePolicies([
    x509.PolicyInformation(policy_identifier=x509.ObjectIdentifier("1.3.6.1.4.1.9999.2.1"),
                           policy_qualifiers=[x509.UserNotice(notice_reference=x509.NoticeReference(organization="My Org", notice_numbers=[1, 2, 3]),
                                                              explicit_text="This is an example of embedded information for compliance and audit purposes.")])
])

server_certificate_builder = x509.CertificateBuilder().subject_name(
    server_subject
).issuer_name(
    ca_subject  # Issued by the CA
).public_key(
    server_private_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    datetime.datetime.utcnow() + datetime.timedelta(days=365)  # Server certificate valid for 1 year
).add_extension(
    policy_information, critical=False
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName("myserver.com")]),
    critical=False,
)

# Sign the server certificate with the CA's private key
server_certificate = server_certificate_builder.sign(
    private_key=ca_private_key, algorithm=hashes.SHA256(),
)

# DER encoding inherently ensures Sequence and Set Ordering.
# Therefore, the existing process already adheres to DER's requirements for canonical ordering within sequences and sets.
# No additional code modification is specifically required for this feature.

# Save the server certificate as a DER file
with open('./tmp/server_certificate_with_embedded_info.der', 'wb') as f:
    f.write(server_certificate.public_bytes(Encoding.DER))

# Optionally, the CA certificate can also be saved if needed for a chain
with open('./tmp/ca_certificate.der', 'wb') as f:
    f.write(ca_certificate.public_bytes(Encoding.DER))

print("DER files with embedded information generated and saved to ./tmp/")