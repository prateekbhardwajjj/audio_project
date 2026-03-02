from fastapi import FastAPI
from common_lib.utils import FutureFastModel 

app = FastAPI()
active_model = FutureFastModel()

@app.get("/")
def read_root():
    final_audio = active_model.generate_audio("Testing the interface!")
    return {
        "service": "Chatterbox text-to-speech", 
        "result": final_audio
    }