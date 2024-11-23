import os

# Create a directory to save the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate mp3 files with different encoding options, bit rates, and sampling rates
for encoding_option in ['Joint Stereo', 'Stereo', 'Mono']:
    for bit_rate in [128, 192, 320]:
        for sampling_rate in [44100, 48000]:
            file_path = f'./tmp/file_{encoding_option.replace(" ", "_")}_br{bit_rate}_sr{sampling_rate}.mp3'
            with open(file_path, 'w') as file:
                file.write(f'This is an mp3 file encoded with {encoding_option} option, bit rate: {bit_rate} kbps, sampling rate: {sampling_rate} Hz.')

print('Generated mp3 files with different encoding options, bit rates, and sampling rates successfully.')