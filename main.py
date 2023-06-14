from RedDownloader import RedDownloader
from instagrapi import Client
import time
import os
import random

def Billido():
    post=RedDownloader.DownloadBySubreddit('catpics', 1, SortBy="new", quality=720)
    author=post.GetPostAuthors()[0]
    print(f'\nSubreddit: r/kitten')
    print(f'OP: {author}\n')
    return author

#insta sign in ke liye
client=Client()
client.login('USERNAME', 'PASSWORD')

def Captions():
    captions=['#cats, #kittens']

    return random.choice(captions) #idt needed

def Deletion():
    try:
        os.remove('downloaded\downloaded1.jpeg')
    except:
        pass

while True:
    author=Billido()
    hashtag=Captions()
    caption=f'Reddit user: {author}\n\n{hashtag}'
    try:
        client.photo_upload('downloaded\downloaded1.jpeg', caption)
    except Exception as e:
        print(e)
    finally:
        print(f'\nPosted')

    Deletion()
    time.sleep(2000)