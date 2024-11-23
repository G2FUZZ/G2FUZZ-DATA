import os

# Create a directory to save the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

def generate_flv_file(file_name, video_data, cue_points, event_triggers):
    with open(file_name, 'wb') as file:
        file.write(b'FLV Header\n')
        file.write(video_data.encode())
        file.write(b'\n')
        file.write(b'Cue Points: ' + ';'.join(cue_points).encode())
        file.write(b'\n')
        file.write(b'Event Triggers: ' + ';'.join(event_triggers).encode())
        file.write(b'\n')
    print(f'Generated {file_name}')

# Generate FLV files with more complex file structures
file_data = [
    {
        'video_data': 'Video Data: Resolution 1920x1080, Codec H.264',
        'cue_points': ['Cue Point 1 at 00:30', 'Cue Point 2 at 01:45'],
        'event_triggers': ['Event Trigger 1: Pause video', 'Event Trigger 2: Show overlay']
    },
    {
        'video_data': 'Video Data: Resolution 1280x720, Codec VP9',
        'cue_points': ['Cue Point 1 at 00:15', 'Cue Point 2 at 02:00'],
        'event_triggers': ['Event Trigger 1: Display ad', 'Event Trigger 2: Jump to section']
    }
]

for i, data in enumerate(file_data):
    file_name = f'./tmp/complex_file_{i}.flv'
    generate_flv_file(file_name, data['video_data'], data['cue_points'], data['event_triggers'])

print('FLV files with more complex file structures have been generated and saved in ./tmp/')