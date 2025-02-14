from fastapi import FastAPI
import models, database
from routes import router

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)
app.include_router(router)