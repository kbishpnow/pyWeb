""" FastAPI + HTMLX """
from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_home():
    return """
    <!DOCTYPE html>
    <html lang="en">
        <head></head>
        <body>
            <h1>Hello World</h1>
        </body>
    </html>
    """
