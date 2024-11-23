import subprocess

# Set the input and output file paths
input_file = "./tmp/audio_aac.mp4"
output_file = "./tmp/audio_aac_encrypted_with_thumbnails.mp4"

# Use ffmpeg to add the Fast Start, Encryption, and Embedded Thumbnails features to the mp4 file
subprocess.run(["ffmpeg", "-i", input_file, "-c", "copy", "-movflags", "faststart+faststart", "-encryption_scheme", "cenc-aes-ctr", "-encryption_key", "0123456789ABCDEF0123456789ABCDEF", "-attach", "thumbnail.jpg", "-metadata:s:t", "mimetype=image/jpeg", "-disposition:attached_pic", "1", output_file])