""" FastAPI + HTMLX """
from fastapi import FastAPI
import uvicorn

# Routers
from .routers.pages import router as pages_router

app = FastAPI()
app.include_router(pages_router)

@app.get("/")
async def read_root():
    """Welcome message"""
    return {"message": "Welcome to the API!"}

def main():
    """Run the server using uvicorn"""
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info", reload=True)

if __name__ == "__main__":
    main()
