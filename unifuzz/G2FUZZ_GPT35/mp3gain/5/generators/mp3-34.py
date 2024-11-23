import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TPE2, TALB, TCON, COMM

mp3_file_path = './tmp/complex_sample.mp3'

if os.path.exists(mp3_file_path):
    mp3_file = MP3(mp3_file_path, ID3=ID3)

    mp3_file.add_tags()

    mp3_file['TIT2'] = TIT2(encoding=3, text='Complex Sample Song')
    mp3_file['TPE1'] = TPE1(encoding=3, text='John Doe, Jane Smith')
    mp3_file['TPE2'] = TPE2(encoding=3, text='Various Artists')
    mp3_file['TALB'] = TALB(encoding=3, text='Complex Album')
    mp3_file['TCON'] = TCON(encoding=3, text='Pop')

    mp3_file.tags.add(
        COMM(
            encoding=3,
            lang='eng',
            desc='Comment',
            text='This is a complex sample mp3 file with multiple artists and composers.'
        )
    )

    with open('sample_image.jpg', 'rb') as img:
        mp3_file.tags.add(
            APIC(
                encoding=3,
                mime='image/jpeg',
                type=3,  # Album front cover
                desc='Cover',
                data=img.read()
            )
        )

    mp3_file.save()
else:
    print(f"Error: File '{mp3_file_path}' not found.")