from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(mp4_file_path, mp3_file_path):
    video = VideoFileClip(mp4_file_path)
    audio = video.audio
    audio.write_audiofile(mp3_file_path)
