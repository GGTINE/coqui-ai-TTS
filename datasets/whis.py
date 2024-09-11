import os
import argparse

import whisper
import subprocess


parser = argparse.ArgumentParser(description='Change mp3 file to LJ_speech dataset format')
parser.add_argument('--model_size', type=str, default='small', help='Select whisper model size')
parser.add_argument('--file', type=str, default='video.mp3', help='mp3 file to convert')


def create_dataset(args):
    model = whisper.load_model(args.model_size)

    result = model.transcribe(args.file)

    os.makedirs('wavs', exist_ok=True)

    for i, r in enumerate(result['segments']):
        # ffmpeg 명령어 생성
        ffmpeg_command = [
            'ffmpeg', '-y', '-i', args.file,
            '-ss', str(r["start"]),
            '-to', str(r["end"]),
            '-hide_banner', '-loglevel', 'error',
            f'wavs/audio{i+1}.wav'
        ]
        
        # subprocess를 사용해 ffmpeg 명령어 실행
        subprocess.run(ffmpeg_command)

    with open("metadata.txt", "w", encoding="utf-8") as f:
        for i, r in enumerate(result['segments']):
            f.write(f"audio{i+1}|{r['text'].strip()}|{r['text'].strip()}\n")


if __name__ == '__main__':
    args = parser.parse_args()
    create_dataset(args)
