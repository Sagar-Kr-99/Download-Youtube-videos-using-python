# importing the module
from pytube import YouTube


# where to save
SAVE_PATH = "H:/IITG VIDEOS/" #to_do

# link of the video to be downloaded
link="https://www.youtube.com/watch?v=xUGnp2QPLJk&t=8462s"

yt = YouTube(link)



try:
    yt.streams.filter(progressive = True, 
file_extension = "mp4").first().download(output_path = "H:\IITG VIDEOS", 
filename = "Reiner and Bertholdt Transformation scene")
except:
    print("Some Error!")


print('Task Completed!')
