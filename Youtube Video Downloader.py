from pytube import YouTube

youtube_video_url="Enter Video URL"

try:
    yt_obj = YouTube(youtube_video_url)

    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

    filters.get_highest_resolution().download()
    print('Video Downloaded Successfully')
except Exception as e:
    print(e)