from pytube import YouTube

def selection(link):
  tags = []
  try:
    yt = YouTube(link)
  except:
    print("Invalid link. ")
    return 1
  options = input("Do you want audio or video? (audio/ video) ")
  if options.lower() == "video":
    for i in yt.streams.filter(progressive=True):
      info = str(i).lstrip("<Stream: itag=")
      info = info[:4]
      info = info.strip('"')
      tags.append(info)
    itag = tags[-1]
    stream = yt.streams.get_by_itag(itag)
    stream.download()
    return 0

  elif options.lower() == "audio":
    for i in yt.streams.filter(only_audio=True):
      info = str(i).lstrip("<Stream: itag=")
      info = info[:4]
      info = info.strip('"')
      tags.append(info)
    itag = tags[-1]
    stream = yt.streams.get_by_itag(itag)
    stream.download()
    return 0
  else: 
    print("I don't understand...\n")
    selection(link)
  print("done")