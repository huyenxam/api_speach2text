from pydub import AudioSegment
import os


def cut_audio(input_file, output_folder, duration):
    paths = []
    audio = AudioSegment.from_file(input_file)

    start_time = 0
    end_time = duration * 1000  # Convert to milliseconds

    counter = 1
    while start_time < len(audio):
        output_file = os.path.join(output_folder, f"output_{counter}.mp3")
        audio_segment = audio[start_time:end_time]
        audio_segment.export(output_file, format="mp3")

        start_time = end_time
        end_time += duration * 1000
        counter += 1

        paths.append(output_file)

    return paths

#
# input_file = "audio.mp3"
# output_folder = "Audio"
# duration = 30
#
# cut_audio(input_file, output_folder, duration)
