from mutagen.id3 import ID3, TIT2, TPE1, TRCK, TALB, APIC, TYER, ID3NoHeaderError

# The rest of your imports and code remains the same...

def generate_complex_mp3(bit_rate, file_title, album_name, track_number, year, artist_name, cover_art_path):
    # Your code for generating the MP3 file remains the same...

    # Save the MP3 data to a file
    file_name = f'./tmp/{file_title}_{bit_rate}kbps.mp3'
    with open(file_name, 'wb') as f:
        f.write(mp3_data)

    # Attempt to add ID3 tags to the MP3 file
    try:
        audio = ID3(file_name)
    except ID3NoHeaderError:
        audio = ID3()
    
    audio.add(TIT2(encoding=3, text=file_title))
    audio.add(TPE1(encoding=3, text=artist_name))
    audio.add(TRCK(encoding=3, text=str(track_number)))
    audio.add(TALB(encoding=3, text=album_name))
    audio.add(TYER(encoding=3, text=str(year)))
    if cover_art_path:
        with open(cover_art_path, 'rb') as img:
            audio.add(APIC(encoding=3, mime='image/jpeg', type=3, desc='Cover', data=img.read()))
    audio.save(file_name)  # Make sure to specify the file_name when saving

    print(f'Generated complex MP3 file at {bit_rate} kbps: {file_name}')

# The rest of your code for calling generate_complex_mp3 remains the same...