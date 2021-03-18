from pytube import YouTube
link = "https://www.youtube.com/watch?v=QYU8zydUqD8"
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
