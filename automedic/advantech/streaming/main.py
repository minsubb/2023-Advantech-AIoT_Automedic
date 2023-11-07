from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from camera import get_stream_video

app = FastAPI()

def video_streaming():
    return get_stream_video()

@app.get("/")
def main():
    return StreamingResponse(video_streaming(), media_type="multipart/x-mixed-replace; boundary=frame")


@app.get("/home")
def home():
    return {"message": "home"}