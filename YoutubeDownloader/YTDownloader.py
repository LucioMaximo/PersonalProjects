from pytube import YouTube


def YTDownload():
    VidID = input("Enter the video ID (e.g QGAMTlI6XxY): ")
    VidID = "https://www.youtube.com/watch?v="+VidID

    if len(VidID) == 43 :
        print("Downloading now...")
        URL = YouTube(VidID)
        URL = URL.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        URL.download("G:\YouTube Download Folder")

    else:
        print("Your ID was incorrect, please enter it again")
        YTDownload()


YTDownload()
