def create_flv_audio(audio_data, sample_rate=44100, codec='mp3', filename='output.flv', backward_compatible=True):
    # Temporary audio file path (to be encoded into FLV)
    temp_audio_path = os.path.join(output_dir, 'temp_audio.wav')  # Correct use of output_dir to save in ./tmp/
    
    # Save the audio data to a temporary WAV file
    write(temp_audio_path, sample_rate, audio_data)  # Save the waveform to a file in ./tmp/
    
    # Use the temporary WAV file with AudioFileClip
    audio_clip = AudioFileClip(temp_audio_path)
    temp_mp3_path = os.path.join(output_dir, 'temp_audio.mp3')  # Again, using output_dir to save in ./tmp/
    audio_clip.write_audiofile(temp_mp3_path, codec=codec)
    
    # Use ffmpeg to package the MP3 into an FLV container
    flv_output_path = os.path.join(output_dir, filename)  # Ensuring the FLV file is saved in ./tmp/
    if backward_compatible:
        # Including backward compatibility flag for older versions of Flash Player
        os.system(f"ffmpeg -i {temp_mp3_path} -ar 22050 -c:a copy {flv_output_path}")
    else:
        os.system(f"ffmpeg -i {temp_mp3_path} -c:a copy {flv_output_path}")
    
    # Cleanup the temporary audio files
    os.remove(temp_audio_path)
    os.remove(temp_mp3_path)