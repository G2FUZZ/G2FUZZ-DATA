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
    return encrypted_frame

# Function to decrypt data
def decrypt_frame(encrypted_frame, key, shape):
    """Decrypts an encrypted frame."""
    fernet = Fernet(key)
    # Decrypt the frame
    decrypted_frame = fernet.decrypt(encrypted_frame)
    return np.frombuffer(decrypted_frame, dtype=np.uint8).reshape(shape)

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate a key for encryption
key = Fernet.generate_key()

# Define the video specifications
output_filename = output_dir + "complex_example_encrypted_streaming.mp4"
frame_size = (640, 480)  # Width, Height
fps = 24  # Frames per second
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec definition
duration_sec = 10  # Duration of the video in seconds

# Create a VideoWriter object
out = cv2.VideoWriter(output_filename, fourcc, fps, frame_size)

# Generate frames with more complex features
for i in range(fps * duration_sec):
    # Generate dynamic background color
    bg_color = (i % 255, (i * 2) % 255, (i * 3) % 255)
    frame = np.full((frame_size[1], frame_size[0], 3), bg_color, dtype=np.uint8)
    
    # Define multiple moving shapes
    # Moving rectangle
    rect_start_point = (i * 5 % frame_size[0], 50)
    rect_end_point = (rect_start_point[0] + 100, 150)
    frame = cv2.rectangle(frame, rect_start_point, rect_end_point, (255, 255, 255), -1)
    
    # Moving circle
    circle_center = (frame_size[0] - i * 5 % frame_size[0], 350)
    frame = cv2.circle(frame, circle_center, 50, (0, 255, 0), -1)
    
    # Overlay text displaying the current frame number
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_position = (10, frame_size[1] - 10)
    cv2.putText(frame, f'Frame: {i}', text_position, font, 1, (0, 0, 255), 2, cv2.LINE_AA)
    
    # Encrypt and then immediately decrypt the frame for demonstration
    encrypted_frame = encrypt_frame(frame, key)
    decrypted_frame = decrypt_frame(encrypted_frame, key, frame.shape)
    
    # Write the decrypted frame into the file
    out.write(decrypted_frame)

# Release everything when the job is finished
out.release()
print(f"Video successfully saved to {output_filename}")