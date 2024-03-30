import whisper

small_model = whisper.load_model("./model/english-whisper-small/small.pt",device="cuda")
# small_model = whisper.load_model("./model/english-whisper-small/small.pt")

def convert_eng_audio_to_text(audio_path: str) -> str:
    try:
        texts =small_model.transcribe(audio_path, fp16=False)
        return texts["text"]
    except Exception as e:
        return str(e)
