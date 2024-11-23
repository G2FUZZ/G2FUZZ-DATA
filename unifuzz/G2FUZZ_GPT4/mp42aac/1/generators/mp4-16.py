import numpy as np
import cv2
import os
from cryptography.fernet import Fernet

# Function to encrypt data
def encrypt_frame(frame, key):
    """Encrypts a frame using Fernet symmetric encryption."""
    fernet = Fernet(key)
    # Encrypt the frame
    encrypted_frame = fernet.encrypt(frame.tobytes())
    return encrypted_frame  # Return encrypted bytes directly

# Function to decrypt data (for demonstration/testing)
def decrypt_frame(encrypted_frame, key, shape):
    """Decrypts an encrypted frame."""
    fernet = Fernet(key)
    # Decrypt the frame
    decrypted_frame = fernet.decrypt(encrypted_frame)  # encrypted_frame is now expected to be bytes
    return np.frombuffer(decrypted_frame, dtype=np.uint8).reshape(shape)

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate a key for encryption
key = Fernet.generate_key()

# Define the video specifications
output_filename = output_dir + "example_encrypted_streaming.mp4"
frame_size = (640, 480)  # Width, Height
fps = 24  # Frames per second
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec definition
duration_sec = 5  # Duration of the video in seconds

# Create a VideoWriter object
out = cv2.VideoWriter(output_filename, fourcc, fps, frame_size)

# Generate frames
for i in range(fps * duration_sec):
    # Create a black image
    frame = np.zeros((frame_size[1], frame_size[0], 3), dtype=np.uint8)
    
    # Define a moving rectangle parameters
    start_point = (i * 5 % frame_size[0], 50)  # Moving along the x-axis
    end_point = (start_point[0] + 100, 150)  # Fixed size
    color = (255, 255, 255)  # White
    thickness = -1  # Solid
    
    # Draw the rectangle on the frame
    frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
    
    # Encrypt the frame before writing to file (demonstration of concept, not actual secure encryption for streaming)
    encrypted_frame = encrypt_frame(frame, key)
    # To maintain the example's simplicity, we'll bypass the actual encrypted data saving and decryption as it
    # cannot be directly written through cv2.VideoWriter due to format and encryption overhead
    # Instead, we'll decrypt immediately for demonstration (to be replaced with actual secure handling methods)
    decrypted_frame = decrypt_frame(encrypted_frame, key, frame.shape)
    
    # Write the decrypted frame (simulating the encryption process) into the file
    out.write(decrypted_frame)

# Release everything when the job is finished
out.release()
print(f"Video successfully saved to {output_filename}")