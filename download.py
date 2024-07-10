import yt_dlp
import instaloader
import os

class InstaDownload:
    def __init__(self, url):        
        # Create an instaloader object with specific download settings
        self.L = instaloader.Instaloader(
            download_pictures=False,        # Do not download pictures
            download_videos=True,           # Download videos
            download_video_thumbnails=False,# Do not download video thumbnails
            download_geotags=False,         # Do not download geotags
            download_comments=False,        # Do not download comments
            save_metadata=False             # Do not save metadata
        )

        # Extract the shortcode from the URL
        self.shortcode = url.split("/")[-2]

        # Download the reel in the highest quality
        self.download_high_quality_reel()

    def download_high_quality_reel(self):
        try:
            post = instaloader.Post.from_shortcode(self.L.context, self.shortcode)
            if post.is_video:
                # Download the video
                self.L.download_post(post, target="reels")
                print("Download completed successfully.")
                self.display_downloaded_videos()
            else:
                print("The provided link does not contain a video reel.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def display_downloaded_videos(self):
        print("\nDownloaded Videos:")
        # List files in the 'reels' directory
        for filename in os.listdir('reels'):
            if filename.endswith(".mp4"):
                print(f"- {filename}")

class YTDownload:
    def __init__(self, url):
        # Create a YDL object
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])