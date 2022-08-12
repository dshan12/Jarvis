import moviepy.editor as mp
import speech_recognition as sr
import wave
import contextlib
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import sys
import os


def get_audio(filename):
    video = mp.VideoFileClip(filename)
    video.audio.write_audiofile("audio.wav")


def get_file_length(audiofile):
    with contextlib.closing(wave.open(audiofile, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration


def get_text(audiofile="audio.wav"):
    r = sr.Recognizer()
    audio_length = get_file_length(audiofile)
    texts = []
    with sr.AudioFile(audiofile) as source:
        for i in range(0, int(round(audio_length / 3))):
            try:
                text = r.recognize_google(r.record(source, duration=3))
            except sr.UnknownValueError:
                text = "error, no sutitles could be distinguished"
            texts.append(text)
    return texts


def write_text(text_chunks, original_video, output, font_size=35):
    txt_clips = []
    for i in range(len(text_chunks)):
        txt_clips.append(TextClip(text_chunks[i], fontsize=font_size, color="yellow")
                         .set_position('bottom')
                         .set_duration(3)
                         .set_start(i * 3))
    clips = [original_video]
    clips.extend(txt_clips)
    result = CompositeVideoClip(clips)
    result.write_videofile(output)


def del_audio():
    os.remove("audio.wav")


def subtitle(a, b=20, c="output.mp4"):
    get_audio(a)
    write_text(get_text(), VideoFileClip(a), c, b)
    del_audio()
