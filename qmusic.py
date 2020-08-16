import json
import threading
import subprocess

import requests
from bs4 import BeautifulSoup


def requestData():
    URL = "http://api.qmusic.be/2.4/tracks/plays?limit=1&next=true"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = json.loads(str(soup))
    return data


def printSong():
    threading.Timer(30.0, printSong).start()

    data = requestData()
    # get the current songname
    songname = data['played_tracks'][0]['title']

    # check if we need this song
    songChecker(songname.upper())


def songChecker(songname):
    needed_songs = ['WAKE ME UP', '---', 'NEVER GROWING UP', '---', '---']

    if songname in needed_songs:
        print(songname + " is momenteel aan het spelen!")

        for i in range(5):
            if songname == needed_songs[i]:
                file = 'song' + str(i+1) + '.sh'
                process = subprocess.run(file, shell=True, check=True, timeout=10)

printSong()
