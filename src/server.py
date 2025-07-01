from fastapi import FastAPI
from src.joke.router import router as joke_router

app = FastAPI(
    title="Joke API",
    description="API cung cấp những câu chuyện đùa bất tận từ các nhân vật.",
    version="1.0.0"
)

# Gắn router từ module joke vào ứng dụng chính
app.include_router(joke_router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Chào mừng đến với Joke API. Truy cập /docs để xem tài liệu API."}