from typing import Optional
import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

dir_path = os.path.dirname(os.path.realpath(__file__))
app = FastAPI()

app.mount("/static", StaticFiles(directory=os.path.join(dir_path, "static")), name="static")

templates = Jinja2Templates(directory=os.path.join(dir_path, "templates"))


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/api/predict/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
