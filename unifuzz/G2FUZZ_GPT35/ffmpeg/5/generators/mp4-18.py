import ffmpeg
import subprocess

# Create a video with chapters
input_file = ffmpeg.input('test.mp4')
output_file = './tmp/video_with_chapters_DRM_and_ChapterMetadata.mp4'

chapters = {
    'chapter1': 10,  # Chapter name and timestamp in seconds
    'chapter2': 30,
    'chapter3': 60
}

chapter_args = []
for chapter_name, timestamp in chapters.items():
    chapter_args.extend(['-metadata', f'chapter={chapter_name}:{timestamp}'])

drm_args = [
    '-encryption_scheme', 'cbcs',
    '-encryption_key', '0123456789ABCDEF0123456789ABCDEF',
    '-encryption_kid', '0123456789ABCDEF0123456789ABCDEF'
]

chapter_metadata_args = [
    '-metadata', 'title=Chapter Metadata Feature',
    '-metadata', 'comment=Generated video with chapters, DRM, and Chapter Metadata'
]

cmd = ffmpeg.concat(input_file).output(output_file, **{'c': 'copy', 'f': 'mp4', 'metadata:s:v:0': 'handler=video', 'metadata:s:a:0': 'handler=audio', 'metadata:s:v:0': 'title=Test Video', 'metadata:s:a:0': 'title=Test Audio', 'metadata:s:v:0': 'comment=Generated video with chapters, DRM, and Chapter Metadata', 'metadata:s:a:0': 'comment=Generated audio with chapters, DRM, and Chapter Metadata'}, cmd=chapter_args + drm_args + chapter_metadata_args).compile()

try:
    subprocess.run(cmd, check=True, stderr=subprocess.PIPE)
except subprocess.CalledProcessError as e:
    print("ffmpeg error:", e.stderr.decode())