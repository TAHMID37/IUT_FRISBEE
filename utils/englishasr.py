import whisper,torch

device = "cuda:0" if torch.cuda.is_available() else "cpu"
small_model = whisper.load_model("./model/english-whisper-small/small.pt",device=device)
# small_model = whisper.load_model("./model/english-whisper-small/small.pt")

def convert_eng_audio_to_text(audio_path: str) -> str:
    try:
        texts =small_model.transcribe(audio_path, fp16=False)
        return texts["text"]
    except Exception as e:
        return str(e)
