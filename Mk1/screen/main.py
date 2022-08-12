from screen_rec import rec
from threading import Thread
from audio_rec import audio_rec

thread1 = Thread(target=rec)
thread2 = Thread(target=audio_rec)

cmd = 'ffmpeg -y -i ./tmp/recording1.wav  -r 30 -i ./tmp/test.mp4  -filter:a aresample=async=1 -c:a flac -c:v copy av.mkv'
subprocess.call(cmd, shell=True)
print('Mixing Done')