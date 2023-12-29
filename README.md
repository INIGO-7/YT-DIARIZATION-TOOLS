
# YT-DIARIZATION-TOOLS

## Description
**YouTube diarization tools** automatically diarizes YouTube videos, creating detailed dataframes with speaker-tagged textual interventions. It's perfect for researchers, content creators, and anyone interested in analyzing spoken content in YouTube videos.

## Usage
> Be guided by the [transcribe-and-diarize.ipynb](YT-DIARIZATION-TOOLS/whisper-speaker-recognition/transcribe-and-diarize.ipynb) notebook under YT-DIARIZATION-TOOLS/whisper-speaker-recognition to get separated diarizations and transcriptions of the requested youtube videos\
> \
> Be guided by the [consistency-checker.ipynb](YT-DIARIZATION-TOOLS/consistency-checker.ipynb) notebook under YT-DIARIZATION-TOOLS to link the diarizations and transcriptions obtained before into one data output in the desired dataframe format.


## Features 📋
- **Automatic Speaker Recognition:** Identifies and tags different speakers in the video.
- **Textual Intervention Extraction:** Transcribes spoken content and associates it with the corresponding speaker.
- **Exportable Dataframe:** Outputs data in a user-friendly .csv format.

## Technologies Used 👨‍💻
- Pyannote.audio
- OpenAI Whisper
- yt-dlp
- ffmpeg
- Pandas Library
- Python

## Disclaimer ❗
The tool we use for the diarizations is pyannote.audio, which works really well except for one issue. It consumes an enourmous amount of RAM memory. For videos under 10-15 minutes it will analyze it in a single run, but for longer ones it will eat RAM until the system runs out of it and the kernel crashes.
\
\
To overcome this issue we split the audio and then feed it into the diarization pipeline, but this raises another problem. The diarizations recognize speakers by the name SPEAKER_00, SPEAKER_01, ..., but different splits may have different speaker names. That is why we have to manually listen to every split and link the speaker name -SPEAKER_00, 01, etc- to the real name of that speaker (The repository has the data for diarizations of some podcasts, we can see this speaker-to-name mappings in speakers.py). This can be tedious if we have, for example, many podcasts to process, but we have currently not found another way.
