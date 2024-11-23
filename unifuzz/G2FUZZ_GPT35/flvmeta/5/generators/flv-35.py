import os
import struct

class FLVMetadata:
    def __init__(self, duration, creation_date, tags, adaptive_streaming, video_tracks, audio_tracks, subtitles, chapters):
        self.duration = duration
        self.creation_date = creation_date
        self.tags = tags
        self.adaptive_streaming = adaptive_streaming
        self.video_tracks = video_tracks
        self.audio_tracks = audio_tracks
        self.subtitles = subtitles
        self.chapters = chapters

    def to_bytes(self):
        duration_bytes = struct.pack('>I', self.duration)
        creation_date_bytes = struct.pack('>I', self.creation_date)
        tags_bytes = self.tags.encode('utf-8')
        adaptive_streaming_bytes = self.adaptive_streaming.encode('utf-8')
        video_tracks_bytes = b''.join([struct.pack('>I', len(track.encode('utf-8'))) + track.encode('utf-8') for track in self.video_tracks])
        audio_tracks_bytes = b''.join([struct.pack('>I', len(track.encode('utf-8'))) + track.encode('utf-8') for track in self.audio_tracks])
        subtitles_bytes = b''.join([struct.pack('>I', len(subtitle.encode('utf-8'))) + subtitle.encode('utf-8') for subtitle in self.subtitles])
        chapters_bytes = b''.join([struct.pack('>I', len(chapter.encode('utf-8'))) + chapter.encode('utf-8') for chapter in self.chapters])

        data = b'\x02' + struct.pack('>I', len(duration_bytes)) + duration_bytes + \
               b'\x03' + struct.pack('>I', len(creation_date_bytes)) + creation_date_bytes + \
               b'\x08' + struct.pack('>I', len(tags_bytes)) + tags_bytes + \
               b'\x08' + struct.pack('>I', len(adaptive_streaming_bytes)) + adaptive_streaming_bytes + \
               b'\x04' + struct.pack('>I', len(video_tracks_bytes)) + video_tracks_bytes + \
               b'\x05' + struct.pack('>I', len(audio_tracks_bytes)) + audio_tracks_bytes + \
               b'\x06' + struct.pack('>I', len(subtitles_bytes)) + subtitles_bytes + \
               b'\x07' + struct.pack('>I', len(chapters_bytes)) + chapters_bytes

        return data

def save_flv_with_metadata(duration, creation_date, tags, adaptive_streaming, video_tracks, audio_tracks, subtitles, chapters):
    metadata = FLVMetadata(duration, creation_date, tags, adaptive_streaming, video_tracks, audio_tracks, subtitles, chapters)
    flv_data = b'FLV' + b'\x01' + b'\x00\x00\x00\x0D' + metadata.to_bytes()
    
    file_path = './tmp/{}.flv'.format(tags.replace(' ', '_'))
    
    with open(file_path, 'wb') as file:
        file.write(flv_data)

# Generate FLV file with extended metadata
duration = 7200  # in seconds
creation_date = 1635591600  # October 30, 2021 12:00:00 AM UTC
tags = 'extended_video'
adaptive_streaming = 'Advanced Adaptive Streaming: FLV files support dynamic quality adjustments.'
video_tracks = ['Track 1', 'Track 2']
audio_tracks = ['Audio Track 1', 'Audio Track 2']
subtitles = ['English Subtitles', 'Spanish Subtitles']
chapters = ['Chapter 1: Introduction', 'Chapter 2: Main Content', 'Chapter 3: Conclusion']

save_flv_with_metadata(duration, creation_date, tags, adaptive_streaming, video_tracks, audio_tracks, subtitles, chapters)