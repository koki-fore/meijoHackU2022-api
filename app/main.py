from typing import Union

from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware

from app.routers import categories, challenge_categories, challenges, challenges_completed, comments, follows, likes, posts, users


app = FastAPI()
app.include_router(posts.router)
app.include_router(categories.router)
app.include_router(challenge_categories.router)
app.include_router(challenges_completed.router)
app.include_router(challenges.router)
app.include_router(comments.router)
app.include_router(follows.router)
app.include_router(likes.router)
app.include_router(users.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return{"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q:Union[str, None] = None):
    return {"item_id": item_id, "q": q} 