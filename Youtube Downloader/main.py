from pytube import Search
from selection import selection
# def func
def init():
  ask = input("Download by video title or url? (title/ url)? ")
  if ask.lower() == "title":
    title = input("Title: ")
    s = Search(title)
    url = str(s.results[0])
    url = url[-12:-1]
    url = ("https://www.youtube.com/watch?v={}".format(url))
    if selection(url) == 1:
      init()
  elif ask.lower() == "url":
    url = input("Url: ")
    if selection(url) == 1:
      init()
  else:
    print("I do not understand. ")
    init()




"""
print(yt.streams.filter(progressive=True))

stream = yt.streams.get_by_itag(22)
stream.download()
"""
init()