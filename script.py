
#! By HookSander

import os
from pytube import Playlist

def userLink():
    var = input("Enter your youtube's playlist link here \n=> ")
    downloadFile = Playlist(var)
    return downloadFile


def userPath():
    var = input("Enter the path of the download \n=> ")
    return var


def valide():
    user = input("Do you want to download the playlist ? [Y/n]\n=> ").lower()
    if user == 'y' :
        return True
    else :
        return False


def download(playlist, uPath):
    playlistLen = len(playlist.videos)
    print("Downloading : {}\n Number of video : {}\n\n".format(playlist.title, playlistLen))
    count = 0
    if valide() :
        for video in playlist.videos :
            count += 1
            print("Download track : {}/{}\n".format(count, playlistLen))
            audioFile = video.streams.filter(only_audio=True).first()
            file = audioFile.download(output_path=uPath)
            base, ext = os.path.splitext(file)
            newFile = base + ".mp3"
            os.rename(file, newFile)
            nbrChara = len(video.title)
            print("{} done.\n==============================================\n\n".format(video.title))
        print("Download down.")
    else :
        input("Enter to exit, download cancel")


if __name__ ==  '__main__' :
    download(userLink(), userPath())
    input = ("Press enter to exit...")