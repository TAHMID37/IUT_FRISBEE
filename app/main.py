import os,shutil
from fastapi import FastAPI, File, UploadFile, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from utils.bengaliasr import convert_bengali_audio_to_text
from utils.generate_meeting_minutes import generate_meeting_minutes
from utils.englishasr import convert_eng_audio_to_text
from models.meetingtext import MeetingContext
from fastapi.responses import StreamingResponse
from prompt.bn_sys import bn_system_prompt
from prompt.en_sys import en_system_prompt 
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,    
    allow_origins=origins,    
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# this endpoint takes Bengali audio file and converts it to Text
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        os.makedirs("./data/audio", exist_ok=True)
        filename = os.path.join("./data/audio", file.filename)
        with open(filename, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        audio_path = filename
        transcription = convert_bengali_audio_to_text(audio_path)
        return {"transcription": transcription}
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": str(e)})
    

# this endpoint takes English audio file and converts it to Text
@app.post("/upload_eng/")
async def upload_file(file: UploadFile = File(...)):
    try:
        os.makedirs("./data/eng", exist_ok=True)
        filename = os.path.join("./data/eng", file.filename)
        with open(filename, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        audio_path = filename
        transcription = convert_eng_audio_to_text(audio_path)
        return {"transcription": transcription}
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": str(e)})
    


@app.post("/bangla_meeting_minutes")
async def bangla_meeting_minutes(context: MeetingContext):
    try:
        #meeting_minutes = generate_bangla_meeting_minutes(context.text)
        #return {"meeting_minutes": meeting_minutes}
        return generate_meeting_minutes(context.text,bn_system_prompt)      
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/english_meeting_minutes")
async def english_meeting_minutes(context: MeetingContext):
    try:
        #meeting_minutes = generate_bangla_meeting_minutes(context.text)
        #return {"meeting_minutes": meeting_minutes}
        return generate_meeting_minutes(context.text,en_system_prompt)      
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

