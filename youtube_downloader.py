from pytube import YouTube
import os

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        ys = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}")
        ys.download(save_path)
        print("Download completed!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    save_path = input("Enter the path where the video will be saved: ")
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    download_video(url, save_path)
