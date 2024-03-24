import sys,os,glob
from typing import List
from fastapi import FastAPI, File, UploadFile, Form, HTTPException, status, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi import FastAPI, File, UploadFile
import shutil
import librosa
import warnings
from transformers import pipeline

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,    
    allow_origins=origins,    
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


MODEL = './model/bengali-whisper-medium'
CHUNK_LENGTH_S = 20.1
BATCH_SIZE = 4

pipe = pipeline(
    task="automatic-speech-recognition",
    model=MODEL,
    tokenizer=MODEL,
    chunk_length_s=CHUNK_LENGTH_S,
    device=-1,  # Using CPU , Change it to 0 if u want to use GPU
    batch_size=BATCH_SIZE
)
pipe.model.config.forced_decoder_ids = pipe.tokenizer.get_decoder_prompt_ids(language="bn", task="transcribe")

# this endpoint takes Bengali audio file and converts it to Text
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        os.makedirs("./data/audio", exist_ok=True)
        filename = os.path.join("./data/audio", file.filename)
        with open(filename, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        audio_path = filename
        texts = pipe(audio_path, generate_kwargs={"max_length": 260, "num_beams": 4})
        return {"transcription": texts}
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": str(e)})
    
    