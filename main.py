import os

from fastapi import FastAPI, Header, Depends, Request, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from util import load_artifacts, predict
load_artifacts()

dir_path = os.path.dirname(os.path.realpath(__file__))
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


def valid_content_length(content_length: int = Header(..., lt=2_000_000)):
    return content_length


app.mount("/static", StaticFiles(directory=os.path.join(dir_path, "static")), name="static")

templates = Jinja2Templates(directory=os.path.join(dir_path, "templates"))


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/predict", dependencies=[Depends(valid_content_length)])
def predict(image: UploadFile = File(...)):
    return {"filename": image.filename}


def server():
    """Launched with `poetry run server` at root level"""
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
