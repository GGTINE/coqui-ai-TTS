import argparse

from pytubefix import YouTube
from pytubefix.cli import on_progress


parser = argparse.ArgumentParser(description='Download mp3 file via YouTube link.')
parser.add_argument('--link', type=str, required=True, help='YouTube link to download')
parser.add_argument('--filename', type=str, default='video', help='mp3 file name to save')


def download(args):
    yt = YouTube(args.link, on_progress_callback=on_progress)

    ys = yt.streams.get_audio_only()
    ys.download(mp3=True, filename=args.filename)


if __name__ == '__main__':
    args = parser.parse_args()
    download(args)

