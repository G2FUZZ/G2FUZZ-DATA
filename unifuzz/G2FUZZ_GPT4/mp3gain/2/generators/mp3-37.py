import os

def generate_complex_sine_wave(freq, sample_rate, duration, file_title, album_name, track_number, year, artist_name, cover_art_path):
    # Generate a sine wave audio signal
    audio = generate_sine_wave(freq, sample_rate, duration)

    # Normalize to 16-bit range for WAV format
    audio_normalized = np.int16((audio / audio.max()) * 32767)

    # Use a temporary directory to first save as WAV (since direct MP3 generation might not be supported)
    with TemporaryDirectory() as tmpdirname:
        wav_path = os.path.join(tmpdirname, 'temp.wav')
        mp3_path = f'./tmp/{file_title}.mp3'
        
        # Write the audio data as a WAV file
        wavfile.write(wav_path, sample_rate, audio_normalized)
        
        # Convert WAV to MP3 with Customizable Quality Settings
        sound = AudioSegment.from_wav(wav_path)
        
        # Export with customizable quality settings
        sound.export(mp3_path, format="mp3", bitrate=bitrate, parameters=["-q:a", str(encoding_quality)])

        # Attempt to add ID3 tags to the MP3 file
        try:
            audio = ID3(mp3_path)
        except ID3NoHeaderError:
            audio = ID3()
        
        audio.add(TIT2(encoding=3, text=file_title))
        audio.add(TPE1(encoding=3, text=artist_name))
        audio.add(TRCK(encoding=3, text=str(track_number)))
        audio.add(TALB(encoding=3, text=album_name))
        audio.add(TYER(encoding=3, text=str(year)))
        if cover_art_path and os.path.isfile(cover_art_path):
            with open(cover_art_path, 'rb') as img:
                audio.add(APIC(encoding=3, mime='image/jpeg', type=3, desc='Cover', data=img.read()))
        else:
            print(f"Warning: Cover art file not found at {cover_art_path}. Proceeding without cover art.")
        audio.save(mp3_path)  # Make sure to specify the file_name when saving

    print(f"Generated complex MP3 saved to: {mp3_path}")