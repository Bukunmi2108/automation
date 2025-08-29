from pytube import YouTube
from sys import argv

link = input("Enter the YouTube Video Link: ")

yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)


"""
NOT FUNCTIONAL
"""