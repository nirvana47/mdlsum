from download import download_video

url = "https://www.youtube.com/watch?v=9FTajHP4JoQ"

output_path = download_video(url)
print(f"Downloaded and converted file: {output_path}")