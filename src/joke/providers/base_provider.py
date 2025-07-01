from abc import ABC, abstractmethod
import random

class JokeProvider(ABC):
    """Lớp cơ sở trừu tượng cho các nhà cung cấp truyện cười."""

    @abstractmethod
    def get_jokes(self) -> list[str]:
        """Trả về một danh sách các câu truyện cười."""
        pass

    def get_random_joke(self) -> str:
        """Trả về một câu truyện cười ngẫu nhiên."""
        jokes = self.get_jokes()
        if not jokes:
            return "Hôm nay không có gì vui để kể cả."
        return random.choice(jokes)