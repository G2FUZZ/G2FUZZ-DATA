import os
import struct

def create_flv_file_with_metadata_frame_rate_and_audio_tracks(file_path, metadata, frame_rate, audio_tracks):
    # Ensure the tmp directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # FLV header
    flv_header = b'FLV\x01\x05\x00\x00\x00\x09'  # FLV Version 1, Video + Audio, Header Length 9
    # PreviousTagSize0
    previous_tag_size_0 = b'\x00\x00\x00\x00'

    # Script tag "onMetaData"
    # First, prepare the metadata body
    script_data = b''
    script_data += b'\x02\x00\x0AonMetaData'  # ScriptDataString 'onMetaData'
    script_data += b'\x08'  # ECMA array marker

    # Adding frameRate to the metadata
    metadata['frameRate'] = frame_rate

    # Adding multiLanguageAudioTracks to the metadata
    metadata['multiLanguageAudioTracks'] = len(audio_tracks)

    script_data += struct.pack('>L', len(metadata) + len(audio_tracks))  # Array length including audio tracks

    for key, value in metadata.items():
        key_length = len(key)
        script_data += struct.pack('>H', key_length)  # String length
        script_data += key.encode('utf-8')  # String data
        if isinstance(value, str):
            script_data += b'\x02'  # Type: String
            value_length = len(value)
            script_data += struct.pack('>H', value_length)  # String length
            script_data += value.encode('utf-8')  # String data
        elif isinstance(value, (int, float)):
            script_data += b'\x00'  # Type: Number (double)
            script_data += struct.pack('>d', value)  # Number value
        elif isinstance(value, bool):  # Handling Boolean for canSeekToEnd
            script_data += b'\x01'  # Type: Boolean
            script_data += struct.pack('>?', value)  # Boolean value

    # Adding audio tracks metadata
    for track_id, language_code in enumerate(audio_tracks, start=1):
        track_key = f'audioTrack{track_id}'
        track_key_length = len(track_key)
        script_data += struct.pack('>H', track_key_length)
        script_data += track_key.encode('utf-8')
        script_data += b'\x02'
        language_code_length = len(language_code)
        script_data += struct.pack('>H', language_code_length)
        script_data += language_code.encode('utf-8')

    script_data += b'\x00\x00\x09'  # Object end marker

    # ScriptTagHeader
    script_tag_header = b'\x12'  # Tag type script data
    data_size = len(script_data)
    timestamp = 0
    stream_id = 0
    script_tag_header += struct.pack('>L', data_size << 8 | timestamp)  # Data size and timestamp
    script_tag_header += struct.pack('>L', stream_id)[:-1]  # StreamID always 0

    with open(file_path, 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size_0)
        f.write(script_tag_header)
        f.write(script_data)
        # Write PreviousTagSize after the tag
        f.write(struct.pack('>L', len(script_tag_header) + data_size))

if __name__ == '__main__':
    file_path = './tmp/sample_with_audio_tracks.flv'
    metadata = {
        'duration': 0,  # Duration in seconds
        'width': 640,  # Video width
        'height': 480,  # Video height
        'videocodecid': 7,  # Codec ID for AVC
        'audiocodecid': 10,  # Codec ID for AAC
        'canSeekToEnd': True,  # Boolean indicating if one can seek to the end
    }
    frame_rate = 30.0  # Adjustable Frame Rate
    audio_tracks = ['en', 'es', 'fr']  # Audio track language codes
    create_flv_file_with_metadata_frame_rate_and_audio_tracks(file_path, metadata, frame_rate, audio_tracks)