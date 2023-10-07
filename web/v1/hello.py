from fastapi import APIRouter,FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

router = APIRouter()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/v1", response_class=HTMLResponse)
def hello_world():
    return """
    <html>
        <head>
            <title>Hello, World!</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <img src="\API\static\assets\img\emojilaugh-emoji.gif" alt="Your Image">
        </body>
    </html>
    """
