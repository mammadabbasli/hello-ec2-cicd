from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message":"CI/CD is LIVE 🚀"}

