import torch
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

model_path = "./model/Wav2Vec2-large-xlsr-hindi"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
processor = Wav2Vec2Processor.from_pretrained(model_path)
model = Wav2Vec2ForCTC.from_pretrained(model_path).to(device)
resampler = torchaudio.transforms.Resample(48_000, 16_000)

def convert_hindi_audio_to_text(audio_file_path: str) -> str:
    speech_array, _ = torchaudio.load(audio_file_path)
    speech_array = resampler(speech_array).squeeze().numpy()
    inputs = processor(speech_array, sampling_rate=16_000, return_tensors="pt", padding=True)
    
    with torch.no_grad():
        logits = model(inputs.input_values.to(device), attention_mask=inputs.attention_mask.to(device)).logits
    
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)[0]
    
    return transcription

