from fastapi import FastAPI
# Direct import - Docker already knows where this is!
from common_lib.utils import QwenAudioModel 

app = FastAPI()
active_model = QwenAudioModel()

@app.get("/")
def read_root():
    final_audio = active_model.generate_audio("Testing the interface!")
    return {
        "service": "Qwen Processor", 
        "result": final_audio
    }