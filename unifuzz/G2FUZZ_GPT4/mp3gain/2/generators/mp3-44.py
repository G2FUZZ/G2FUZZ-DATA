import os
from pydub import AudioSegment
from pydub.generators import Sine
import lameenc
from mutagen.id3 import ID3, TIT2, TPE1, TRCK, TALB, APIC, TYER, USLT, ID3NoHeaderError

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_melodic_mp3(bit_rates, file_title, album_name, track_number, year, artist_name, cover_art_path, lyrics):
    melody = AudioSegment.silent(duration=0)  # Start with a silent segment

    # Define a simple melody: sequence of frequencies (Hz)
    notes = [440, 494, 523, 587, 659, 698, 784, 880]

    # Generate the melody: combining sine waves for each note
    for note in notes:
        tone = Sine(note).to_audio_segment(duration=500)
        melody += tone

    # Apply fading in and out
    melody = melody.fade_in(200).fade_out(300)

    for bit_rate in bit_rates:
        # Convert the audio segment to raw audio data (WAV)
        wave_data = melody.raw_data

        # Setup the encoder with the specified bit rate
        encoder = lameenc.Encoder()
        encoder.set_bit_rate(bit_rate)
        encoder.set_in_sample_rate(melody.frame_rate)
        encoder.set_channels(melody.channels)
        encoder.set_quality(2)  # 2 is the highest quality

        # Encode the raw audio data to MP3
        mp3_data = encoder.encode(wave_data)
        mp3_data += encoder.flush()

        # Save the MP3 data to a file
        file_name = f'./tmp/{file_title}_{bit_rate}kbps.mp3'
        with open(file_name, 'wb') as f:
            f.write(mp3_data)

        # Attempt to add ID3 tags and lyrics to the MP3 file
        try:
            audio = ID3(file_name)
        except ID3NoHeaderError:
            audio = ID3()
        
        audio.add(TIT2(encoding=3, text=file_title))
        audio.add(TPE1(encoding=3, text=artist_name))
        audio.add(TRCK(encoding=3, text=str(track_number)))
        audio.add(TALB(encoding=3, text=album_name))
        audio.add(TYER(encoding=3, text=str(year)))
        if cover_art_path and os.path.exists(cover_art_path):
            with open(cover_art_path, 'rb') as img:
                audio.add(APIC(encoding=3, mime='image/jpeg', type=3, desc='Cover', data=img.read()))
        else:
            print(f"Warning: Cover art file '{cover_art_path}' not found. Continuing without cover art.")
        if lyrics:
            audio.add(USLT(encoding=3, lang='eng', desc='desc', text=lyrics))
        audio.save(file_name)  # Make sure to specify the file_name when saving

        print(f'Generated melodic MP3 file at {bit_rate} kbps: {file_name}')

# Example of calling the function:
generate_melodic_mp3(
    bit_rates=[128, 256], 
    file_title="SimpleMelody", 
    album_name="My Album", 
    track_number=1, 
    year="2023", 
    artist_name="My Artist", 
    cover_art_path="./cover.jpg", 
    lyrics="Lyrics of the simple melody song."
)