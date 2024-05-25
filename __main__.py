""" FastAPI + HTMLX """
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Routers
from .routers.pages import router as pages_router

app = FastAPI()
app.include_router(pages_router)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Welcome message"""
    return templates.TemplateResponse(request=request, name="index.html")

def main():
    """Run the server using uvicorn"""
    print("hey")
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info", reload=True)

if __name__ == "__main__":
    main()
