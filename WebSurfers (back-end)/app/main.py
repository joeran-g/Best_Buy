from fastapi import FastAPI
from app.db import engine, Base
from app.models import user, world, vote
from app.routes import auth


app = FastAPI(title="WebSurfers API")

app.include_router(auth.router)

# Create tables automatically
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "WebSurfers backend running"}
