import os
import struct

class FLVMetadata:
    def __init__(self, duration, creation_date, tags, chapter_markers, has_3d_support, audio_tracks, video_tracks, subtitles, custom_metadata):
        self.duration = duration
        self.creation_date = creation_date
        self.tags = tags
        self.chapter_markers = chapter_markers
        self.has_3d_support = has_3d_support
        self.audio_tracks = audio_tracks
        self.video_tracks = video_tracks
        self.subtitles = subtitles
        self.custom_metadata = custom_metadata

    def to_bytes(self):
        duration_bytes = struct.pack('>I', self.duration)
        creation_date_bytes = struct.pack('>I', self.creation_date)
        tags_bytes = self.tags.encode('utf-8')
        chapter_markers_bytes = self.chapter_markers.encode('utf-8')
        audio_tracks_bytes = self.audio_tracks.encode('utf-8')
        video_tracks_bytes = self.video_tracks.encode('utf-8')
        subtitles_bytes = self.subtitles.encode('utf-8')
        custom_metadata_bytes = self.custom_metadata.encode('utf-8')

        has_3d_support_byte = b'\x0A' + struct.pack('?', self.has_3d_support)

        data = b'\x02' + struct.pack('>I', len(duration_bytes)) + duration_bytes + \
               b'\x03' + struct.pack('>I', len(creation_date_bytes)) + creation_date_bytes + \
               b'\x08' + struct.pack('>I', len(tags_bytes)) + tags_bytes + \
               b'\x09' + struct.pack('>I', len(chapter_markers_bytes)) + chapter_markers_bytes + \
               b'\x0B' + struct.pack('>I', len(audio_tracks_bytes)) + audio_tracks_bytes + \
               b'\x0C' + struct.pack('>I', len(video_tracks_bytes)) + video_tracks_bytes + \
               b'\x0D' + struct.pack('>I', len(subtitles_bytes)) + subtitles_bytes + \
               b'\x0E' + struct.pack('>I', len(custom_metadata_bytes)) + custom_metadata_bytes + \
               has_3d_support_byte

        return data

def save_flv_with_metadata(duration, creation_date, tags, chapter_markers, has_3d_support, audio_tracks, video_tracks, subtitles, custom_metadata):
    metadata = FLVMetadata(duration, creation_date, tags, chapter_markers, has_3d_support, audio_tracks, video_tracks, subtitles, custom_metadata)
    flv_data = b'FLV' + b'\x01' + b'\x00\x00\x00\x0D' + metadata.to_bytes()

    file_path = './tmp/{}.flv'.format(tags.replace(' ', '_'))

    with open(file_path, 'wb') as file:
        file.write(flv_data)

# Generate FLV file with extended metadata and features
duration = 7200  # in seconds
creation_date = 1635591600  # October 30, 2021 12:00:00 AM UTC
tags = 'example_video_extended'
chapter_markers = 'Chapter 1: Introduction; Chapter 2: Main Content; Chapter 3: Conclusion'
has_3d_support = True
audio_tracks = 'English, Spanish'
video_tracks = '1080p, 4k'
subtitles = 'English, Spanish'
custom_metadata = 'Custom Metadata: Additional information about the video'

save_flv_with_metadata(duration, creation_date, tags, chapter_markers, has_3d_support, audio_tracks, video_tracks, subtitles, custom_metadata)