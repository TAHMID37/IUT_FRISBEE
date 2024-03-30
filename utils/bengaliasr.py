import os
import shutil
from transformers import pipeline

MODEL = './model/bengali-whisper-medium'
CHUNK_LENGTH_S = 20.1
BATCH_SIZE = 4

pipe = pipeline(
    task="automatic-speech-recognition",
    model=MODEL,
    tokenizer=MODEL,
    chunk_length_s=CHUNK_LENGTH_S,
    device=0,  # Using CPU , Change it to 0 if you want to use GPU
    batch_size=BATCH_SIZE
)
pipe.model.config.forced_decoder_ids = pipe.tokenizer.get_decoder_prompt_ids(language="bn", task="transcribe")

def convert_bengali_audio_to_text(audio_path: str) -> str:
    try:
        texts = pipe(audio_path, generate_kwargs={"max_length": 260, "num_beams": 4})
        return texts
    except Exception as e:
        return str(e)
