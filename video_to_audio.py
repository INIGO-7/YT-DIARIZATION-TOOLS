import subprocess

class Video_to_audio:

    def __init__(self, input, output_with_name_and_extension):
        self.input = input
        self.output = output_with_name_and_extension        

    def convert(self):

        """
        ffpeg arguments:
            1.  ffmpeg -> name of the command 
            2.  -i input -> name of the input fil
            3.  -vn -> not take into account the video
            4.  -acodec codecname -> set audio codec
            5.  -ab bitrate -> set bitrate
            6.  -ar sampling -> set sampling rate
            7.  -y -> overwrite if existing
            8.  output -> output file name with extension
        """

        ffmpeg_cmd = [
            "ffmpeg",
            "-i", self.input,
            "-vn",
            "-acodec", "libmp3lame",
            "-ab", "192k",
            "-ar", "44100",
            "-y", 
            self.output
        ]

        try: 
            subprocess.run(ffmpeg_cmd, check=True)
            print("------------------------- Conversion successful! -------------------------")
        except subprocess.CalledProcessError as e:
            print("Conversion failed. Error:", e)

#Video_to_audio("mrbeast_vid.mp4", "mrbeast_audio.wav").convert()