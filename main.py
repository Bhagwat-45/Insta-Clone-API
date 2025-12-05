from fastapi import FastAPI
from db import models
from db.database import engine
from router import user,post
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Instagram API"
)
app.include_router(user.router)
app.include_router(post.router)


@app.get("/")
def root():
    return {
        "message" : "Hello World!!"
    }

models.Base.metadata.create_all(engine)

app.mount('/images',StaticFiles(directory='images'),name='images')