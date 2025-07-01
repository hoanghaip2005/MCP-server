from fastapi import APIRouter, HTTPException, Path
from . import joke_factory

# Tạo một router riêng cho module joke
router = APIRouter(
    prefix="/api/jokes",  # Tiền tố cho tất cả API trong router này
    tags=["Jokes"]        # Gom nhóm API trong tài liệu Swagger UI
)

@router.get("/")
def get_joke_types():
    """
    API để xem tất cả các loại truyện cười hiện có.
    Đây là cách bạn "chọn các api có sẵn" như đã đề cập.
    """
    return {"available_types": joke_factory.get_available_types()}

@router.get("/{joke_type}")
def get_a_joke(
    joke_type: str = Path(..., title="Loại truyện cười", description="Chọn 'hoang' hoặc 'tin'.")
):
    """
    API chính để lấy một truyện cười ngẫu nhiên theo loại được chọn.
    """
    provider = joke_factory.get_joke_provider(joke_type.lower())

    if not provider:
        raise HTTPException(
            status_code=404,
            detail=f"Không tìm thấy loại truyện cười '{joke_type}'. Các loại hiện có: {joke_factory.get_available_types()}"
        )

    joke = provider.get_random_joke()
    return {"joke_type": joke_type, "joke": joke}