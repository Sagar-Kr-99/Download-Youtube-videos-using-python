import pytube
link="https://www.youtube.com/watch?v=xUGnp2QPLJk&t=8462s"

yt = pytube.YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()
