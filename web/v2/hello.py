from fastapi import APIRouter

router = APIRouter()

@router.get("/v2")
def hello_world():
    return {"message": "Hello, World!"}

# <div class="tenor-gif-embed" data-postid="22496814" data-share-method="host" data-aspect-ratio="1" data-width="100%"><a
#         href="https://tenor.com/view/emojilaugh-emoji-laughing-gif-22496814">Emojilaugh Laughing GIF</a>from <a
#         href="https://tenor.com/search/emojilaugh-gifs">Emojilaugh GIFs</a></div>
# <script type="text/javascript" async src="https://tenor.com/embed.js">

# </script>