from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login/")
async def login(username: [None, str] = Form(default=None), password: [None, str] = Form(default=None)):
    return {"username": username, "password": password}