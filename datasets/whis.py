from pytubefix import YouTube
from pytubefix.cli import on_progress
import whisper
import subprocess


yt = YouTube('https://www.youtube.com/watch?v=wCbUWU4l_Ko', on_progress_callback=on_progress)

#yt.streams.filter(only_audio=True).first().download(output_path='.', filename='input.mp3')

ys = yt.streams.get_audio_only()
ys.download(mp3=True, filename='iu')

model = whisper.load_model("small")

result = model.transcribe('iu.mp3')

for i, r in enumerate(result['segments']):
    # ffmpeg 명령어 생성
    ffmpeg_command = [
        'ffmpeg', '-y', '-i', 'iu.mp3',
        '-ss', str(r["start"]),
        '-to', str(r["end"]),
        '-hide_banner', '-loglevel', 'error',
        f'iu/audio{i+1}.wav'
    ]
    
    # subprocess를 사용해 ffmpeg 명령어 실행
    subprocess.run(ffmpeg_command)

with open("metadata.txt", "w", encoding="utf-8") as f:
    for i, r in enumerate(result['segments']):
        f.write(f"audio{i+1}|{r['text'].strip()}|{r['text'].strip()}\n")

