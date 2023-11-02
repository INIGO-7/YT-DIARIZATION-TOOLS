from pydub import AudioSegment

def split_wav_pydub(filename, fragment_duration):
    # Load the audio file
    audio = AudioSegment.from_wav(filename)

    # Calculate the length of each split in milliseconds
    fragment_duration_ms = fragment_duration * 1000

    # Calculate the number of splits

    num_splits = (len(audio) // fragment_duration_ms) + 1
    
    # Split the file and save each part
    for i in range(num_splits):
        # Calculate the start and end of the split
        start = i * fragment_duration_ms

        #we want to get audio for each interval, and then the last which will be smaller
        if i != num_splits - 1:
            end = start + fragment_duration_ms
        else:
            end = start + (len(audio) - start)
        # Extract the split audio
        split_audio = audio[start:end]
        # Export the split audio to a new .wav file
        split_audio.export(f'/audio_fragments/output_{i+1}.wav', format='wav')

# Use the function to split the .wav file
#split_wav_pydub('whisper-speaker-recognition/input_prep.wav', 1800)  # Split by every 30 minutes
