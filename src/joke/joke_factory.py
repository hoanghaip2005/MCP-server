from .providers.base_provider import JokeProvider
from .providers.hoang_jokes import HoangJokeProvider
from .providers.tin_jokes import TinJokeProvider
from typing import Type

# Đăng ký tất cả các provider có sẵn
AVAILABLE_JOKE_PROVIDERS = {
    "hoang": HoangJokeProvider,
    "tin": TinJokeProvider,
}

def get_joke_provider(provider_key: str) -> JokeProvider | None:
    """
    Lấy một instance của joke provider dựa vào key.
    Trả về None nếu không tìm thấy provider.
    """
    provider_class: Type[JokeProvider] = AVAILABLE_JOKE_PROVIDERS.get(provider_key)
    if provider_class:
        return provider_class()
    return None

def get_available_types() -> list[str]:
    """Trả về danh sách các loại joke có sẵn."""
    return list(AVAILABLE_JOKE_PROVIDERS.keys())