from gtts import gTTS
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Text to be converted into speech, including the new feature description
text = "MP3 files are suitable for streaming over the internet due to their small size and ability to be decoded in real-time, which has made them popular for online music services. Additionally, the Joint Stereo Encoding Techniques feature utilizes MP3's joint stereo mode to apply techniques like Mid/Side (M/S) stereo coding and Intensity Stereo. This reduces file size by exploiting the psychoacoustic properties of how humans perceive sound spatially, optimizing the encoding of stereo signals by sharing information between channels when appropriate."

# Convert text to speech
tts = gTTS(text, lang='en')

# Save the converted file
tts.save("./tmp/streaming_support_with_joint_stereo.mp3")

print("MP3 file with Joint Stereo Encoding Techniques has been generated and saved to ./tmp/streaming_support_with_joint_stereo.mp3")