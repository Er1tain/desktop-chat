from fastapi import FastAPI, Response

app = FastAPI()

@app.get('/dialogues')
async def GetDialogues(a: int, b: int, c: int):
    pass