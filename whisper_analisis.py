import whisper
from yt_downloader import GetFromYoutube
import pandas as pd
import os

def preparation(url, filename=None, extension=".wav"):

    """
    If we do not yet have extracted the audio, we can do it here with
    the youtube url and renaming or not the output file.
    """

    if filename != None: GetFromYoutube(url).get_audio_and_rename(filename, extension)
    else: GetFromYoutube(url).get_audio(extension)

class TranscribeAudio:
    def __init__(self, model):
        self.model = whisper.load_model(model)
        self.result = ""

    def transcribe(self, file, verbose=True):
        self.result = self.model.transcribe(file, verbose=verbose)
        print("-------------- Transcription successfull! --------------")

    def save_WriteTXT(self, destination, filename):
        if self.result != None:
            # call to WriteTXT returns a instance of ResultWriter, saving the destination directory
            txtout = whisper.utils.WriteTXT(destination)
            # call to txtout object writes the segments found to a file name based on target
            txtout(self.result, filename)

            # this way sets up to iterate over all know output formats.
            allout = whisper.utils.get_writer('all', destination)
            allout(self.result, filename)

    def save_DF_as_CSV(self, destination, filename):
        if self.result != None:
            segments_df = pd.DataFrame(self.result['segments'])
            segments_df.to_csv(os.path.join(destination + filename))
            print(f"-------------- {filename} saved in: {destination} --------------")

def one_url():

    #some example videos for testing:
    #url_mrBeast = 'https://www.youtube.com/watch?v=3ryID_SwU5E'
    #url_flagrantCasey = 'https://youtu.be/sdUzors72GQ'

    file = "casey_flagrant_audio.wav"   #file shall be in .wav format preferably
    model = "base.en"

    filename, extension = file.split(".")
    extension = "." + extension

    # If we don't have the audio, get it here. Include url, the desired name of
    # the output file and the extension with a dot preceding it (e.g: .wav)
    #preparation(url_mrBeast, filename, extension)

    transcribed_destination = "transcribed-audio/"
    transcribed_name = str(filename + "_transcribed.csv")

    transcriber = TranscribeAudio(model, file)
    print("-------------- class initialized --------------")
    transcriber.transcribe(verbose=False)    #put False as a parameter to turn off verbose
    transcriber.save_DF_as_CSV(transcribed_destination, transcribed_name)

def multiple_urls(urls_file):

    videos = {}

    #read all urls in path

    with open(urls_file) as file:
        for line in file:
            name, url = line.split(";")
            videos[str(name)] = url

    for video_name, video_link in videos.items():

        model = "base.en"

        extension = ".wav"
        audio_file = video_name + extension

        # If we don't have the audio, get it here. Include url, the desired name of
        # the output file and the extension with a dot preceding it (e.g: .wav)
        preparation(video_link, video_name, extension, rename=True)

        transcribed_destination = "transcribed-audio/"
        transcribed_name = str(video_name + "_transcribed.csv")

        transcriber = TranscribeAudio(model, audio_file)
        transcriber.transcribe(verbose=False)    #put False as a parameter to turn off verbose
        transcriber.save_DF_as_CSV(transcribed_destination, transcribed_name)

def main():
    urls_directory = "urls"
    urls_file = "joeRogan_podcasts.txt"
    urls = urls_directory + "/" + urls_file
    multiple_urls(urls)
    urls_file = "flagrant_podcasts.txt"
    urls = urls_directory + "/" + urls_file
    multiple_urls(urls)

if __name__ == "__main__":
    main()