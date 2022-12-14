
#! By HookSander

import os
from pytube import Playlist

def userLink():
    var = input("Entrer votre lien de la playlist YouTube \n=> ")
    downloadFile = Playlist(var)
    return downloadFile


def userPath():
    var = input("Entrer le chemin d'accès du dossier dans lequelle les morceaux seront téléchargés\n=> ")
    return var


def valide():
    user = input("Voulez vous télécharger cette playlist ? [Y/o]\n=> ").lower()
    if user == 'y' :
        return True
    else :
        return False


def download(playlist, uPath):
    playlistLen = len(playlist.videos)
    print("Téléchargement de la playlist : {}\n Nombre de vidéos : {}\n\n".format(playlist.title, playlistLen))
    count = 0
    if valide() :
        for video in playlist.videos :
            count += 1
            print("Téléchargement du morceaux {}/{}\n".format(count, playlistLen))
            audioFile = video.streams.filter(only_audio=True).first()
            file = audioFile.download(output_path=uPath)
            base, ext = os.path.splitext(file)
            newFile = base + ".mp3"
            os.rename(file, newFile)
            nbrChara = len(video.title)
            print("{} a finit de télécharger.\n==============================================\n\n".format(video.title))
        print("Téléchargement terminé.")
    else :
        input("Appuyer sur entrer pour quitter, téléchargement annulé")


if __name__ ==  '__main__' :
    download(userLink(), userPath())
    input = ("Appuyer sur Entrer pour quiter...")