from fastapi import FastAPI
from app.routes import router
from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router, prefix="/items")
