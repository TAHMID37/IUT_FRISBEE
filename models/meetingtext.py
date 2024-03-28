from pydantic import BaseModel

class MeetingContext(BaseModel):
    text: str