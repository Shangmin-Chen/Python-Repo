# pip install pytube3 
# ***make sure to use pytube3 because pytube doesnt work
from pytube import YouTube, Search

def detect(x):
  if "https://" in x or "www.youtube.com".lower() in x:
    return 'url'
  else:
    return 'title'

def init():
  user_input = input('Enter title or url: ')
  # below checks if user entered either title or url
  title_or_url = detect(user_input)
  if title_or_url == 'title':
    # Search function to find based on title
    search_results = Search(user_input)
    # finds the url of the most popular video, read doc for pytube to see why results[0].watch_url works
    user_input_converted = search_results.results[0].watch_url
    # next three lines downloads with url
    my_video = YouTube(user_input_converted)
    my_video_highres = my_video.streams.get_highest_resolution()
    my_video_highres.download()
  elif title_or_url == 'url':
    # next three lines downloads with url
    my_video = YouTube(user_input)
    my_video_highres = my_video.streams.get_highest_resolution()
    my_video_highres.download()
init()
