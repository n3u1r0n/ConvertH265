import fire
import os

def convert(i, o, crf=26):
    for filename in os.listdir(i):
        if filename.lower().endswith('.mp4'):
            os.system('ffmpeg -i "{}" -c:v libx265 -c:a copy -x265-params crf={} "{}"'\
                .format(os.path.join(i, filename), crf, os.path.join(o, filename)))
        else:
            os.system('cp "{}" "{}"'.format(os.path.join(i, filename), os.path.join(o, filename)))

if __name__ == '__main__':
    fire.Fire(convert)