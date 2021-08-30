from pytube import YouTube

url = input("Enter Video url : ")

video_obj = YouTube(url)
file_stream = video_obj.streams.get_highest_resolution()
file_stream.download()