from pytube import YouTube as YT
import os

class GetFromYoutube:
    def __init__(self, url):
        self.url = url

    def get_video_and_rename(self, output_name):

        """
        Download a video in mp4 format and rename as desired.
        """

        video = YT(self.url).streams.get_highest_resolution()
        #out_file will store the absolute path where the video will be placed.
        out_file = video.download()
        #get the directory (and the filename, it will almost always be "name of video".mp4 but we won't need it)
        directory, _ = os.path.split(out_file)
        #Change the name of the file
        new_file = os.path.join(directory, output_name + ".mp4")
        os.rename(out_file, new_file)

        if os.path.exists(new_file):
            print("-------------- Video download successful --------------")
        else:
            print("--- ERROR ERROR --- VIDEO DOWNLOAD UNSUCCESSFUL --- ERROR ERROR ---")

    def get_audio_and_rename(self, output_name, extension):

        """
        Downloads the audio of a video, for some reason it is given in
        mp4 format, so we change the extension renaming it to
        whichever we want (it seems to work for now).
        """

        video = YT(self.url).streams.filter(only_audio=True).get_audio_only()
        #out_file will store the absolute path where the video will be placed.
        out_file = video.download()
        #get the directory and the extension (will almost always be .mp4, but we won't need it)
        directory, _ = os.path.split(out_file)
        #put the real extension
        new_file = os.path.join(directory, output_name + extension)
        os.rename(out_file, new_file)

        if os.path.exists(new_file):
            print("-------------- Video download successful --------------")
        else:
            print("--- ERROR ERROR --- VIDEO DOWNLOAD UNSUCCESSFUL --- ERROR ERROR ---")

    def get_video(self):

        """
        Download a video in mp4 format.
        """
        video = YT(self.url).streams.get_highest_resolution()
        video.download()
        print("-------------- Video download successful --------------")

    def get_audio(self, extension):

        """
        Downloads the audio of a video, for some reason it is given in
        mp4 format, so we change the extension (it works for now).
        """

        video = YT(self.url).streams.filter(only_audio=True).get_audio_only()
        #out_file will store the absolute path where the video will be placed.
        out_file = video.download()
        #get the directory and the extension (will almost always be .mp4, but we won't need it)
        pathname, _ = os.path.splitext(out_file)
        #put the real extension
        new_file = pathname + extension
        os.rename(out_file, new_file)
        print("-------------- Audio download successful --------------")

#url_mrBeast = 'https://www.youtube.com/watch?v=3ryID_SwU5E'
# url_flagrantCasey = 'https://youtu.be/sdUzors72GQ'
# url_joeRoganMiley = 'https://www.youtube.com/watch?v=D7WUMXKV-FE'
# GetFromYoutube(url_joeRoganMiley).get_audio_and_rename("miley", ".wav")