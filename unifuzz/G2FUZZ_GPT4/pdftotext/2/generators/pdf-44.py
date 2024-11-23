import os
import tempfile

def add_qr_code(self, data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Ensure the ./tmp/ directory exists
    tmp_dir = './tmp'
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)

    # Create a temporary file within the ./tmp/ directory
    tmpfile_fd, tmpfile_path = tempfile.mkstemp(suffix=".png", dir=tmp_dir)
    os.close(tmpfile_fd)  # Close the file descriptor

    # Save the QR code image to the temporary file
    img.save(tmpfile_path, format="PNG")

    # Use the temporary file path to insert the image
    self.image(tmpfile_path, x=10, y=self.get_y(), w=30)
    self.ln(40)  # Adjust space after QR code

    # Clean up by deleting the temporary file
    os.remove(tmpfile_path)