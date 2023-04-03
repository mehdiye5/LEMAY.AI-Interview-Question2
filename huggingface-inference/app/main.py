from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    text: str
    model_name: str
    task: str

def generate_output(text, model_name, task):
    model = pipeline(task, model=model_name)
    result = model(text)
    for item in result:
        yield str(item)

# text: str, model_name: str, task: str

@app.post("/predict")
async def predict(data : Data):    
    text = data.text
    model_name = data.model_name
    task = data.task
    output_generator = generate_output(text, model_name, task)
    return StreamingResponse(output_generator, media_type="text/plain")