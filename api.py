from stable_whisper import load_model
from stable_whisper import stabilize_timestamps
from preprocess import cut_audio
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = load_model('large', device=device)
output_folder = "Audio"
duration = 30


def transcript(audio_path):
    """
         Transcribe an audio file using Whisper

        Parameters
        ----------
        audio_path : str
            audio path to transcript

        Returns
        -------
        list : [{'word': ' Đây', 'timestamp': 0.7699999856948853, 'confidence': 0.9438593640940702},
                {'word': ' là', 'timestamp': 0.8099999725818634, 'confidence': 0.9598403519806485}]
        """
    paths = cut_audio(audio_path, output_folder, duration)

    whole_word_timestamps = []
    for path in paths:
        results = model.transcribe(path, temperature=0.1)
        stab_segments = stabilize_timestamps(results, top_focus=True)
        whole_word_timestamps.extend(stab_segments[0]['whole_word_timestamps'])

    return whole_word_timestamps


whole_word_timestamps = transcript(audio_path="audio.mp3")
for item in whole_word_timestamps:
    print(item)
