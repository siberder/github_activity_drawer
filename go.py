import os
import datetime
import random
import subprocess

### Git

date_format = '%Y.%m.%dT%H:%M:%S'


def git(*args):
    return subprocess.check_call(['git'] + list(args))


def create_commit(date):
    message = "hello world"
    fname = "hi.txt"
    with open(fname, "w+") as f:
        r = "hi " + str(random.randint(0, 9999999))
        f.write(r)

    # git commit --date "Wed Feb 16 14:00 2037 +0100"
    date_str = date.strftime(date_format)
    git("add", fname)
    git("commit", "-m", message, "--date", date_str)




from PIL import Image
im = Image.open("input2.png")
px = im.load() 
width, height = im.size

s_date = datetime.datetime.strptime("2017.01.01T12:12:12", date_format)

print(width)
print(height)

for w in range(0, width):
    for h in range(0, height):
        d = w * height + h
        cur_date = s_date + datetime.timedelta(days=d)
        if px[w, h] == (0, 0, 0, 255):
            print(px[w, h])
            print(f"{cur_date}")
            create_commit(cur_date)