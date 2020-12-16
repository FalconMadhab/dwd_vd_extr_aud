
#Download Video
import urllib.request

url_link = "https://videosmaple.s3.ap-south-1.amazonaws.com/test.webm"
urllib.request.urlretrieve(url_link, 'test.webm') 

#Extract Audio
import subprocess
command = "ffmpeg -i test.webm -ab 160k -ac 2 -ar 44100 -vn audio.wav"
subprocess.call(command, shell=True)

