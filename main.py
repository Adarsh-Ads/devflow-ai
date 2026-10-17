from fastapi import FastAPI

app = FastAPI(title="DevFlow AI")


@app.get("/health")
def health_check():
    return {"status": "ok"}